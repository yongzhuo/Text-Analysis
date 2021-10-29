# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2021/10/29 11:23
# @author  : Mo
# @function: 从docx抽取标颜色的文本


from text_analysis.utils.text_common import docx_read, pdf_read, txt_read, txt_write, get_all_dirs_files
from text_analysis.utils.text_ml import remove_urls, remove_webtags
from text_analysis.utils.text_common import docx_extract_color
from text_analysis.conf.path_log import logger
import html
import os


def extract_highligt_doc(path_in_dir, path_save_dir=None, highligt_colors=["YELLOW"]):
    """将某个目录下的word文档转化为txt
    Args:
        path_dir: String, path_in/origin text,  eg. "叉尾斗鱼介绍.docx"
        path_save_dir: String, path_save_dir/save text,  eg. "叉尾斗鱼介绍.docx"
        highligt_colors: List, enum/highligt colors,  eg. ["YELLOW", "RED"]
    Returns:
        passages: List<tuple>, 文章段落
    """
    # 创建存储的目录名
    if path_save_dir:
        if not os.path.exists(path_save_dir):
            os.makedirs(path_save_dir)
    else:  # 如果没有就存在原目录
        path_save_dir = path_in_dir
    # 所有文件名
    files = get_all_dirs_files(path_in_dir)
    file_name_suffix = [".docx", ".doc"]
    big_texts = []
    # 转换
    for file in files:
        # 过滤不符合的后缀
        is_suffix = [fns for fns in file_name_suffix if fns in file]
        if is_suffix:
            passages = docx_extract_color(file, highligt_colors)
            big_texts += passages
    path_save_file = os.path.join(path_save_dir, "汇总高亮文本.md")
    txt_write(big_texts, path_save_file)


def os_main(path_in_dir, path_save_dir):
    """ 将word文档转换为txt文档 """
    # path_in_dir = "../data/corpus/原始语料"
    # path_save_dir = "../data/corpus/分析结果/高亮语料"

    path_save_dir = os.path.join(path_save_dir, "高亮语料")

    highligt_colors = ["YELLOW"]  # ["DARK_YELLOW", "BRIGHTGREEN", "YELLOW", "GREEN", "BLUE", "RED"]
    extract_highligt_doc(path_in_dir, path_save_dir, highligt_colors)
    logger.info("w08_extract_highligt_doc.py ok")


if __name__ == '__main__':
    # path = "../data/corpus/16001_送马秀才.html"


    # path_dir = "../../test/corpus"
    # files = get_dir_files(path_dir)
    # # file_name_suffix = [".docx", ".doc", ".html", "htm", ".txt"]
    # for file in files:
    #     transfer_file_to_txt(file)
    # ee = 0

    path_in_dir = "../data/corpus/原始语料"
    path_save_dir = "../data/corpus/分析结果/高亮语料"
    extract_highligt_doc(path_in_dir, path_save_dir)

