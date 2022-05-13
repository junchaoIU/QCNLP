
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

**<big>QCNLP: Preprocessing &amp; Parsing tool for Chinese Natural Language Processing (一个预处理与中文自然语言处理解析工具)</big>**

## 📦 Quick Start（快速使用）
```shell
# install
pip install qcnlp
```

```shell
# version
import qcnlp as qc
print(qc.__version__)
```

## ✨ 方法集合
### 1.分词
| 功能   | 函数    | 描述       |
|--------|-------|----------|
|[**正向最长匹配分词**](../../wiki/分词-说明文档#正向最长匹配分词) | f_seg | 正向最长匹配分词 |
|[**逆向最长匹配分词**](../../wiki/分词-说明文档#逆向最长匹配分词) | b_seg | 逆向最长匹配分词 |
|[**双向最长匹配分词**](../../wiki/分词-说明文档#双向最长匹配分词) | l_seg | 双向最长匹配分词 |

### 2.工具集
| 功能   | 函数    | 描述       |
|--------|-------|----------|
|[**去除停用词**](../../wiki/分词-说明文档#去除停用词) | remove_stopwords | 去除停用词 |


## 🖥 Package Publish
``` shell
python setup.py sdist  
twine upload dist/qcnlp-0.0.1.tar.gz
```

## 🌸 About Author（关于作者）
[WU, JUNCHAO](https://github.com/junchaoIU)

个人博客（Blog）：[春天与爱情の樱花🌸](https://www.wujunchao.top)

如遇到问题，请致邮（Email）：wujunchaoIU@outlook.com