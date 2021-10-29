# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2021/10/23 10:14
# @author  : Mo
# @function: transfer word to txt, 将word文档转换为txt文档


from text_analysis.utils.text_common import docx_read, pdf_read, txt_read, txt_write, get_all_dirs_files
from text_analysis.utils.text_ml import extract_html_text, remove_urls, remove_webtags
from text_analysis.conf.path_log import logger
import os


def transfer_file_to_txt(path_in, path_save_dir=None):
    """读取word文档的段落数据text, docx
    read corpus from docx
    Args:
        path_in: String, path_in/origin text,  eg. "叉尾斗鱼介绍.docx"
        path_save_dir: String, path_save_dir/save text,  eg. "叉尾斗鱼介绍.docx"
    Returns:
        passages: List<tuple>, 文章段落
    """
    # 如果存储地址为None, 则默认
    path_in = os.path.abspath(path_in)
    path_in_dir = os.path.dirname(path_in)
    if not path_save_dir:
        path_save_dir = path_in_dir
    file_name = path_in.replace(path_in_dir, "").strip("/").strip("\\")
    # 读取html, docx, txt等
    if path_in.endswith(".docx") or path_in.endswith(".doc"):
        passages = docx_read(path_in)
    elif path_in.endswith(".pdf"):
        passages = pdf_read(path_in)
    elif path_in.endswith(".html") or path_in.endswith(".htm"):
        passages = txt_read(path_in)
        passages = extract_html_text("\n".join(passages))
    else:
        passages = txt_read(path_in)
    # 文章内容存储
    file_name = file_name.replace(file_name.split(".")[-1], "txt")
    path_save = os.path.join(path_save_dir, file_name)
    txt_write(passages, path_save)
    return passages


def transfer_dir_to_txt(path_in_dir, path_save_dir=None):
    """将某个目录下的word文档转化为txt
    Args:
        path_dir: String, path_in/origin text,  eg. "叉尾斗鱼介绍.docx"
        path_save_dir: String, path_save_dir/save text,  eg. "叉尾斗鱼介绍.docx"
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
    file_name_suffix = [".docx", ".doc", ".html", "htm", ".txt"]
    big_texts = []
    # 转换
    for file in files:
        # 过滤不符合的后缀
        is_suffix = [fns for fns in file_name_suffix if fns in file]
        if is_suffix:
            passages = transfer_file_to_txt(file, path_save_dir)
            big_texts += passages
    path_save_file = os.path.join(path_save_dir, "汇总大文本.md")
    txt_write(big_texts, path_save_file)


def os_main(path_in_dir, path_save_dir):
    """ 将word文档转换为txt文档 """
    path_save_dir = os.path.join(path_save_dir, "文本语料")
    transfer_dir_to_txt(path_in_dir, path_save_dir)
    logger.info("w00_transfer_file_to_txt.py ok!")


if __name__ == "__main__":

    path_in_dir = "../data/corpus/原始语料"
    path_save_dir = "../data/corpus/分析结果/文本语料"
    transfer_dir_to_txt(path_in_dir, path_save_dir)
    ta = 0

