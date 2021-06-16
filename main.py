#-*-coding:euc-kr
"""
Author : Black Cows
2021.06.16
크롬을 활용하여 구글에서 고양이 사진 다운받는 프로그램
"""

import time
import random
import pywinmacro as pw

location = (557, 1056)
location2 = (618, 248)
location3 = (636, 428)
location_next = (878, 186)


def scrap():
    chromeopen()
    time.sleep(1)
    pw.type_in("고양이")
    pw.key_press_once("enter")
    time.sleep(2)

    for i in range(12):
        pw.key_press_once("tab")
        time.sleep(0.1)
    pw.key_press_once("enter")
    time.sleep(1)

    for j in range(29):
        pw.key_press_once("tab")
        time.sleep(0.1)
    pw.key_press_once("enter")
    time.sleep(3)

    while True:
        downloads()
        time.sleep(1)
        pw.click(location_next)
        time.sleep(2)


def chromeopen():
    pw.key_on("window")
    pw.key_on("r")
    pw.key_off("window")
    pw.key_off("r")
    time.sleep(0.5)
    pw.type_in('"chrome" -incognito')
    time.sleep(2)
    pw.key_press_once("enter")


def downloads():
    pw.right_click(location2)
    time.sleep(0.5)
    pw.click(location3)
    time.sleep(1)
    pw.key_press_once("enter")

