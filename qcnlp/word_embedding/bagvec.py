# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""

#导入需要的包
import pandas as pd
import csv
import os
from sklearn import feature_extraction
from tqdm import tqdm

import qcnlp
from qcnlp import stopwords_loader

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
GRAND_DIR_PATH = os.path.dirname(DIR_PATH)

class BagvecModel():
    def __init__(self):
        self.vectorizer = None
        self.stopwords_list = stopwords_loader()

    def __call__(self,data_path):

        self.vectorizer = feature_extraction.text.TfidfVectorizer(max_features=10000, ngram_range=(1,2))
        sentence = pd.read_csv(data_path, header=None, quoting=csv.QUOTE_NONE, delimiter="\n")  # 读取文件，记住取名不要用中文
        data = sentence[0].tolist()  # 转换为列表格式

        stop_words = self.stopwords_list

        data_cut = []
        print("=" * 10 + "begin to spilt the sentence" + "=" * 10)

        for line in tqdm(data):
            data_cut.append(" ".join(qcnlp.b_seg(line)))
        # data_cut = [" ".join(qcnlp.b_seg(line)) for line in data]

        print("=" * 10 + "sentence seg finished" + "=" * 10)

        corpus = data_cut
        self.vectorizer.fit(corpus)

        return self.vectorizer