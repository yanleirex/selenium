# -*- coding:utf-8 -*-
# Created by yanlei on 16-8-13

from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get(
    "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&sf=1&"
    "fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%8B%97%E7%8B%97"
    "&f=3&oq=gou&rsp=2")
html = browser.page_source
print html

browser.close()
