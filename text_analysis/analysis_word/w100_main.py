# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2021/10/24 22:59
# @author  : Mo
# @function: 运行 * 总


# 适配linux
import sys
import os
path_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
print(path_root)
sys.path.append(path_root)
from text_analysis.analysis_word.w00_transfer_file_to_txt import os_main as os_main_1
from text_analysis.analysis_word.w01_find_newword_txt import os_main as os_main_2
from text_analysis.analysis_word.w02_cut_word_to_txt import os_main as os_main_3
from text_analysis.analysis_word.w03_transfer_to_doc import os_main as os_main_4
from text_analysis.analysis_word.w04_tfidf_xlsx import os_main as os_main_5
from text_analysis.analysis_word.w05_train_w2v import os_main as os_main_6
from text_analysis.analysis_word.w06_cluster_w2v import os_main as os_main_7
from text_analysis.analysis_word.w07_cluster_sen import os_main as os_main_8
from text_analysis.analysis_word.w08_extract_highligt_doc import os_main as os_main_9
from text_analysis.conf.path_log import logger


def run_os_cmd(orders):
    """运行命令行
    run os cmd
    Args:
        orders: List, orders,  eg. "新闻.txt"
    Returns:

    """
    # os.system("activate tf115")
    for o in orders:
        cmd = "python  " + o
        print(cmd)
        os.system(cmd)


def run_word_analysis(path_in_dir, path_save_dir):
    """运行命令行
    run os cmd
    Args:
        path_in_dir: String, path-in,  eg. "../data/corpus/原始语料"
        path_save_dir: String, path-save,  eg. "../data/corpus/分析结果"
    Returns:
        None
    """
    os_main_1(path_in_dir, path_save_dir)
    os_main_2(path_in_dir, path_save_dir)
    os_main_3(path_in_dir, path_save_dir)
    os_main_4(path_in_dir, path_save_dir)
    os_main_5(path_in_dir, path_save_dir)
    os_main_6(path_in_dir, path_save_dir)
    os_main_7(path_in_dir, path_save_dir)
    os_main_8(path_in_dir, path_save_dir)
    os_main_9(path_in_dir, path_save_dir)


if __name__ == '__main__':

    ## 方法一, 有时win10会报错
    # orders = ["w00_transfer_file_to_txt.py",
    #         "w01_find_newword_txt.py",
    #         "w02_cut_word_to_txt.py",
    #         "w03_transfer_to_doc.py",
    #         "w04_tfidf_xlsx.py",
    #         "w05_train_w2v.py",
    #         "w06_cluster_w2v.py",]
    # os.system(" activate tf20 ")
    # # 放在全局里边
    # for o in orders:
    #     cmd = "python  " + o
    #     print(cmd)
    #     os.system(cmd)
    # ta = 0



    ## 方法二
    path_in_dir = "../data/corpus/原始语料"
    path_save_dir = "../data/corpus/分析结果"
    run_word_analysis(path_in_dir, path_save_dir)

    ta = 0

