# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/6/2 11:13
# @author  : Mo
# @function: cluster of word2vec and t-sne plt-show


from text_analysis.utils.text_common import save_json, load_json, get_all_dirs_files
from text_analysis.utils.text_ml import load_word2vec_format
from text_analysis.conf.path_log import logger
from typing import Union, Dict, Any, Tuple
import sklearn.discriminant_analysis
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
import sklearn.random_projection
import matplotlib.pyplot as plt
import sklearn.decomposition
import sklearn.datasets
import sklearn.ensemble
import sklearn.manifold
import pandas as pd
import numpy as np
# import gensim
import re
import os


def cluster_w2v_file(path_emmbed:str, path_in_file:str, path_save_file:str, cluster_type:str="dbscan",
                n_clusters:int=3200, limit:int=None):

    # 只聚类当前file
    lines = open(path_in_file, "r", encoding="utf-8").readlines()
    lins_sp = [re.split(r"[ |\/]", ls.strip()) for ls in lines if ls.strip()]
    file_words = set()
    for ls in lins_sp:
        for w in ls:
            if w and w not in file_words:
                file_words.add(w)

    # 获取词向量
    vector_vs = load_word2vec_format(path_emmbed, limit=limit, length_word=2) # 只要2个字以上成词的
    keys = []
    vector_v = []
    for k,v in vector_vs.items():
        if k in file_words:
            vector_v.append(v)
            keys.append(k)

    # 聚类
    if cluster_type == "kmeans":
        # k-means聚类
        try:
            clf = KMeans(n_clusters=n_clusters)
            clf.fit(vector_v)
        except Exception as e:
            clf = KMeans()
            clf.fit(vector_v)
        cluster_centers_ = clf.cluster_centers_
        labels_ = clf.labels_
    elif cluster_type == "dbscan":
        clf = DBSCAN(eps=0.2, min_samples=3, metric="cosine")
        clf.fit(vector_v)
        cluster_centers_ = clf.components_
        labels_ = clf.labels_
    
    # labels_ int 转 str
    labels_ = [str(ls) for ls in labels_]
    label_words = {}
    for i in range(len(labels_)):
        if labels_[i] not in label_words:
            label_words[labels_[i]] = [keys[i]]
        else:
            label_words[labels_[i]] += [keys[i]]
    # 存储
    len_max = max([len(e) for e in list(label_words.values())])
    for k,v in label_words.items():
        label_words[k] += [""] * (len_max-len(label_words[k]))
    label_words = dict(sorted(label_words.items(), key=lambda x:int(x[0]), reverse=False))
    pd_lw = pd.DataFrame(label_words)
    pd_lw.to_excel(path_save_file)


def cluster_w2v(path_emmbed, path_in_dir, path_save_dir, cluster_type:str="dbscan", n_clusters:int=3200, limit:int=None):
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
    files = get_all_dirs_files(path_in_dir)
    for file in files:
        if (".切词." in file or ".md" in file) and ".新词." not in file\
                and ".词频." not in file:
            # 最后一层文件名
            file_name = file.replace(path_in_dir, "").strip("/").strip("\\")
            file_name = file_name.replace(file_name.split(".")[-1], "xlsx")
            path_save_file = os.path.join(path_save_dir, file_name)
            cluster_w2v_file(path_emmbed, file, path_save_file, cluster_type, n_clusters, limit)
    ta = 0


def os_main(path_in_dir, path_save_dir):
    """ 词语聚类 """

    path_emmbed = os.path.join(path_save_dir, "词向量", "w2v.vec")
    path_in_dir = os.path.join(path_save_dir, "中文分词")
    path_save_dir = os.path.join(path_save_dir, "词语聚类")

    # path_in_dir = "../data/corpus/分析结果/中文分词"
    # path_save_dir = "../data/corpus/分析结果/词语聚类"
    # path_emmbed = "../data/corpus/分析结果/词向量/w2v.vec"
    # cluster_type = "kmeans"
    # n_clusters = 32
    # limit = None

    cluster_type = "kmeans"
    n_clusters = 32
    limit = None

    cluster_w2v(path_emmbed, path_in_dir, path_save_dir, cluster_type, n_clusters, limit)
    logger.info("w06_cluster_w2v.py ok")
    ta = 0


if __name__=="__main__":

    path_in_dir = "../data/corpus/分析结果/中文分词"
    path_save_dir = "../data/corpus/分析结果/词语聚类"
    path_emmbed = "../data/corpus/分析结果/词向量/w2v.vec"

    # cluster_type = "kmeans"
    # n_clusters = 32
    # limit = None

    cluster_type = "kmeans"
    n_clusters = 32
    limit = None

    cluster_w2v(path_emmbed, path_in_dir, path_save_dir, cluster_type, n_clusters, limit)
    ee = 0


