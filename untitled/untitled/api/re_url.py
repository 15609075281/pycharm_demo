# coding=utf-8
import sys
import re


# Make sure we have a single URL argument.

# if len(sys.argv) != 2:
#     print(sys.stderr, "URL Required")
#     sys.exit(-1)
# # Easie access.
# url = sys.argv[1]
# url = 'https://www.baidu.com'
# url = '哈哈哈哈哈'
# Ensure we were passed a somewhat valid URL.
# This is a superficial test.
# if re.match(r'^https?:/{2}\w.+$', url):
#     print("This looks valid.")
# else:
#     print("This looks invalid.")


def if_url(url):
    if url != None:
        if re_apk(url) == '1':
            if re.match(r'^https?:/{2}\w.+$', url):
                print("This looks valid.")
                return '1'
            else:
                print("This looks invalid.")
                return '2'
        else:
            print('不是网址')
    else:
        print('地址为null', url)
        return '2'


def re_apk(apk_url):
    r = r'.apk'
    s = re.findall(r, apk_url, re.M | re.S | re.I)
    if len(s) == 0:
        return '1'
    else:
        return '2'


if __name__ == '__main__':
    print()
    # url='http://downpack.baidu.com/baidunews_AndroidPhone_1014720b.apk'
    url = 'http://www.baidu.com'
    re_apk(url)
