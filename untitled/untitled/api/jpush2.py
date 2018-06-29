# -*- coding:utf-8 -*-
import jpush as jpush

# from tests.conf import app_key,master_secret
app_key = u'0854f04c0ed3c2d211a06b1c'
master_secret = u'543b4c4eea6dce3c5adc973e'
_jpush_1 = jpush.JPush(app_key, master_secret)##1、初始化JPush，获取AppKey，Master Secret;实例化JPush，
push = _jpush_1.create_push()
# --------------------------------推送设备对象---------------------------
# 一个推送对象，以 JSON 格式表达，表示一条推送相关的所有信息。
# push.audience=jpush.all_ ;#audience	必填	推送设备指定;确认推送设备对象，JPush 提供了多种方式，比如：别名、标签、注册ID、分群、广播等。
push.audience = jpush.audience(
    jpush.registration_id("18071adc0308b6e0dc2", ),
)
# -----------------------------------------------------------------------
# ----------------------------自定义消息 发给android的实现---------------
push.message = jpush.message(
    "{'salists': [{'payType': 1, 'proid': 3, 'name': '燕麦谷粒多', 'count': 1, 'sinPrice': 2, 'toPrice': 2, 'chid': 162}], 'nums': 1}");  # message	可选	消息内容体。是被推送到客户端的内容。与 notification 一起二者必须有其一，可以二者并存
# ------------------------------------------------------------------------
# --------------------------- 发送通知 给android的实现--------------------
# android = jpush.android(alert={
# "salists": [
# {
# "payType": 1,
# "proid": 3,
# "name": "燕麦谷粒多",
# "count": 1
# }
# ],
# "nums": 1
# }, priority=1, style=2,inbox=2, alert_type=1, extras={'k1':'v1'})#通知栏样式类型:inbox=2，big_text=1,bigPicture=3
# push.notification = jpush.notification(alert="Hello, JPush!", android=android,)#注意notification的alert没起作用，被android中的alert覆盖掉了。
# ------------------------------------------------------------------------
push.platform = jpush.all_  # platform	必填	推送平台设置
push.send()
