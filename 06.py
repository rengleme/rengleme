# 创建垃圾桶和垃圾
# 规则：k:v,一个k对应一个v，代码表示用冒号分割
# 输入
# 判断
# 保存
# 函数


import json

# laji = '菜叶'


# lajitong = "湿垃圾"

ljt_shi = {
    'name': "湿垃圾",
    'data': []
}

ljt_gan = {
    'name': "干垃圾",
    'data': []
}

# 读文件，加载数据
# with open('gan.json') as f:
#     ljt_gan = json.load(f)

# print('加载文件：', ljt_gan)
def load_data(filename):
    with open(filename) as f:
        data = json.load(f)
        return data

ljt_gan = load_data('gan.json')
ljt_shi = load_data('shi.json')

print('加载文件：', ljt_gan, ljt_shi)

rule = {
    "湿垃圾": ["菜叶", "橙皮", "葱", "饼干"],
    "干垃圾": ["旧浴缸", "盆子", "海绵", "卫生纸"]
}

laji = input("输入要扔的垃圾：")
print("垃圾：", laji)


def reng_laji(rule_k, laji, ljt):
    if rule_k == ljt['name']:
        ljt['data'].append(laji)


def fenlei(laji, rule, ljt):
    for k, v in rule.items():
        print(k, v)
        if laji in v:
            print('找到了垃圾：', laji, k)
            reng_laji(k, laji, ljt)
            # reng_laji(k, laji, ljt_shi)
        
fenlei(laji, rule, ljt_gan)
fenlei(laji, rule, ljt_shi)

print('-'*20)
print(ljt_shi)
print(ljt_gan)

# 写文件
# json，交换格式
# with open('gan.json', 'w') as f:
#     json.dump(ljt_gan, f)

# # json，交换格式
# with open('shi.json', 'w') as f:
#     json.dump(ljt_shi, f)

# 用函数封装写文件的代码
def save_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

# 调用函数
save_to_file('gan.json', ljt_gan)
save_to_file('shi.json', ljt_shi)




