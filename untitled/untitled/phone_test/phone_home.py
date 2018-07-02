# coding=utf-8

import csv
import os
import time
import requests
from bs4 import BeautifulSoup
from untitled.phone_test import pymysql1
from untitled.api import excls_csv
from untitled.phone_test import phone_util
from untitled.api import api
from untitled.phone_test import python_deatils

# 首页获取地址
one_url = ['https://www.atobo.com.cn/Companys/s-p26-y{}/'.format(str(i)) for i in range(2, 4)]
one_url1 = ['https://www.atobo.com.cn/Companys/s-p26-s568-y{}/'.format(str(i)) for i in range(2, 100)]
# 所有列表
one_title_url = '#setcolor_area > div.product_contextlist.bplist > ul > li'
# 所有列表href
one_href_url = ' div > ul > li.p_name > div > ul > li.pp_name > a.CompanyName'


# 获取（阿土伯）首页所有地址
def get_html_url():
    arr_page = ['page', 'http']
    arr_ = []
    for var_url in one_url:
        arr_1 = []
        time.sleep(5)
        page = one_url.index(var_url) + 2
        url_html = requests.get(var_url)
        soup = BeautifulSoup(url_html.text, 'html.parser')
        for var_one in soup.select(one_title_url):
            one_href = var_one.select(one_href_url)
            for two_url in one_href:
                url_url = two_url.get('href')
                home_url = 'https:%s' % url_url
                data_ = (str(page), home_url)
                data_1 = {'page': str(page), 'address': home_url}
                # 存入本地表格
                arr_1.append(data_)
                excls_csv.if_file(phone_util.set_data_time('阿土伯', '初始网址'), arr_page, arr_1)
                arr_.append(data_1)
    print('所有页的数据', arr_)
    print('一共有', len(arr_), '条数据')
    arr_there = []
    for var_all in arr_:
        print(var_all['address'])
        time.sleep(5)
        data_tto = python_deatils.get_name_phone(var_all['address'])
        if data_tto != None:
            arr_there.append(data_tto)
    print('总的所有数据:::', arr_there)
    return api.get_api('存活下来的数据', 200, arr_there)


if __name__ == '__main__':
    print('开始运行！！！')
    # get_phone('https://hyb8816.atobo.com.cn/')
    url = 'https://hyb8816.atobo.com.cn/'
    get_html_url()
