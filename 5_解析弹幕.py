# -*- coding:utf-8 -*-
# @File : 5_解析弹幕.py

from xml.dom import minidom


def main():
    with open('./无价之姐~让我乘风破浪~~~.cmt.xml', 'r', encoding='utf-8') as f:
        dom = minidom.parse(f)
        # 获取根节点
        root = dom.documentElement
        with open('./barrages.txt', 'w', encoding='utf-8') as fp:
            try:
                for i in range(2000):
                    name = root.getElementsByTagName('d')[i]
                    name_text_node = name.childNodes[0]
                    danmu = name_text_node.data
                    type(danmu)
                    fp.write(danmu)
                    fp.write('\n')
            except:
                print('over!')


if __name__ == '__main__':
    main()
