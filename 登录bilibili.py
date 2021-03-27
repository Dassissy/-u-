# -*- coding: utf-8 -*-
"""
登录
"""
from selenium import webdriver
import re,os

driver_dict = {'1':'chromes','2':'gecko'}#字典方便拓展
d = input('''1.Chrome
2.Firefox
选择：''')
d = driver_dict[d]

for path in os.listdir(r"G://好东西//py//插件//webdriver//" + d):
    try:
        if d == 'chromes':#对chrome执行版本判定
            driver = webdriver.Chrome("G://好东西//py//插件//webdriver//" + d + "//" + path)
            break
        elif d == 'gecko':#火狐不需要判定版本，但路径前要加'executable_path='
            driver = webdriver.Firefox(executable_path="G:\好东西\py\插件\webdriver\gecko\geckodriver.exe")
            break
    except:
        continue

url = "https://www.bilibili.com"
#cookie操作
with open(r'G:\好东西\py\文件\bili_cookie.txt','r') as f:
    cookie_string = f.read()
    cookie_string = re.sub("true","True",cookie_string)
    cookie_string = re.sub("false","False",cookie_string)
    cookie_list = list(eval(cookie_string))
driver.get(url)
for cookie in cookie_list:
    if cookie['sameSite']:#虽然不知道这玩意干嘛用，但是不弹掉会报错
        cookie.pop('sameSite')
    driver.add_cookie(cookie)
driver.get(url)#重开网页
#不退出了


