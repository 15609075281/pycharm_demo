# -*- coding: utf-8 -*-
from django.http import HttpResponse
from untitled.phone_test import phone2
from untitled.phone_test import phone_home
from untitled.phone_test import python_deatils
from untitled.api import api


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
        url = request.GET.get('url', '1')
        print('Get Data:', request.GET)
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
    number = request.GET.get('number')
    if request.method == 'POST':
        print('POST请求')
        return HttpResponse(phone_home.get_html_url())
    else:
        print('GET请求')


def two(request):
    if request.method == 'POST':
        print('POST请求')
        return HttpResponse(python_deatils.get_mysql())
    else:
        print('GET请求')
