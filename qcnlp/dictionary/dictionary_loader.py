# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""
import os


DIR_PATH = os.path.dirname(os.path.abspath(__file__))
GRAND_DIR_PATH = os.path.dirname(DIR_PATH)

def stopwords_loader():
    """ 加载停用词典
    中文停用词表	cn_stopwords.txt
    哈工大停用词表	hit_stopwords.txt
    百度停用词表	baidu_stopwords.txt
    四川大学机器智能实验室停用词库	scu_stopwords.txt
    """
    stopwords_list = []
    for line in open(os.path.join(
        GRAND_DIR_PATH, 'dictionary/baidu_stopwords.txt'), "r", encoding="utf8"):
        stopwords_list.append(line.split('\n')[0])
    for line in open(os.path.join(
        GRAND_DIR_PATH, 'dictionary/cn_stopwords.txt'), "r", encoding="utf8"):
        stopwords_list.append(line.split('\n')[0])
    for line in open(os.path.join(
        GRAND_DIR_PATH, 'dictionary/hit_stopwords.txt'), "r", encoding="utf8"):
        stopwords_list.append(line.split('\n')[0])
    for line in open(os.path.join(
        GRAND_DIR_PATH, 'dictionary/scu_stopwords.txt'), "r", encoding="utf8"):
        stopwords_list.append(line.split('\n')[0])

    stopwords_list = list(set(stopwords_list))
    return stopwords_list