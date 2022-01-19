"""
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

# 会出现符号处理麻烦的问题
# file_name = "words.txt"
#
# def words_count():
#
#     file = open(file_name, 'r')
#     words = file.read().replace('.', '').replace(':', '').replace(',', '').split()
#
#
#     dic = dict()
#     for word in words:
#         if word not in dic:
#             dic[word] = 1
#         else: dic[word] += 1
#
#     for k, v in dic.items():
#         print(k, v)
#
# def main():
#     words_count()
#
# if __name__ == '__main__':
#     main()


import re
# 匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+
pattern = re.compile("[a-zA-Z]+")
file_name = "words.txt"
result_file = open("result.txt", 'w')
def words_count():
    file = open(file_name, 'r')
    words = pattern.findall(file.read())

    dic = dict()
    for word in words:
        if word.lower() not in dic:
            dic[word.lower()] = 1
        else: dic[word.lower()] += 1

    for k, v in dic.items():
        result_file.write(k+": %d\n"%v)

words_count()

