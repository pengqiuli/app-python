import os
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from appium import webdriver
from base.activity import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import unittest

class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 启动app
        driver = desired_caps()
        sleep(4)
        swip1 = swipLeft(driver,500)
        sleep(1)
        swip2 = swipLeft(driver,500)
        sleep(1)
        swip2 = swipLeft(driver,500)
        driver = mainpage(driver)
        login = cls.login(driver,"peng1","peng123")
        sleep(5)
        el = driver.find_element_by_accessibility_id("任务").click()
        TouchAction(driver).tap(x = 300,y = 310).perform()

    def tearDownClass(cls) -> None:
        pass













