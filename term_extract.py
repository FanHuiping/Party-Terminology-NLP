# -*- coding: utf-8 -*-
import jieba 
import jieba.posseg as pseg

# 读取党章文件（文件需与脚本同目录）
with open('dangzhang.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 设置党政术语词典（提升识别准确率）
jieba.load_userdict("dangzhang_dict.txt")  # 手动新建空文件

# 执行术语提取
terms = []
for word, flag in pseg.cut(text):
    # 保留名词(n)和动名词(vn)且长度≥2
    if flag in ['n', 'vn'] and len(word) >= 2:
        terms.append(word)

# 保存结果
with open('dangjian_terms.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(set(terms)))  # 去重后保存

print(f'成功提取{len(terms)}个术语！结果已保存到dangjian_terms.txt')