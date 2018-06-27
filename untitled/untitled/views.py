# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from untitled.phone_test import phone2
from untitled.phone_test import phone_home
from untitled.phone_test import python_deatils

'''
输入网址直接获取所有手机号
'''


# 第一版获得手机号
def phone(request):
    if request.method == 'POST':
        url = request.GET.get('url', '1')
        if url == '1':
            return HttpResponse('什么也没有！！！')
        else:
            return HttpResponse(phone2.get_phone(url))
    else:
        return HttpResponse(phone2.get_phone('https://yzt236364.atobo.com.cn/'))


'''
平台选者 0(阿土伯),1(),2
'''


def one(request):
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


def test(request):
    url = request.GET.get('name', '1')
    phone2.get_all_url(url)
    return HttpResponse('1')
