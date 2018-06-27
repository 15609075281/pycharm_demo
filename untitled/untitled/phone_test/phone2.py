# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
from untitled.phone_test import phone_util

# 获得手机号码
re_r = '1[3|4|5|7|8]\d{9}'  # 1代表第一个号码为1;;;[3|4|5|7|8]第二位指定为这几个数；；；\d代表0~9，{9}循环9次
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')


def contain_zh(word):
    '''
    判断传入字符串是否包含中文
    :param word: 待判断字符串
    :return: True:包含中文  False:不包含中文
    '''
    # word = word.decode()
    global zh_pattern
    match = zh_pattern.search(word)
    return match


# url 判断
def is_get_url(url):
    print('url 判断')
    if contain_zh(url):
        return '输入不合法'
    else:
        return get_all_url(url)


# 对地址进行获取
def get_phone(url):
    arr_data = []
    url_html = requests.get(url).text
    re_phone = re.findall(re_r, url_html, re.M | re.S | re.I)
    re_phone = set(re_phone)
    if len(re_phone) == 0:
        print('占时没有数据')
    else:
        for car_phone in re_phone:
            # data_a = (
            #     car_phone
            # )
            # arr_data.append(data_a)
            print(car_phone)
            return car_phone
        # print(phone_util.set_data_time('phone'), arr_data)


def get_all_url(url_):
    arr_phone_url = []
    arr_phone_ = []
    print('-----------------------------------------------------------------------------')
    print(url_)
    print('-----------------------------------------------------------------------------')
    url_12 = requests.get(url_)
    soup_1 = BeautifulSoup(url_12.text, 'html.parser')
    url_a = soup_1.find_all('a')
    arr_phone_url.append(url_)
    for var_url_a in url_a:
        arr_phone_url.append(var_url_a.get('href'))
        print(len(arr_phone_url))
        if len(arr_phone_url) == 20:
            break
    # print(arr_phone_url)
    for var_url_ in arr_phone_url:
        arr_phone_.append(get_phone(var_url_))
    return arr_phone_


if __name__ == '__main__':
    print()
    # url = 'https://www.atobo.com.cn/'
    str = input('输入链接地址:')
    print('输入地址：', str)
    print(is_get_url(str))
