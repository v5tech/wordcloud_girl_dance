# -*- coding:utf-8 -*-
# @File : 4_1_弹幕爬取.py

import datetime
import re

import requests
from fake_useragent import UserAgent

# 随机产生请求头
ua = UserAgent(verify_ssl=False, path='fake_useragent.json')
start_time = datetime.datetime.now()


def grab_barrage():
    headers = {
        "origin": "https://www.bilibili.com",
        "referer": "https://www.bilibili.com/video/BV1jZ4y1K78N?from=search&seid=1084505810439035065",
        "cookie": "buvid3=592F6039-5AFE-47E6-992B-44A71830295A138370infoc; rpdid=|(JY)J~ukuYY0J'uY|l)R~RkY; buvid_fp=592F6039-5AFE-47E6-992B-44A71830295A138370infoc; buvid_fp_plain=592F6039-5AFE-47E6-992B-44A71830295A138370infoc; fingerprint3=5f5555085c0912d9be8bea4db90eb2f0; fingerprint_s=e61be3b836d07c887d17aaead3c607a8; CURRENT_QUALITY=80; blackside_state=0; fingerprint=05b944ca121b66bc733ce04590e7dfb5; DedeUserID=108053590; DedeUserID__ckMd5=c2a18dd4087f979e; SESSDATA=14bc4f23,1651211041,df8c0*a1; bili_jct=41e3cb9b9ce3c2882f767675e1f198a0; _uuid=21CDC81C-EFEC-10242-1109E-10A6A10745945F86747infoc; bp_t_offset_108053590=595433662964172320; video_page_version=v_old_home; CURRENT_FNVAL=2000; sid=8ym3b3hd; PVID=1; bsource=search_google; b_lsid=EF35103AE_17DAA28DC1C",
        "user-agent": ua.random,
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    comments = re.findall('<d p=".*?">(.*?)</d>', r.text)
    with open('./barrages.txt', 'w', encoding='utf-8') as f:
        for comment in comments:
            f.write(comment)
            f.write('\n')


if __name__ == '__main__':
    # 目标url
    url = "https://comment.bilibili.com/222413092.xml"
    grab_barrage()
