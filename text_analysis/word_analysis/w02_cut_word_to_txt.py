# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2021/10/23 10:14
# @author  : Mo
# @function: cut word txt, 将txt文档切词


from text_analysis.utils.text_common import txt_read, txt_write, get_all_dirs_files
from text_analysis.conf.path_log import logger
import jieba
import os


def cut_word_to_txt(path_in_dir, path_save_dir=None, path_keywords_field="keywords/keywords_field.txt"):
    """切词存储到txt文件中
    cut word to txt
    Args:
        path_in_dir: String, path_in_dicr/origin text,  eg. "dir_txt"
        path_save_dir: String, path_save_dir/save text,  eg. "dir_txt_cut"
        path_keywords_field: String, path_keywords_field/keywords file,  eg. "keywords_field.txt"
        path_keywords_common: String, path_keywords_common/keywords file,  eg. "keywords_common.txt"
        path_keywords_newword: String, path_keywords_newword/keywords file,  eg. "keywords_newword.txt"    Returns:
    Returns:
        None
    """
    # 原有的关键词
    keywords_field = open(path_keywords_field, "r", encoding="utf-8").readlines()
    keywords_field = [kf.strip() for kf in keywords_field]
    for kf in keywords_field:
        jieba.add_word(kf, 12000)
    # 创建存储的目录名
    if path_save_dir:
        if not os.path.exists(path_save_dir):
            os.mkdir(path_save_dir)
    else:  # 如果没有就存在原目录
        path_save_dir = path_in_dir
    # 切词
    files = get_all_dirs_files(path_in_dir)
    texts_all = []
    for file in files:
        if ".txt" in file and ".切词.txt" not in file:
            texts = open(file, "r", encoding="utf-8").readlines()
            texts = ["/".join(jieba.lcut(t, HMM=True)) for t in texts if t.strip()]
            # 最后一层文件名
            file_name = file.replace(path_in_dir, "").strip("/").strip("\\")
            file_name = file_name.replace(file_name.split(".")[-1], "切词.txt")
            path_save_file = os.path.join(path_save_dir, file_name)
            txt_write(texts, path_save_file)
            texts_all += [t.replace("/", " ") for t in texts]
    txt_write(texts_all, os.path.join(path_save_dir, "汇总大文本.md"))
    ta = 0


def os_main(path_in_dir, path_save_dir):
    """ 切词 """
    # path_in_dir = "../data/corpus/分析结果/文本语料"
    # path_save_dir = "../data/corpus/分析结果/中文分词"

    path_in_dir = os.path.join(path_save_dir, "文本语料")
    path_save_dir = os.path.join(path_save_dir, "中文分词")

    cut_word_to_txt(path_in_dir, path_save_dir, path_keywords_field="keywords/keywords_field.txt")
    logger.info("w02_cut_word_to_txt.py ok!")
    ta = 0


if __name__ == '__main__':

    path_in_dir = "../data/corpus/分析结果/文本语料"
    path_save_dir = "../data/corpus/分析结果/中文分词"
    cut_word_to_txt(path_in_dir, path_save_dir, path_keywords_field="keywords/keywords_field.txt")
    ta = 0

