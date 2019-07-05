# 创建垃圾桶和垃圾
# 规则：k:v,一个k对应一个v，代码表示用冒号分割
# 输入
# 判断
# 保存


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
with open('gan.json') as f:
    ljt_gan = json.load(f)

print('加载文件：', ljt_gan)

rule = {
    "湿垃圾": ["菜叶", "橙皮", "葱", "饼干"],
    "干垃圾": ["旧浴缸", "盆子", "海绵", "卫生纸"]
}

laji = input("输入要扔的垃圾：")
print("垃圾：", laji)


for k, v in rule.items():
    print(k, v)
    if laji in v:
        print('找到了垃圾：', laji, k)
        if k == '湿垃圾':
            ljt_shi['data'].append(laji)
        if k == '干垃圾':
            ljt_gan['data'].append(laji)


print('-'*20)
print(ljt_shi)
print(ljt_gan)

# 写文件
# json，交换格式
with open('gan.json', 'w') as f:
    json.dump(ljt_gan, f)




