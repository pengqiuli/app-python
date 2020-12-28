import os
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from appium import webdriver
from base.activity import *
from time import sleep
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

        login1 = login(driver,'peng1','peng123')
        sleep(8)
        # 进入设置中心
        el1 = driver.find_element_by_accessibility_id("peng1\npeng1")
        el1.click()
        sleep(1)
        # 进入我的昵称
        el2 = driver.find_element_by_accessibility_id("我的昵称\npeng1")
        el2.click()
        sleep(1)
        cls.driver = driver

    def test_nicheng_001(self):
        # 昵称为空
        nicheng1 = nicheng(self.driver,"")
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_nicheng_photo_01.png')

    def test_nicheng_002(self):
        # 昵称为1个字符
        nicheng2 = nicheng(self.driver,"我")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_nicheng_photo_02.png')

    def test_nicheng_003(self):
        # 输入特殊字符
        clean2 = clean_nicheng(self.driver)
        nicheng3 = nicheng(self.driver,"@##$")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_nicheng_photo_03.png')

    def test_nicheng_004(self):
        # 输入符合条件的昵称
        clean1 = clean_nicheng(self.driver)
        nicheng4 = nicheng(self.driver,u"peng1")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_nicheng_photo_04.png')

    @classmethod
    def tearDownClass(cls):
        pass
#
# if __name__ == "__main__":
#     unittest.main()

