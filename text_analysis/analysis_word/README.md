# analysis-word 词语分析

# 介绍
analysis_word可用于无监督分析多文件语料(HTML/PDF/DOCX/DOC/TXT/MD), 支持docx高亮抽取-读写、新词发现、中文分词、TFIDF、词向量、词语聚类、句子聚类等功能。 

# 详情
各个文件(夹)详情
 - keywords/keywords_common.txt        通用词, 可自己加, 用于高亮成其他颜色
 - keywords/keywords_field.txt         已有领域词, 可自己加, 用于高亮成其他颜色
 - keywords/keywords_newword.txt       新词发现, 自动生成, 用于高亮成其他颜色
 - w00_transfer_file_to_txt.py         将目录下文件(支持HTML/PDF/DOCX/DOC/TXT/MD)提取为TXT文件
 - w01_find_newword_txt.py             新词发现, 生成每个文件对应的"xlsx"文件、和一个汇总的xlsx文件, 存储到"新词发现"目录
 - w02_cut_word_to_txt.py              中文分词, 生成每个文件对应的".切词.txt"文件、和一个汇总的"汇总大文本.md"文件, 存储到"中文分词"目录
 - w03_transfer_to_doc.py              中文分词docx, 生成每个文件对应的".切词.docx"文件, 方便高亮和查看, 存储到"中文分词docx"目录
 - w04_tfidf_xlsx.py                   TFIDF, 生成"汇总TFIDF.xlsx"文件, 包括tf/idf/tf-idf等列, 存储到"TFIDF"目录
 - w05_train_w2v.py                    词向量, 训练w2v词向量, 生成"w2v.vec"文件, 存储到"词向量"目录
 - w06_cluster_w2v.py                  词语聚类, w2v词向量作为距离, 支持K-MEANS/DBSCAN算法, 生成"xlsx"文件, 存储到"词语聚类"目录
 - w07_cluster_sen.py                  句子聚类, w2v词向量/TFIDF作为距离, 支持K-MEANS/DBSCAN算法, 生成"xlsx"文件, 存储到"句子聚类"目录
 - w08_extract_highligt_doc.py         抽取高亮, 抽取原docx文件中标注的高亮词语/句子等, 生成"汇总高亮文本.md"文件, 存储到"高亮语料"目录
 - w100_main.py                        主函数
 - word_discovery.py                   新词发现代码
 
# 快速使用
```python3
python w100_main.py
```

# 使用方式
## 简单样例
```python3
1. 必选, 配置文件所在目录, 
 - 1.1 可以选择在text_analysis/word_analysis/w100_main.py文件中配置地址, 包括 原始语料文件目录(需要存在文件) 和 分析结果文件目录 
 - 1.2 也可以将文件(支持HTML/PDF/DOCX/DOC/TXT/MD)置于目录text_analysis/data/corpus/原始语料下
 - 1.1、1.2任选一种方式就好

2. 可选, 配置通用词/专业词等
 - keywords/keywords_common.txt        通用词, 可自己加, 用于高亮成其他颜色
 - keywords/keywords_field.txt         已有领域词, 可自己加, 用于高亮成其他颜色

3. 必选, 运行主函数, 例如  python w100_main.py
```


# 参考
This library is inspired by and references following frameworks and papers.

* python-docx: [https://github.com/python-openxml/python-docx](https://github.com/python-openxml/python-docx)
* pdfminer.six: [https://github.com/pdfminer/pdfminer.six](https://github.com/pdfminer/pdfminer.six)
* scikit-learn: [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
* tqdm: [https://github.com/tqdm/tqdm](https://github.com/tqdm/tqdm)


# Reference
For citing this work, you can refer to the present GitHub project. For example, with BibTeX:
```
@software{Text-Analysis,
    url = {https://github.com/yongzhuo/Text-Analysis},
    author = {Yongzhuo Mo},
    title = {Text-Analysis},
    year = {2021}

```

希望对你有所帮助!

