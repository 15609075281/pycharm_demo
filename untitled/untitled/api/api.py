# coding=utf-8
import json


# 返回固定格式
# content::返回没有数据的提示语
# msg::返回码
# arr_::数组+object(字典)
def get_api(content, msg, arr_):
    print()
    data1 = {
        'content': content,
        'msg': msg,
        'result': arr_
    }
    # return "(" + json.dumps(data1, indent=2, ensure_ascii=False).encode() + ");"
    return json.dumps(data1, ensure_ascii=False).encode()


def get_api1(content, msg, arr_):
    print()
    data1 = {
        'content': content,
        'msg': msg,
        'result': arr_
    }
    return "(" + json.dumps(data1, indent=2, ensure_ascii=False).encode() + ");"
