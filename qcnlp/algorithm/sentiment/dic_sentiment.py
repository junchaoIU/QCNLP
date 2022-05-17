# -*- coding=utf-8 -*-
"""
# library: qcnlp
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/QCNLP
# description: A Preprocessing & Parsing tool for Chinese Natural Language Processing
"""
import math
import re

from enum import Enum, unique

from qcnlp.algorithm.segmation import SentenceSeg
from qcnlp.algorithm.ner import NerSearch
from qcnlp.dictionary.dictionary_loader import negative_words_loader, sentiment_adv_words_loader, sentiment_words_loader


@unique
class Bias(Enum):
    LEFT = 0
    MIDDLE = 0.5
    RIGHT = 1

def sigmoid(x):
    try:
        x = x  # / 10.0  # 为了使结果平滑
        ans = math.exp(-x)
    except OverflowError:
        ans = float('inf')
    return 1 / (1 + ans)


class Item(object):
    def __init__(self, start_idx, end_idx, prev_len, next_len, word):
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.prev_len = prev_len
        self.next_len = next_len
        self.bias = Bias.MIDDLE
        self.word = word

    def set_next_len(self, next_len):
        self.next_len = next_len
        if self.prev_len >= self.next_len and self.next_len < 6:
            self.bias = Bias.RIGHT
        elif self.prev_len < self.next_len and self.prev_len < 6:
            self.bias = Bias.LEFT

    def set_prev_len(self, prev_len):
        self.prev_len = prev_len
        if self.prev_len >= self.next_len and self.next_len < 6:
            self.bias = Bias.RIGHT
        elif self.prev_len < self.next_len and self.prev_len < 6:
            self.bias = Bias.LEFT


class Items(object):
    def __init__(self):
        self.items_list = list()

    def put_note(self, item):
        item_start_idx = item.start_idx
        item_end_idx = item.end_idx
        if len(self.items_list) == 0:
            self.items_list.append(item)
        else:
            tmp_item = self.items_list[-1]
            tmp_item_start_idx = tmp_item.start_idx
            tmp_item_end_idx = tmp_item.end_idx
            if item_start_idx < tmp_item_end_idx and not (item_start_idx > tmp_item_start_idx
                                                          and item_end_idx == tmp_item_end_idx):
                prev_len = tmp_item.prev_len
                if item_end_idx == tmp_item_end_idx:
                    prev_len -= abs(item_start_idx - tmp_item_start_idx)
                item.set_prev_len(prev_len)
                item.set_next_len(20)
                self.items_list[-1] = item

            elif not (item_start_idx > tmp_item_start_idx and item_end_idx == tmp_item_end_idx):
                tmp_len = item_start_idx - tmp_item_end_idx
                item.set_prev_len(tmp_len)
                item.set_next_len(20)
                tmp_item.set_next_len(tmp_len)
                self.items_list[-1] = tmp_item
                self.items_list.append(item)

class DictionarySentiment(object):
    def __init__(self):
        self.negative_words_list = negative_words_loader()
        self.sentiment_adv_words_dic = sentiment_adv_words_loader()
        self.sentiment_words_dic = sentiment_words_loader()
        self.lexicon_ner = NerSearch(
            {'sentiment_word': list(self.sentiment_words_dic.keys()),
             'negative_word': self.negative_words_list,
             'expand_word': list(self.sentiment_adv_words_dic.keys())})

        self.split_sentence = SentenceSeg()
        self.transition_words = re.compile('((，|\,)(但是|可是|但|不过))')

    def get_sentence_sentiment(self, sentence):
        # print(sentence)
        # rule1: 转折词汇，不考虑前面的情感词，仅考虑之后的情感词
        transition_item = self.transition_words.search(sentence)
        if transition_item:
            match_word = transition_item.group()
            sentence_split = sentence.split(match_word)
            if len(sentence_split) > 0:
                sentence = sentence_split[-1]

        items_object = Items()
        for item in self.lexicon_ner(sentence):
            # tmp_end = tmp_end/3
            it_object = Item(item['offset'][0], item['offset'][1],
                             20, 20, item['text'])

            items_object.put_note(it_object)  # 整理每一个情感词汇

        val_list = list()
        sentence_not = 1.0
        sentence_weight = 1.0
        for x in items_object.items_list:

            word = x.word
            bias = x.bias
            next_len = x.next_len
            word_val = 0
            if word in self.sentiment_words_dic:
                word_val = self.sentiment_words_dic.get(word)
                if sentence_weight != 1.0:  # 前有乘子副词，则相乘
                    word_val *= sentence_weight
                if sentence_not != 1.0:  # 前有否定词，则相乘
                    word_val *= sentence_not
                if word_val < 0:
                    word_val *= 2

                val_list.append(word_val)
                sentence_not = 1.0
                sentence_weight = 1.0

            elif word in self.negative_words_list:  # 否定词汇，乘以 -1
                if next_len < 6:
                    sentence_not = -1.0

            elif word in self.sentiment_adv_words_dic:  # 乘子副词，乘以权重
                word_weight = self.sentiment_adv_words_dic.get(word)
                if bias == Bias.LEFT and len(val_list) > 0:
                    val_list_last_val = val_list[-1]
                    val_list_last_val *= word_weight
                    val_list[-1] = val_list_last_val

                elif bias == Bias.RIGHT:
                    sentence_weight = word_weight

        sentence_value = 0
        for x in val_list:
            sentence_value += x

        return sentence_value

    def __call__(self, text: str):
        if not text:
            return 0.5

        sentiment_value = 0.
        sentence_list = self.split_sentence(text)

        for sentence in sentence_list:
            sentence_val = self.get_sentence_sentiment(sentence)
            sentiment_value += sentence_val

        sentiment_value = sentiment_value / len(sentence_list)

        sentiment_value = sigmoid(sentiment_value)
        return sentiment_value

