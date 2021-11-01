# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/5/27 21:18
# @author  : Mo
# @function: 统计


from text_analysis.utils.text_common import txt_read, txt_write, load_json, save_json, get_all_dirs_files
from text_analysis.conf.path_log import logger
from collections import Counter
from typing import List, Dict
import json
import os
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from pylab import mpl


def counter_length_label(path_file, dir_save, show: str="bar"):
    """
    统计文本长度-类别数
    :param path_file: str
    :param path_save: str
    :return: 
    """

    files = get_all_dirs_files(path_file)
    files = [file for file in files if file.endswith(".json")]
    tc_data_dev = []
    for f in files:
        tc_data_dev += txt_read(f)
    # 文本长度与类别数
    lengths_question = []
    label_total = []
    for tdd in tc_data_dev:
        tdd_json = json.loads(tdd)
        question = tdd_json.get("text", "")
        label = tdd_json.get("label")
        lengths_question.append(len(question))
        if type(label) == list:
            label_total += label
        else:
            label_total.append(label)
    # 统计
    lengths_dict = dict(Counter(lengths_question))
    label_dict = dict(Counter(label_total))
    # 排序
    lengths_dict_sort = sorted(lengths_dict.items(), key=lambda x: x[0], reverse=False)
    label_dict_sort = sorted(label_dict.items(), key=lambda x: x[1], reverse=True)
    logger.info("length of text is {}".format(lengths_dict_sort))
    logger.info("freq of label is {}".format(label_dict_sort))
    # 长度覆盖
    lengths_question.sort()
    len_ques = len(lengths_question)
    len_99 = lengths_question[int(0.99 * len_ques)]
    len_98 = lengths_question[int(0.98 * len_ques)]
    len_95 = lengths_question[int(0.95 * len_ques)]
    len_90 = lengths_question[int(0.90 * len_ques)]
    logger.info("99% length of text is {}".format(len_99))
    logger.info("98% length of text is {}".format(len_98))
    logger.info("95% length of text is {}".format(len_95))
    logger.info("90% length of text is {}".format(len_90))
    length_dict = {"len_99": len_99,
                   "len_98": len_98,
                   "len_95": len_95,
                   "len_90": len_90
                   }
    # 文本长度length/字典
    save_json(length_dict, os.path.join(dir_save, "length.json"))
    # 文本长度length/展示
    draw_picture(lengths_dict_sort, os.path.join(dir_save, "length.png"), show="plot")
    # 类别数label/展示
    draw_picture(label_dict_sort, os.path.join(dir_save, "label.png"), show)
    # 箱型图length/展示
    draw_box([lengths_question], os.path.join(dir_save, "{}_boxplot.png".format("length")))


def show_chinese(xs: List, ys: List, file: str=None, show: str="bar"):
    """
    画折线图,支持中文
    :param xs: list
    :param ys: list
    :param dir: str
    :return: draw picture
    """
    mpl.rcParams["font.sans-serif"] = ["SimHei"]
    xis = [i for i in range(len(xs))]

    if len(ys) >= 32:
        plt.xscale('symlog')
        plt.yscale('symlog')
    plt.subplots_adjust(bottom=0.2)
    # plt.figure(dpi=64)

    # elif len(ys) >= 128:
    #     plt.xscale('log')
    #     plt.yscale('log')

    # plt.yticks(xis, ys, size='small', fontsize=13)
    if show=="plot":  # 绘制折线图
        # fig, ax = plt.subplots(1, 1)
        # ax.xaxis.set_major_locator(ticker.MultipleLocator(64))
        # plt.figure(dpi=256)
        # from matplotlib.font_manager import FontProperties
        # font = FontProperties(fname="C:\Windows\Fonts\simkai.ttf", size=16)
        # fontproperites = font
        # fontdict={"fontname":"C:\Windows\Fonts\simkai.ttf"}
        # plt.xlabel(xs, fontproperites = font)

        plt.xticks(xis, ys, size='small', rotation=64, fontsize=13)
        plt.plot(xis, xs, 'o-', label=u"线条")  # 画图
    elif show=="pie": # 绘制扇形图
        # plt.figure(dpi=256)
        plt.xticks(xis, xs, size='small', rotation=64, fontsize=13)
        plt.pie(xs, labels=ys, autopct='%1.1f%%', shadow=False, startangle=150)
    else:  # 绘制并列柱状图
        # 创建画布
        # fig, ax = plt.subplots(1, 1)
        # ax.xaxis.set_major_locator(ticker.MultipleLocator(max(int(len(xs)/16), 128)))
        # plt.figure(dpi=128)
        # plt.figure(dpi=256)
        plt.xticks(xis, ys, size='small', rotation=64, fontsize=13)
        plt.bar(xis, xs, 0.8)
        # plt.figure(figsize=(min(512, len(xs)), min(256, int(len(xs)/2))), dpi=32)
        # plt.figure(dpi=128)
        # plt.yticks(xis, ys, size='small', fontsize=13)
        # plt.barh(xis, xs, 0.8)
    if file:  # 保存图片, save要在plt之前才行
        plt.savefig(file)
    else:     # 没有指定则默认一个
        plt.savefig("fig.png")
    # plt.show()
    plt.close()


def draw_picture(xy_list_tuple, path, show: str="bar"):
    """
    文本长度-类别(展示-保存)
    :param xy_list_tuple: List[tuple]
    :param path: str
    :return: 
    """
    length_x = []
    length_y = []
    for k, v in xy_list_tuple:
        length_x.append(k)
        length_y.append(v)
    show_chinese(length_y, length_x, path, show)


def draw_box(boxs: List, file: str=None):
    """
        箱线图、箱型图 boxplot() 
    :param boxs: list
    :param file: str
    :return: 
    """
    mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 中文
    plt.figure(figsize=(10, 5))  # 设置画布的尺寸
    plt.title("boxplot-length", fontsize=20)  # 标题，并设定字号大小
    # notch：是否是凹口的形式展现箱线图；sym：异常点的形状；
    plt.boxplot(boxs, notch=True, sym="*", vert=False, showmeans=True, patch_artist=True)
                # boxprops={'color':'orangered', 'facecolor':'gray'})  # 颜色
    if file:  # 保存图片, save要在plt之前才行
        plt.savefig(file)
    else:     # 没有指定则默认一个
        plt.savefig("boxplot.png")
    # plt.show()  # 显示图像
    plt.close()




if __name__ == '__main__':

    path_in_dir = "../data/corpus/classify"
    path_save_dir = "../data/corpus/classify/分析结果"
    if path_save_dir is None:
        path_save_dir = os.path.join(os.path.dirname(path_in_dir), "分析结果")
    if path_save_dir:
        if not os.path.exists(path_save_dir):
            os.mkdir(path_save_dir)
    counter_length_label(path_in_dir, path_save_dir, show="bar")

    # show_x = [i for i in range(32)]
    # show_y = [str("你是谁") for i in range(32)]
    # show_chinese(show_x, show_y, file="xy1.png")
    # show_chinese(show_x, show_y, file="xy2.png", show="pie")
    # show_chinese(show_x, show_y, file="xy3.png", show="plot")

