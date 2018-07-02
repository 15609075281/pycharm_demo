# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
from untitled.api import api
from untitled.api import re_url
from untitled.api import excls_csv
import time

# 获得手机号码
re_r = '1[3|4|5|7|8]\d{9}'  # 1代表第一个号码为1;;;[3|4|5|7|8]第二位指定为这几个数；；；\d代表0~9，{9}循环9次
arr_data_ = []

# heards = {
#     'Usser-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36',
#     'Cookie': 'SESSION=758cf29f-f90a-45b3-afb1-6c40b3503a79; JSESSIONID=B3795B795249A88CBD0CB60C6D77C046'
# }


# 对地址进行获取
def get_phone(path, url):
    arr_data = []
    url_html = requests.get(url).text
    re_phone = re.findall(re_r, url_html, re.M | re.S | re.I)
    re_phone = set(re_phone)
    if len(re_phone) == 0:
        data_a = {
            'url': url,
            'phone': 'null'
        }
        return data_a
    else:
        for car_phone in re_phone:
            data_a = {
                'url': url,
                'phone': car_phone
            }
            arr_data.append(data_a)
            arr_f = []
            da_f = (url, car_phone)
            arr_f.append(da_f)
            excls_csv.if_file(path, ['url', 'phone'], arr_f)
            return data_a


# 根据一个url获取整个页面上的所有url
def get_all_url(url_):
    arr_one_phone_url = []
    arr_two_phone_url = []
    if re_url.if_url(url_) == '1':
        print('这个是首页地址', url_)
        url_12 = requests.get(url_)
        soup_1 = BeautifulSoup(url_12.text, 'html.parser')
        url_a = soup_1.find_all('a')
        arr_one_phone_url.append(url_)
        for var_url_a in url_a:
            href_url = var_url_a.get('href')
            print(href_url)
            if re_url.if_url(href_url) == '1':
                arr_one_phone_url.append(href_url)
            else:
                print()
            print(len(arr_one_phone_url))
            if len(arr_one_phone_url) == 1000:
                # 跳出去
                break
        for var_two_getPhone in arr_one_phone_url:
            print(arr_one_phone_url.index(var_two_getPhone))
            print(var_two_getPhone)
            lenth_ = get_phone('E:\stest\stest.csv', var_two_getPhone)
            if lenth_['phone'] == 'null':
                print('phone::::没有数据')
            else:
                arr_two_phone_url.append(lenth_)
            print(lenth_)
        print('有效数据:::', len(arr_two_phone_url), '条')
        return api.get_api('唯一数据', 200, arr_two_phone_url)
    else:
        return api.get_api('地址错误', 500, arr_data_)


if __name__ == '__main__':
    # url = 'https://www.atobo.com.cn/'
    str = input('输入链接地址:')
    print('输入地址：', str)
