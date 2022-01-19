
"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""


import string
import random

Total_Choices = string.digits + string.ascii_letters

def single_key(len):
    key = ""
    for i in range(0, len):
        key = key + str(random.choice(Total_Choices))
    return key

def generate_keys(num, len):

    keys = []
    for i in range(0, num):
        key = single_key(len)
        if key not in keys:
            keys.append(key)
        else: i -= 1

    save_file = open('001.txt', 'w')
    for key in keys:
        save_file.write(key + '\n')



def main():
    generate_keys(200, 10)

if __name__ == "__main__":
    main()