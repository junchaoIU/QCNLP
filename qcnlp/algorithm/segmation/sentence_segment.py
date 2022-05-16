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
import re
import pdb


class SentenceSeg(object):
    """ 分句，将文本切分为若干句子
    Args:
        text(str): 字符串文本
        criterion(coarse/fine): 句子切分粒度，粗细两种 `coarse` 或 `fine`，
            `coarse` 指的是按句号级别切分，`fine` 指按所有标点符合切分，
            默认按照粗粒度进行切分
    Returns:
        list(str): 分句后的句子列表
    """

    def __init__(self):
        self.puncs_fine = None

    def _prepare(self):
        self.puncs_fine = ['……', '\r\n', '，', '。', ';', '；', '…', '！',
                           '!', '?', '？', '\r', '\n', '“', '”', '‘', '’',
                           '：']
        self.puncs_coarse = ['。', '！', '？', '\n', '“', '”', '‘', '’']
        self.front_quote_list = ['“', '‘']
        self.back_quote_list = ['”', '’']

        self.puncs_coarse_ptn = re.compile('([。“”！？\n])')
        self.puncs_fine_ptn = re.compile('([，：。;“”；…！!?？\r\n])')

    def __call__(self, text, criterion='coarse'):

        if self.puncs_fine is None:
            self._prepare()

        if criterion == 'coarse':
            tmp_list = self.puncs_coarse_ptn.split(text)
        elif criterion == 'fine':
            tmp_list = self.puncs_fine_ptn.split(text)
        else:
            raise ValueError('The parameter `criterion` must be '
                             '`coarse` or `fine`.')

        final_sentences = list()
        cur_flag = 0
        quote_flag = False

        for idx, sen in enumerate(tmp_list):
            if sen == '':
                continue
            if criterion == 'coarse':
                if sen in self.puncs_coarse:
                    if len(final_sentences) == 0:  # 即文本起始字符是标点
                        if sen in self.front_quote_list:  # 起始字符是前引号
                            quote_flag = True
                        final_sentences.append(sen)
                        continue

                    # 以下确保当前标点前必然有文本且非空字符串
                    # 前引号较为特殊，其后的一句需要与前引号合并，而不与其前一句合并
                    if sen in self.front_quote_list:
                        if final_sentences[-1][-1] in self.puncs_coarse:
                            # 前引号前有标点如句号，引号等：另起一句，与此合并
                            final_sentences.append(sen)
                        else:
                            # 前引号之前无任何终止标点，与前一句合并
                            final_sentences[-1] = ''.join(
                                [final_sentences[-1], sen])
                        quote_flag = True
                    else:  # 普通,非前引号，则与前一句合并
                        final_sentences[-1] = ''.join(
                            [final_sentences[-1], sen])
                    continue

            elif criterion == 'fine':
                if sen in self.puncs_fine:
                    if len(final_sentences) == 0:  # 即文本起始字符是标点
                        if sen in self.front_quote_list:  # 起始字符是前引号
                            quote_flag = True
                        final_sentences.append(sen)
                        continue

                    # 以下确保当前标点前必然有文本且非空字符串
                    # 前引号较为特殊，其后的一句需要与前引号合并，而不与其前一句合并
                    if sen in self.front_quote_list:
                        if final_sentences[-1][-1] in self.puncs_fine:
                            # 前引号前有标点如句号，引号等：另起一句，与此合并
                            final_sentences.append(sen)
                        else:
                            # 前引号之前无任何终止标点，与前一句合并
                            final_sentences[-1] = ''.join(
                                [final_sentences[-1], sen])
                        quote_flag = True
                    else:  # 普通,非前引号，则与前一句合并
                        final_sentences[-1] = ''.join(
                            [final_sentences[-1], sen])
                    continue

            if len(final_sentences) == 0:  # 起始句且非标点
                final_sentences.append(sen)
                continue

            if quote_flag:  # 当前句子之前有前引号，须与前引号合并
                final_sentences[-1] = ''.join([final_sentences[-1], sen])
                quote_flag = False
            else:
                if final_sentences[-1][-1] in self.back_quote_list:
                    # 此句之前是后引号，需要考察有无其他终止符，用来判断是否和前句合并
                    if len(final_sentences[-1]) <= 1:
                        # 前句仅一个字符。后引号，则合并
                        final_sentences[-1] = ''.join([final_sentences[-1], sen])
                    else:  # 前句有多个字符，
                        if criterion == 'fine':
                            if final_sentences[-1][-2] in self.puncs_fine:
                                # 有逗号等，则需要另起一句，该判断不合语文规范，但须考虑此情况
                                final_sentences.append(sen)
                            else:  # 前句无句号，则需要与前句合并
                                final_sentences[-1] = ''.join([final_sentences[-1], sen])

                        elif criterion == 'coarse':
                            if final_sentences[-1][-2] in self.puncs_coarse:
                                # 有句号，则需要另起一句
                                final_sentences.append(sen)
                            else:  # 前句无句号，则需要与前句合并
                                final_sentences[-1] = ''.join([final_sentences[-1], sen])
                else:
                    final_sentences.append(sen)

        return final_sentences
