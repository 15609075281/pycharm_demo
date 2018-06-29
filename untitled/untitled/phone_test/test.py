# coding=utf-8
import json


def get_arr():
    arr_ = []
    for var in range(1, 10):
        data = {
            'name': var,
            'password': var + 2,
        }
        arr_.append(data)
    data1 = {
        'content': "我也不知道成不成功",
        'msg': 200,
        'result': arr_
    }
    print(json.dumps(data1))

if __name__ == '__main__':
    print('开始')
    get_arr()
