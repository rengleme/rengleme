# handle_file.py
# author: DE8UG
# PROJECT: rengleme

import json


# print('加载文件：', ljt_gan)
def load_data(filename):
    with open(filename) as f:
        data = json.load(f)
        return data


# 用函数封装写文件的代码
def save_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)