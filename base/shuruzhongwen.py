import os
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base.appelement import *
from base.activity import *
from base.screenshot import *
from time import sleep
# 启动app
driver = desired_caps()
sleep(4)

swip1 = swipLeft(driver,500)
sleep(1)
swip2 = swipLeft(driver,500)
sleep(1)
driver = mainpage(driver)

login = login(driver,'p123456','p123456')
sleep(8)
# 进入设置中心
el8 = driver.find_element_by_accessibility_id("p123456\nVIP1\np123456")
el8.click()
sleep(1)
# 进入我的昵称
el9 = driver.find_element_by_accessibility_id("我的昵称\np123456")
el9.click()
sleep(1)
el10 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText")
el10.click()
el11 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText/android.view.View")
el11.click()
el10.click()
el10.send_keys(u"我的昵称")