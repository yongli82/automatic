#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
用Python + PyObjc 写一个脚本：
1、在15:59分打开网页， https://sale.jd.com/act/4rfTusWj76kqv.html 
2、用pyautogui，滚动网页到特定位置，以一秒一次的频率点击领优惠券的位置
3、在16:00:10结束程序
"""
import time
import webbrowser
from datetime import datetime
import pyautogui

begin_time = datetime(2018, 10, 22, 15, 59, 50, 0)
end_time = datetime(2018, 10, 22, 16, 00, 10, 0)

# wait for begin time
while True:
    time.sleep(1)
    print(datetime.now())
    if datetime.now() > begin_time:
        break

print("Step1: open page")
webbrowser.open("https://sale.jd.com/act/4rfTusWj76kqv.html")
time.sleep(1)

# scroll to bottom with 10 clicks(a platform special unit) while mouse point is at (500, 400)
pyautogui.scroll(-10, x=500, y=400)
print("Step2: scroll to show the target")
time.sleep(2)

count = 0
while True:
    print("------------\n")
    print(datetime.now())
    print("Step3: move to target and click")
    # click at (948, 609)
    pyautogui.moveTo(x=948, y=609, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click()

    # if there is an alert dialog, click ok at (909,207)
    print("Step4: if there is an alert, move to button and click")
    # 没有准确获取到弹框上OK按钮的颜色
    # pyautogui.pixelMatchesColor(909, 207, (), tolerance=10)
    pyautogui.moveTo(x=909, y=207, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    count += 1
    if count > 60:
        break
    if datetime.now() > end_time:
        break


