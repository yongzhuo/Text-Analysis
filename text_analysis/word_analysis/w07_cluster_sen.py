# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/5/27 21:12
# @author  : Mo
# @function: text-cluster 文本聚类


from text_analysis.utils.text_common import save_json, load_json, get_all_dirs_files
from text_analysis.utils.text_ml import tfidf_fit, macropodus_encode, macropodus_cut
from text_analysis.utils.text_ml import cut_sentence, extract_chinese
from text_analysis.utils.words import stop_words
from text_analysis.conf.path_log import logger
# sklearn
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import NMF
#
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.metrics import *
#
from typing import Any, List
import pandas as pd
import numpy as np
import os


class TextCluster:
    def __init__(self):
        self.stop_words = stop_words.values()
        self.algorithm = "k-means"

    def cluster_tfidf(self, text: Any, n_clusters: int=5, topic_min: int=5, use_combine: bool=True,
                      topic_type: str="none", cluster_type: str="kmeans", encode_type: str="tfidf"):
        """
        聚类, 可传入List或str
        Args:
            text: str, text or list, input docs
            n_clusters: int, number of clusters center
            topic_min: int, topic number, eg. 8
            use_combine: bool, whether use combine or not 
            topic_type: str, topic type, eg. "NMF", "LSI", "LDA", "NONE"
            cluster_type: str, cluster type, eg. "kmeans", "dbscan", "hierarchical", "meanshift", "spectralclustering"
        Returns:
            Label: List
        """
        # 切句
        if type(text) == str:
            self.sentences = cut_sentence(text)
        elif type(text) == list:
            self.sentences = text
        else:
            raise RuntimeError("text type must be list or str")
        # 切词
        sentences_cut = [[word for word in macropodus_cut(extract_chinese(sentence))
                          if word.strip()] for sentence in self.sentences]
        # 去除停用词等
        self.sentences_cut = [list(filter(lambda x: x not in self.stop_words, sc)) for sc in sentences_cut]
        self.sentences_cut = [" ".join(sc) for sc in self.sentences_cut]

        logger.info("切词切句完成!")
        if encode_type == "tfidf":
            # 计算每个句子的tfidf
            sen_vector = tfidf_fit(self.sentences_cut).toarray()
        elif encode_type == "word2vec":
            sen_vector = []
            for sent in self.sentences_cut:
                sent_vector = macropodus_encode(sent)
                sen_vector.append(sent_vector)
            sen_vector = np.array(sen_vector)
        logger.info("vector 构建完成!")

        logger.info("tfidf构建完成!")

        # 主题数, 经验判断
        topic_num = min(topic_min, int(len(sentences_cut) / 2))  # 设定最小主题数为3
        # 降维
        iter_nums = 320
        if topic_type == "nmf":
            model_topic = NMF(n_components=topic_num, max_iter=iter_nums)
            vector_u = model_topic.fit_transform(sen_vector.T) # 基矩阵 or 权重矩阵
            vector_v = model_topic.components_                # 系数矩阵 or 降维矩阵
        elif topic_type == "lsi":
            model_topic = TruncatedSVD(n_components=topic_num, n_iter=iter_nums)
            vector_u = model_topic.fit_transform(sen_vector.T)
            vector_v = model_topic.components_
        elif topic_type == "lda":
            model_topic = LatentDirichletAllocation(n_components=topic_num, max_iter=iter_nums,
                                            learning_method='online',
                                            learning_offset=50.,
                                            random_state=2020)
            vector_u = model_topic.fit_transform(sen_vector.T)
            vector_v = model_topic.components_
        else:
            vector_v = sen_vector

        logger.info("语料降维完成!")
        # 主题模型
        if topic_type in ["nmf", "lsi", "lda"]:
            # 对每列(一个句子topic_num个主题),得分进行排序,0为最大
            idxs = np.argmax(vector_v, axis=0)
            labels_ = idxs.tolist()
        else:
            ###########聚类
            if cluster_type=="kmeans":
                # k-means聚类
                clf = KMeans(n_clusters=n_clusters)
                clf.fit(vector_v)
                cluster_centers_ = clf.cluster_centers_
                labels_ = clf.labels_
            elif cluster_type=="dbscan":
                # eps[认为相邻的最大距离], min_samples[成类的最小个数]
                clf = DBSCAN(eps=0.5, min_samples=5, metric="cosine")
                clf.fit(vector_v)
                cluster_centers_ = clf.components_
                labels_ = clf.labels_
            elif cluster_type=="hierarchical": # 层次聚类
                clf = AgglomerativeClustering(n_clusters=n_clusters, affinity="cosine", linkage="average")
                clf.fit(vector_v)
                cluster_centers_ = clf.children_
                labels_ = clf.labels_
            elif cluster_type=="meanshift":
                bandwidth_ = estimate_bandwidth(vector_v, quantile=0.2)
                clf = MeanShift(bandwidth=bandwidth_, bin_seeding=True)
                clf.fit(vector_v)
                cluster_centers_ = clf.cluster_centers_
                labels_ = clf.labels_
            else:
                clf = SpectralClustering(n_clusters=n_clusters, random_state=2020)
                clf.fit(vector_v)
                cluster_centers_ = clf.affinity_matrix_
                labels_ = clf.labels_
            score_sc, score_chs = self.cluster_metrics(vector_v, labels_)
            logger.info(("silhouette_score", "calinski_harabaz_score"))
            logger.info((score_sc, score_chs))
        # 输出选择
        labels_ = [str(li) for li in labels_]
        res_combine = {}
        if use_combine: # 按label汇合起来
            for i in range(len(labels_)):
                if labels_[i] not in res_combine:
                    res_combine[labels_[i]] = [self.sentences[i]]
                else:
                    res_combine[labels_[i]] += [self.sentences[i]]
        else:  # 按原句顺序输出label
            res_combine = {"label_question":[labels_[i], self.sentences[i]] for i in range(len(labels_))}
        return res_combine

    def cluster_metrics(self, X, y_pred):
        """
        评估指标
        """
        # 轮廓系数 Silhouette Coefficient和Calinski-Harabasz Index
        score_sc = silhouette_score(X, y_pred, metric="euclidean")    # 轮廓系数, 同类别相近而不同类别越远, 分数越高
        score_chs = calinski_harabaz_score(X, y_pred)                 # CHI, 越大越好
        # score_ari = adjusted_rand_score(X, y_pred)  # 兰德系数, Adjusted Rand index
        # score_ml = adjusted_mutual_info_score(X, y_pred)  # 互信息
        # return score_sc, score_ari, score_ml
        return score_sc, score_chs


