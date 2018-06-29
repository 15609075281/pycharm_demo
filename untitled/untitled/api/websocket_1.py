# coding=utf-8
from django.shortcuts import render
from dwebsocket.decorators import accept_websocket, require_websocket
from django.http import HttpResponse
from untitled.phone_test import phone2
from untitled.api import api
from untitled.api import re_url
import json


@accept_websocket
def echo(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        try:  # 如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'index.html')
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
