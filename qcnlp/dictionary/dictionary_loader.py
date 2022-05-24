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

def core_nature_dictionary_loader():
    """ 加载分词词典
    """
    dic = set()

    # 按行读取字典文件，每行第一个空格之前的字符串提取出来。
    for line in open(os.path.join(GRAND_DIR_PATH, 'dictionary/CoreNatureDictionary.txt'), "r", encoding="utf8"):
        dic.add(line[0:line.find('	')])

    return dic

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

def negative_words_loader():
    """ 加载否定词典 negative_words.txt """
    negative_words_list = []
    for line in open(os.path.join(
        GRAND_DIR_PATH, 'dictionary/negative_words.txt'), "r", encoding="utf8"):
        negative_words_list.append(line.split('\n')[0])
    return negative_words_list

def sentiment_adv_words_loader():
    """ 加载情感副词词典，并附带其对应的情感权重 sentiment_adv_words.txt """
    sentiment_adv_words_dic = {}
    for line in open(os.path.join(
        GRAND_DIR_PATH, 'dictionary/sentiment_adv_words.txt'), "r", encoding="utf8"):
        key, value = line.split('\t')
        assert len(line.split('\t')) == 2
        sentiment_adv_words_dic.update({key: float(value)})

    return sentiment_adv_words_dic

def sentiment_words_loader():
    """ 加载情感词典，并附带其对应的情感权重 sentiment_words.txt """
    sentiment_words_dic = {}
    for line in open(os.path.join(
        GRAND_DIR_PATH, 'dictionary/sentiment_words.txt'), "r", encoding="utf8"):
        key, value = line.split('\t')
        assert len(line.split('\t')) == 2
        sentiment_words_dic.update({key: float(value)})

    return sentiment_words_dic