def cluster_sen(path_in_dir, path_save_dir, n_clusters:int=3200, cluster_type:str="dbscan",
                topic_type:str="none", encode_type:str="word2vec"):
    """聚类词向量
    cluster w2v
    Args:
        path_emmbed: String, path_emmbed/embedd word,  eg. "w2v.vec"
        path_in_dir: String, path_in_dicr/origin text,  eg. "dir_txt"
        path_save_dir: String, path_save_dir/save text,  eg. "dir_txt_cut"
        cluster_type: String, cluster_type,  eg. "dir_txt_cut"
        n_clusters: Int, n_clusters,  eg. 32
        limit: String, Int, limit,  eg. 100000
    Returns:

    """
    # 创建存储的目录名
    if path_save_dir:
        if not os.path.exists(path_save_dir):
            os.mkdir(path_save_dir)
    else:  # 如果没有就存在原目录
        path_save_dir = path_in_dir

    # 聚类
    k_cluster = TextCluster()
    # cluster_type = "kmeans"  # "kmeans", "dbscan", "hierarchical", "meanshift", "spectralclustering"
    # topic_type = "none"      # "nmf", "lsi", "lda", "name"
    # encode_type = "tfidf"    # "tfidf", "word2vec"
    # n_clusters = 32
    # 聚类
    files = get_all_dirs_files(path_in_dir)
    for file in files:
        if (".txt" in file or ".md" in file) and ".新词." not in file and ".切词." not in file \
                and ".词频." not in file:
            questions = open(file, "r", encoding="utf-8").readlines()
            questions = [q for q in questions if q.strip()]
            # 最后一层文件名
            file_name = file.replace(path_in_dir, "").strip("/").strip("\\")
            file_name = file_name.replace(file_name.split(".")[-1], "xlsx")
            path_save_file = os.path.join(path_save_dir, file_name)
            kcc = k_cluster.cluster_tfidf(text=questions, n_clusters=n_clusters, topic_min=n_clusters, use_combine=True,
                                          topic_type=topic_type, cluster_type=cluster_type, encode_type=encode_type)
            # 存储
            len_max = max([len(e) for e in list(kcc.values())])
            for k, v in kcc.items():
                kcc[k] += [""] * (len_max - len(kcc[k]))
            pd_kcc = pd.DataFrame(kcc)
            pd_kcc.to_excel(path_save_file)
    ta = 0


def os_main(path_in_dir, path_save_dir):
    """ 句子聚类 """
    # path_in_dir = "../data/corpus/分析结果/文本语料"
    # path_save_dir = "../data/corpus/分析结果/句子聚类"

    path_in_dir = os.path.join(path_save_dir, "文本语料")
    path_save_dir = os.path.join(path_save_dir, "句子聚类")

    # k_cluster = TextCluster()
    cluster_type = "kmeans"  # "kmeans", "dbscan", "hierarchical", "meanshift", "spectralclustering"
    topic_type = "none"  # "nmf", "lsi", "lda", "name"
    encode_type = "word2vec"  # "tfidf", "word2vec"
    n_clusters = 32

    cluster_sen(path_in_dir, path_save_dir, n_clusters, cluster_type, topic_type, encode_type)
    logger.info("w07_cluster_sen.py ok")
    ta = 0


if __name__ == '__main__':

    path_in_dir = "../data/corpus/分析结果/文本语料"
    path_save_dir = "../data/corpus/分析结果/句子聚类"

    k_cluster = TextCluster()
    cluster_type = "kmeans"  # "kmeans", "dbscan", "hierarchical", "meanshift", "spectralclustering"
    topic_type = "none"  # "nmf", "lsi", "lda", "name"
    encode_type = "word2vec"  # "tfidf", "word2vec"
    n_clusters = 32
    questions = []

    cluster_sen(path_in_dir, path_save_dir, n_clusters, cluster_type, topic_type)
    ta = 0


