# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/6/2 21:43
# @author  : Mo
# @function: text tools of machine learning, 机器学习文本数据分析基础函数


from sklearn.feature_extraction.text import TfidfVectorizer
from text_analysis.conf.path_log import logger
from typing import Union, Any, Dict
import jieba.posseg as pseg
import pandas as pd
import numpy as np
import logging
import jieba
import json
import re
import os


jieba.setLogLevel(logging.INFO)


__all__ = ["macropodus_keyword",
           "macropodus_encode",
           "macropodus_newword",
           "macropodus_cut",
           "jieba_tag_cut",
           "jieba_cut",
           "extract_chinese",
           "cut_sentence",
           "remove_urls",
           "read_and_process",
           "gram_uni_bi_tri",
           "tfidf_fit",
           ]


re_continue = re.compile("[A-Za-z0-9.@_]", re.U)
re_zh_cn = re.compile("([\u4E00-\u9FD5]+)", re.U)


def macropodus_encode(text):
    """
    Macropodus encode of word2vec
    :param text: input sentence
    :return: list
    """
    from macropodus.similarity import swc
    return swc.encode(text)


def macropodus_newword(text):
    """
    Macropodus find newword
    :param text: input sentence
    :return: list
    """
    import macropodus
    return macropodus.find(text)


def macropodus_keyword(text, num=8):
    """
    Macropodus keyword
    :param text: input sentence
    :return: list
    """
    import macropodus
    return list(macropodus.keyword(text, num=num))


def macropodus_cut(text):
    """
    Macropodus cut
    :param text: input sentence
    :return: list
    """
    import macropodus
    return list(macropodus.cut(text))


def jieba_tag_cut(text):
    """
        jieba cut and tagged
    :param text:str 
    :return: dict
    """
    words = pseg.cut(text)
    return dict(words)


def jieba_cut(text):
    """
      Jieba cut
    :param text: input sentence
    :return: list
    """
    return list(jieba.cut(text, cut_all=False, HMM=False))


def cut_sentence2(sentence):
    """
        分句
    :param sentence:str
    :return:list
    """
    # re_sen = re.compile('[:;!?。：；？！\n\r]')
    re_sen = re.compile('[:;!?。：；？！\n\r]')
    #.不加是因为不确定.是小数还是英文句号(中文省略号......)
    sentences = re_sen.split(sentence)
    sen_cuts = []
    for sen in sentences:
        if sen and str(sen).strip():
            sen_cuts.append(sen)
    return sen_cuts


def cut_sentence(text, use_type="summarize"):
    """
        分句(文本摘要)
    :param sentence:str, like "大漠帝国"
    :param use_type:str, like "summarize" or "new-word-discovery"
    :return:list
    """
    if use_type=="summarize":
        re_sen = re.compile('[:;!?。：；？！\n\r]') #.不加是因为不确定.是小数还是英文句号(中文省略号......)
    elif use_type=="new-word-discovery":
        re_sen = re.compile('[,，"“”、<>《》{}【】:;!?。：；？！\n\r]') #.不加是因为不确定.是小数还是英文句号(中文省略号......)
    else:
        raise RuntimeError("use_type must be 'summarize' or 'new-word-discovery'")
    sentences = re_sen.split(text)
    sen_cuts = []
    for sen in sentences:
        if sen and str(sen).strip():
            sen_cuts.append(sen)
    return sen_cuts


def extract_chinese(text):
    """
      只提取出中文、字母和数字
    :param text: str, input of sentence
    :return: 
    """
    chinese_exttract = ''.join(re.findall(u"([\u4e00-\u9fa5A-Za-z0-9@. ])", text))
    return chinese_exttract


