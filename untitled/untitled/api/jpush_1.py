# ! /usr/bin/env	python2
# encoding=utf-8
import time, random, hashlib, json, requests, urllib, sys, os

# sys.path.insert(0, os.path.dirname(sys.path[0]))
# reload(sys)
# sys.setdefaultencoding('utf8')

import requests

# 苹果的测试环境0,生产环境 v2
apns_production = 1
# 苹果的测试环境0,生产环境 v3
apns_production_boolean = True

# 极光key配置
apps = {
    "app_key": u'0854f04c0ed3c2d211a06b1c',
    "master_secret": u'543b4c4eea6dce3c5adc973e'
}
app_2 = {
    "app_key": u'0854f04c0ed3c2d211a06b1c',
    "master_secret": u'543b4c4eea6dce3c5adc973e'
}


# https request jpush v3


def https_request(app_key, body, url, content_type=None, version=None, params=None):
    https = requests.Session()
    https.auth = (app_key['app_key'], app_key['master_secret'])
    headers = {}
    headers['user-agent'] = 'jpush-api-python-client'
    headers['connection'] = 'keep-alive'
    headers['content-type'] = 'application/json;charset:utf-8'
    # print url,body
    response = https.request('POST', url, data=body, params=params, headers=headers)
    # 合并返回
    return dict(json.loads(response.content), **{'status_code': response.status_code})


# jpush v3 params
# 支持离线消息，在线通知同时发送
def push_params_v3(content, receiver_value=None, n_extras=None, platform="all"):
    global apns_production_boolean
    sendno = int(time.time() + random.randint(10000000, 99999900))
    payload = dict()
    payload['platform'] = platform

    payload['audience'] = {
        "alias": receiver_value
    }
    # 离线消息
    payload['message'] = {
        "msg_content": content,
        "extras": n_extras
    }
    # 在线通知
    payload['notification'] = {
        "android": {"alert": content, "extras": n_extras},
        "ios": {"alert": content, "sound": "default", "extras": n_extras},  # "badge":1,
    }
    payload['options'] = {"apns_production": apns_production_boolean, "time_to_live": 86400 * 3, 'sendno': sendno}

    return payload


# jpush v3 request
def jpush_v3(app_key, payload):
    body = json.dumps(payload)
    # print body
    return https_request(app_key, body, "https://api.jpush.cn/v3/push", 'application/json', version=1)


if __name__ == '__main__':
    print()
    jpush_v3(apps['app_key'], apps['master_secret'])
    # push_params_v3()
