# handle_laji.py
# author: DE8UG
# PROJECT: rengleme

def reng_laji(rule_k, laji, ljt):
    if rule_k == ljt['name']:
        ljt['data'].append(laji)


def fenlei(laji, rule, ljt):
    for k, v in rule.items():
        print(k, v)
        if laji in v:
            print('找到了垃圾：', laji, k)
            reng_laji(k, laji, ljt)