def extract_html_text(text):
    """获取html中的text
    extract html text
    Args:
        text: String, text/origin text,  eg. "叉尾斗鱼介绍"
    Returns:
        passages: List<tuple>, 文章段落
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()
    passages = [t.replace("\xa0", "").replace("\n", "").replace("\t", "")+"\n" for t in text.split("\n")
               if t.replace("\xa0", "").replace("\n", "").replace("\t", "")]
    return passages


def remove_webtags(text):
    """
        删除所有的html标签, 只有<>, 会存在<!--> <--!>
    :param text: str
    :return: str
    """
    re_webtag = re.compile(r"<[^>]+>", re.S)
    text_remove = re_webtag.sub("", text)
    return text_remove


def remove_urls(text):
    """
        删除https/http等无用url
    :param text: str
    :return: str
    """
    text_remove_url = re.sub(r"(全文：)?(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b",
                             "", text, flags=re.MULTILINE)
    return text_remove_url


def read_and_process(path):
    """
      读取文本数据并
    :param path: 
    :return: 
    """
    data = pd.read_csv(path)
    ques = data["ques"].values.tolist()
    labels = data["label"].values.tolist()
    line_x = [extract_chinese(str(line).upper()) for line in labels]
    line_y = [extract_chinese(str(line).upper()) for line in ques]
    return line_x, line_y


def gram_uni_bi_tri(text):
    """
        获取文本的unigram, trugram, bigram等特征
    :param text: str
    :return: list
    """
    len_text = len(text)
    gram_uni = []
    gram_bi = []
    gram_tri = []
    for i in range(len_text):
        if i + 3 <= len_text:
            gram_uni.append(text[i])
            gram_bi.append(text[i:i+2])
            gram_tri.append(text[i:i+3])
        elif i + 2 <= len_text:
            gram_uni.append(text[i])
            gram_bi.append(text[i:i+2])
        elif i + 1 <= len_text:
            gram_uni.append(text[i])
        else:
            break
    return gram_uni, gram_bi, gram_tri


def get_ngrams(text, ns=[1], use_type="summarize", len_max=7):
    """
        获取文本的ngram等特征
    :param text: str, like "大漠帝国"
    :param ns: list, like [1, 2, 3]
    :param type: str, like "summarize" or "new-word-discovery"
    :param type: int, like 6, 7
    :return: list<list> or list
    """
    if type(ns) != list:
        raise RuntimeError("ns of function get_ngram() must be list!")
    for n in ns:
        if n < 1:
            raise RuntimeError("enum of ns must '>1'!")
    len_text = len(text)
    ngrams = []
    if use_type == "summarize": # 分别返回uni, bi, tri...
        for n in ns:
            ngram_n = []
            for i in range(len_text):
                if i + n <= len_text:
                    ngram_n.append(text[i:i + n])
                else:
                    break
            if not ngram_n:
                ngram_n.append(text)
            ngrams.append(ngram_n)
    else: # 只返回一个list
        for i in range(len_text):
            ngrams += [text[i: j + i]
                       for j in range(1, min(len_max + 1, len_text - i + 1))]
    return ngrams


def tfidf_fit(sentences, max_features=50000):
    """
       tfidf相似度
    :param sentences: 
    :return: 
    """
    # tfidf计算
    model = TfidfVectorizer(ngram_range=(1, 2), # 3,5
                            stop_words=[' ', '\t', '\n'],  # 停用词
                            max_features=max_features,
                            token_pattern=r"(?u)\b\w+\b",  # 过滤停用词
                            min_df=1,
                            max_df=0.95,
                            use_idf=1,  # 光滑
                            smooth_idf=1,  # 光滑
                            sublinear_tf=1, )  # 光滑
    matrix = model.fit_transform(sentences)
    return matrix


def load_word2vec_format(path: str, encoding: str = "utf-8", dtype: Union[np.float32, np.float16] = np.float16,
                         limit: int = None, length_word: int=1) -> Dict:
    """
    Load word2vec from word2vec-format file, 加载词向量文件
    Args:
        path: file path of saved word2vec-format file.
        encoding: If you save the word2vec model using non-utf8 encoding for words, specify that encoding in `encoding`.
        dtype: Can coerce dimensions to a non-default float type (such as `np.float16`) to save memory.
        limit: the limit of the words of word2vec
    Returns:
        dict of word2vec
    """
    w2v = {}
    count = 0
    with open(path, "r", encoding=encoding) as fr:
        for line in fr:
            count += 1
            if count > 1:  # 第一条不取
                idx = line.index(" ")
                word = line[:idx]
                if len(word)>=length_word:
                    vecotr = line[idx + 1:]
                    vector = np.fromstring(vecotr, sep=" ", dtype=dtype)
                    w2v[word] = vector
            # limit限定返回词向量个数
            if limit and count >= limit:
                break
    return w2v

