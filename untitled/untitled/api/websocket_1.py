# coding=utf-8
from django.shortcuts import render
from dwebsocket.decorators import accept_websocket, require_websocket
from django.http import HttpResponse
from untitled.phone_test import phone2
from untitled.api import api
from untitled.api import re_url
import json
import time
from untitled.phone_test import phone_home


@accept_websocket
def echo(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        print('普通的http请求')
    else:
        print('连接，连接，连接，连接，连接')
        for message in request.websocket:
            url = message.decode('utf-8')  # 解码
            if re_url.if_url(url) == '2':
                data = []
                print(api.get_api('什么也没有', 500, data))
                api.get_api('什么也没有', 500, data)
                request.websocket.send(url)
            else:
                xx_xl = phone2.get_all_url(url)
                print(xx_xl)
                request.websocket.send(xx_xl)  # 发送消息到客户端


# 平台获取数据
@accept_websocket
def get_platform(request):
    print('平台通信连接')
    if not request.is_websocket():
        print('普通http请求')
    else:
        print('连接，连接')
        for message in request.websocket:
            number = message.decode('utf-8')  # 解码
            print('平台序号：：：：', number)
            if number == '0':
                print('阿土伯')
                request.websocket.send(phone_home.get_html_url())
            elif number == 1:
                print('第二平台')
            elif number == 2:
                print('第二平台第三平台')
            elif number == 3:
                print('其他平台')


def get_time(request):
    print('定时发送')
    for message in request.websocket:
        for var_ in range(1, 100):
            time.sleep(3)
            print(var_)
            request.websocket.send(message)  # 发送消息到客户端
