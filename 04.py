# 创建垃圾桶和垃圾
# 规则：k:v,一个k对应一个v，代码表示用冒号分割
# 输入
# 判断

# laji = '菜叶'
laji = input("输入要扔的垃圾：")
print("垃圾：", laji)


# lajitong = "湿垃圾"

ljt_shi = {
    'name': "湿垃圾",
    'data': []
}

rule = {
    "湿垃圾": ["菜叶", "橙皮", "葱", "饼干"],
    "干垃圾": ["旧浴缸", "盆子", "海绵", "卫生纸"]
}

for k, v in rule.items():
    print(k, v)
    if laji in v:
        print('找到了垃圾：', laji, k)


# ljt_shi['data'].append(laji)

# print(ljt_shi)

