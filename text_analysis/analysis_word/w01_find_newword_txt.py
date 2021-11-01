# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2021/10/24 20:15
# @author  : Mo
# @function: 新词发现


from text_analysis.utils.text_common import txt_read, txt_write, get_all_dirs_files
from text_analysis.conf.path_log import logger
from word_discovery import WordDiscovery
import pandas as pd
import os


def find_newword_txt(path_in_dir, path_save_dir=None):
    """计算新词到txt/xlsx
    find newword txt
    Args:
        path_in_dir: String, path_in_dicr/origin text,  eg. "dir_txt"
        path_save_dir: String, path_save_dir/save text,  eg. "dir_txt_cut"
    Returns:

    """
    # 创建存储的目录名
    if path_save_dir:
        if not os.path.exists(path_save_dir):
            os.mkdir(path_save_dir)
    else:  # 如果没有就存在原目录
        path_save_dir = path_in_dir
    files = get_all_dirs_files(path_in_dir)
    big_texts = ""
    for file in files:
        if ".txt" in file and ".切词.txt" not in file and ".词频.txt" not in file:
            texts = open(file, "r", encoding="utf-8").readlines()
            big_text = "".join(texts).replace("\n", "")
            big_texts += big_text
            # 新词发现-文本
            wd = WordDiscovery()
            res = wd.find_word(text=big_text, use_type="text", use_avg=False, use_filter=True, use_output=True,
                               freq_min=2, len_max=10, entropy_min=2.0, aggregation_min=3.2)
            res_dict = {"word": [], "f": [], "s": [], "a": [], "r": [], "l": [], "ns": []}
            for k, v in res.items():
                res_dict["word"] += [k]
                for k2, v2 in v.items():
                    res_dict[k2] += [v2]
            pf = pd.DataFrame(res_dict)
            file_name = file.replace(path_in_dir, "").strip("/").strip("\\")
            file_name = file_name.replace(file_name.split(".")[-1], "新词.xlsx")
            path_save_file = os.path.join(path_save_dir, file_name)
            pf.to_excel(path_save_file, encoding='utf-8', index=False)
    # 汇总新词发现-文本
    wd = WordDiscovery()
    res = wd.find_word(text=big_texts, use_type="text", use_avg=False, use_filter=True, use_output=True,
                       freq_min=2, len_max=10, entropy_min=2.0, aggregation_min=3.2)
    res_dict = {"word": [], "f": [], "s": [], "a": [], "r": [], "l": [], "ns": []}
    for k, v in res.items():
        res_dict["word"] += [k]
        for k2, v2 in v.items():
            res_dict[k2] += [v2]
    pf = pd.DataFrame(res_dict)
    path_save_file = os.path.join(path_save_dir, "汇总新词.xlsx")
    pf.to_excel(path_save_file, encoding='utf-8', index=False)
    # 关键词只存储6%
    res_sort = [w[0].strip()+"\n" for w in sorted(res.items(), key=lambda x: x[1]["s"], reverse=True)]
    len_6 = int(0.6 * len(res_sort))
    path_save_keywords = "keywords/keywords_newword.txt"
    txt_write(res_sort[:len_6], path_save_keywords)



def os_main(path_in_dir, path_save_dir):
    """ 新词发现 """
    # path_in_dir = "../data/corpus/分析结果/文本语料"
    # path_save_dir = "../data/corpus/分析结果/新词发现"

    path_in_dir = os.path.join(path_save_dir, "文本语料")
    path_save_dir = os.path.join(path_save_dir, "新词发现")
    find_newword_txt(path_in_dir, path_save_dir)
    logger.info("w01_find_newword_txt.py ok!")


if __name__ == '__main__':

    path_in_dir = "../data/corpus/分析结果/文本语料"
    path_save_dir = "../data/corpus/分析结果/新词发现"
    find_newword_txt(path_in_dir, path_save_dir)
    ta = 0

