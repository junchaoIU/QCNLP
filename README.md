
<p align="center">
    <a alt="jionlp logo">
        <img src="image/QCNLP_LOGO.png" style="width:300px;height:100px">
    </a>
</p>
<p align="center">
    <a alt="License">
        <img src="https://img.shields.io/github/license/junchaoIU/QCNLP?color=crimson" /></a>
    <a alt="Version">
        <img src="https://img.shields.io/badge/version-0.0.1-green" /></a>
    <a href="https://github.com/junchaoIU/QCNLP/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/junchaoIU/QCNLP?color=blue" /></a>
</p>
<p align="center">
<big>A Preprocessing &amp; Parsing tool for Chinese Natural Language Processing</big><br/>
<big>一个预处理与中文自然语言处理解析工具</big>
</p>

## 📦 Quick Start（快速使用）
```shell
# install
pip install qcnlp
```

```shell
# version
import qcnlp as qc
print(qc.__version__)

# 1.1.0
```

## ✨ 方法集合
### 1.分词
| 功能                                          | 函数           | 描述       |
|---------------------------------------------|--------------|----------|
| [**正向最长匹配分词**](../../wiki/分词-说明文档#正向最长匹配分词) | f_seg        | 正向最长匹配分词 |
| [**逆向最长匹配分词**](../../wiki/分词-说明文档#逆向最长匹配分词) | b_seg        | 逆向最长匹配分词 |
| [**双向最长匹配分词**](../../wiki/分词-说明文档#双向最长匹配分词) | l_seg        | 双向最长匹配分词 |
| [**文本句子切分**](../../wiki/分词-说明文档#文本句子切分)   | sentence_seg | 文本句子切分 |

### 2.工具集
| 功能   | 函数    | 描述       |
|--------|-------|----------|
|[**去除停用词**](../../wiki/分词-说明文档#去除停用词) | remove_stopwords | 去除停用词 |

### 3.命名实体识别
| 功能                                               | 函数        | 描述       |
|--------------------------------------------------|-----------|----------|
| [**基于词典的命名实体识别**](../../wiki/命名实体识别-说明文档#基于词典的命名实体识别) | NerSearch | 基于词典的命名实体识别 |

### 4.情感分析
| 功能                                              | 函数    | 描述       |
|-------------------------------------------------|-------|----------|
| [**基于词典的情感分析**](../../wiki/情感分析-说明文档#基于词典的情感分析) | sentiment_dic | 基于词典的情感分析 |

### 5.词嵌入
| 功能                                              | 函数    | 描述       |
|-------------------------------------------------|-------|----------|
| [**词袋训练**](../../wiki/词嵌入-说明文档#词袋训练) | bagvec_model | 词袋训练 |
| [**word2vec词嵌入训练**](../../wiki/词嵌入-说明文档#word2vec词嵌入训练) | word2vec_model | word2vec词嵌入训练 |
| [**bert词嵌入模型获取**](../../wiki/词嵌入-说明文档#bert_vec词嵌入模型获取) | bertvec_model | bert词嵌入模型获取 |

## 🖥 Package Publish
``` shell
python setup.py sdist  
twine upload dist/qcnlp-1.1.0.tar.gz
```

## 🌸 About Author（关于作者）
[WU, JUNCHAO](https://github.com/junchaoIU)

个人博客（Blog）：[春天与爱情の樱花🌸](https://www.wujunchao.top)

如遇到问题，请致邮（Email）：wujunchaoIU@outlook.com
