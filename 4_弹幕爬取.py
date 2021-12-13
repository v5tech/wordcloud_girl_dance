# -*- coding:utf-8 -*-
# @File : 4_弹幕爬取.py

import datetime
import re
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False, path='fake_useragent.json')
start_time = datetime.datetime.now()


def grab_barrage(date):
    headers = {
        "origin": "https://www.bilibili.com",
        "referer": "https://www.bilibili.com/video/BV1jZ4y1K78N?from=search&seid=1084505810439035065",
        "cookie": "",
        "user-agent": ua.random,
    }
    params = {
        'type': 1,
        'oid': "222413092",
        'date': date
    }
    r = requests.get(url, params=params, headers=headers)
    r.encoding = 'utf-8'
    comments = re.findall('<d p=".*?">(.*?)</d>', r.text)
    df = []
    for i in comments:
        df.append(i)
    a = pd.DataFrame(df)
    a.to_excel("./danmu.xlsx")


def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(grab_barrage, date_list)
    """计算所需时间"""
    delta = (datetime.datetime.now() - start_time).total_seconds()
    print(f'用时：{delta}s')


if __name__ == '__main__':
    # 目标url
    url = "https://api.bilibili.com/x/v2/dm/history"
    start, end = '20200808', '20200908'
    date_list = [x for x in pd.date_range(start, end).strftime('%Y-%m-%d')]
    main()
