# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/6/2 11:13
# @author  : Mo
# @function: cluster of word2vec and t-sne plt-show


from __future__ import print_function
from text_analysis.conf.path_log import logger
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import multiprocessing
import sys
import os


def train_word2vec_by_word(path_in, path_out):
    """计算 词级别 词向量
    train word2vec by word
    Args:
        path_in: String, path_in/origin text,  eg. "新闻.txt"
        path_out: String, path_out/save text,  eg. "w2v.vec"
    Returns:

    """
    model = Word2Vec(LineSentence(path_in), size=300,  window=7, min_count=1,
                     sg=1, hs=1, iter=10, workers=multiprocessing.cpu_count())
    # model.save(path_out)
    model.wv.save_word2vec_format(path_out, binary=False)


def train_word2vec_by_char(path_in, path_out):
    """计算 字级别 词向量
    train word2vec by char
    Args:
        path_in: String, path_in/origin text,  eg. "新闻.txt"
        path_out: String, path_out/save text,  eg. "w2v.vec"
    Returns:

    """
    model = Word2Vec(LineSentence(path_in), size=300, window=7, min_count=1,
                     sg=1, hs=1, iter=10, workers=multiprocessing.cpu_count())
    # model.save(path_out)
    model.wv.save_word2vec_format(path_out, binary=False)


def os_main(path_in_dir, path_save_dir):
    """ 训练词向量 """
    path_in = os.path.join(path_save_dir, "中文分词", "汇总大文本.md")
    path_out = os.path.join(path_save_dir, "词向量", "w2v.vec")
    path_out_dir = os.path.dirname(path_out)
    if not os.path.exists(path_out_dir):
        os.makedirs(path_out_dir)
    train_word2vec_by_word(path_in, path_out)
    # train_word2vec_by_char(path_in, path_out)
    logger.info("w05_train_w2v.py ok")
    ta = 0


if __name__ == '__main__':

    path_in = "../data/corpus/分析结果/中文分词/汇总大文本.md"
    path_out = "../data/corpus/分析结果/词向量/w2v.vec"
    path_out_dir = os.path.dirname(path_out)
    if not os.path.exists(path_out_dir):
        os.makedirs(path_out_dir)
    train_word2vec_by_word(path_in, path_out)
    # train_word2vec_by_char(path_in, path_out)
    ta = 0




