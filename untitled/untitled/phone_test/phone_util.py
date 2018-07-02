# coding=utf-8
import time
import datetime
import pymongo


# 设置文件生成时间
# platform平台
# st结果名称
def set_data_time(platform, st):
    # time_ = time.localtime(time.time())#time_.tm_hour,小时
    data_day = datetime.date.today()
    folder = 'E:\sc\%s四川%s%s.csv' % (platform, data_day, st)
    return folder


