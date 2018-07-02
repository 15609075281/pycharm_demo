# -*- coding: utf-8 -*-
from django.http import HttpResponse
from untitled.phone_test import phone2
from untitled.phone_test import phone_home
from untitled.phone_test import python_deatils
from untitled.api import api
import json


# 输入网址直接获取所有手机号
# 第一版获得手机号
def phone(request):
    if request.method == 'POST':
        url = request.GET.get('url', '1')
        print('Get Data:', request.GET)
        callback_func = ''
        print(callback_func)
        if url == '1':
            data = []
            print(api.get_api('什么也没有', 500, data))
            return HttpResponse(callback_func + api.get_api('什么也没有', 500, data))
        else:
            return HttpResponse(callback_func + phone2.get_all_url(url))
    else:
        print('Get Data:', request.GET)
        url = request.GET.get('url', '1')
        callback_func = request.GET.get('callback')
        print(callback_func)
        if url == '1':
            data = []
            print(api.get_api('什么也没有', 500, data))
            return HttpResponse(callback_func + api.get_api('什么也没有', 500, data))
        else:
            return HttpResponse(callback_func + phone2.get_all_url(url))


# 平台选者 0(阿土伯),1(),2
def one(request):
    print('Get Data:', request.GET)
    if request.method == 'POST':
        print('POST请求')
        number = request.GET.get('number')
        if number == 0:
            print('阿土伯')
        elif number == 1:
            print('第二平台')
        elif number == 2:
            print('第二平台第三平台')
        else:
            print('其他平台')
    else:
        print('GET请求')
        # jsonp
        callback = request.GET.get('callback')
        number = request.GET.get('number')
        if number == 0:
            print('阿土伯')
        elif number == 1:
            print('第二平台')
        elif number == 2:
            print('第二平台第三平台')
        else:
            print('其他平台')


# 获取标签
def get_tag(request):
    print('返回标签')
    print('GET DATE:', request.GET)

    callback = request.GET.get('callback')
    data_0 = {'label': '阿土伯', 'value': 0}
    data_1 = {'label': '第二平台', 'value': 1}
    data_2 = {'label': '第三平台', 'value': 2}
    data_3 = {'label': '其他', 'value': 3}
    arr = []
    arr.append(data_0)
    arr.append(data_1)
    arr.append(data_2)
    arr.append(data_3)
    print(arr)
    return HttpResponse(callback + api.get_api_ordinary('标签', 200, arr))


def get_points(request):
    print('获取平台编号')
    number = request.GET.get('number')


def two(request):
    if request.method == 'POST':
        print('POST请求')
        return HttpResponse(python_deatils.get_mysql())
    else:
        print('GET请求')
