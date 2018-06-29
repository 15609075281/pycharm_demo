# coding=utf-8
import csv
import datetime
import time
import os


# 数据文件存储
# path文件存储地址
# arr_1存储数据种类//格式{列表}
# arr_2存储数据//格式{列表+字典}
def if_file(path, arr_1, arr_2):
    if os.access(path, os.F_OK):
        try:
            with open(path, 'a+', newline='')as file_1:
                path_writer = csv.writer(file_1)
                path_writer.writerows(arr_2)
                file_1.close()
        except IOError as e:
            print("File is not accessible.", e)
    else:
        try:
            with open(path, 'w', newline='')as file_1:
                path_writer = csv.writer(file_1)
                path_writer.writerow(arr_1)
                path_writer.writerows(arr_2)
                file_1.close()
        except IOError as ioe:
            print("File is not accessible.", ioe)


if __name__ == '__main__':
    path = 'E:\stest\stest.csv'
    arr_1 = ['num1', 'num2', 'num3']
    arr_2 = [('111', '1112', '1113'), ('222', '2224', '2225'), ('333', '3336', '3337')]
    # if_file(path, arr_1, arr_2)
    data = {}
    data1 = {'1': 1, '2': 2}
    print(data1['2'])
