import random
import re

import requests

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 ' \
     'Safari/537.36 '


def get_op(tid):
    url = 'https://www.v2ex.com/amp/t/' + tid
    r = requests.get(url, headers={'User-Agent': UA})
    return re.findall(r'alt=\"(.+?)\"', r.text)[0]


def get_user_list(url):
    r = requests.get(url, headers={'User-Agent': UA})
    return re.findall(r'alt=\"(.+?)\"', r.text)[2:]


def get_all_pages(tid):
    url = 'https://www.v2ex.com/amp/t/' + tid
    r = requests.get(url, headers={'User-Agent': UA})
    r.encoding = 'utf-8'
    page_num = re.findall(r'共 (\d+) 页', r.text)[-1]
    pages = [url]
    for i in range(2, int(page_num) + 1):
        pages.append(url + '/' + str(i))
    return pages


def get_all_user(tid):
    pages = get_all_pages(tid)
    user_list = []
    for page in pages:
        user_list += get_user_list(page)
    return user_list


def get_xmr_info():
    r = requests.get('https://xmrchain.net', headers={'User-Agent': UA})
    return re.findall(r'Server time: (.+?)\|', r.text)[0], int(re.findall(r'as of (\d+) block', r.text)[0])


if __name__ == '__main__':
    tid = input('请输入帖子ID: ').strip()
    num = int(input('请输入抽奖人数: ').strip())
    op = get_op(tid)
    unique_user_list = list(set(get_all_user(tid)) - {op})
    print('符合条件的用户共有 %d 人' % len(unique_user_list))
    server_time, height = get_xmr_info()
    random.seed(height)
    random.shuffle(unique_user_list)
    print('当前时间: ' + server_time)
    print('当前区块高度: ' + str(height))
    print('抽奖结果: ')
    for i in range(num):
        print(unique_user_list[i])
