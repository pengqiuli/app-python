import os
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
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
        swip3 = swipLeft(driver,500)
        driver = mainpage(driver)

        el2 = driver.find_element_by_accessibility_id("忘记用户名")
        el2.click()
        sleep(1)

    def test_forgot_username_001(self):
        # 忘记用户名,手机号为空
        fogret = forget_username(self.driver,"")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_01.png')

    def test_forgot_username_002(self):
        # 忘记用户名，图片验证码为空
        fogret = forget_username(self.driver,"15219451564")
        sleep(0.8)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_02.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_003(self):
        # 忘记用户名，短信验证码为空
        fogret = forget_username(self.driver,"15219451564")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_03.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_004(self):
        # 忘记用户名，手机号未注册
        fogret = forget_username(self.driver,"15219451564")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_03.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_005(self):
        # 手机号格式错误
        fogret = forget_username(self.driver,"1521945156")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_04.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_006(self):
        # 图片验证码错误，手动输入图片验证码
        fogret = forget_username(self.driver,"15219451564")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_05.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_007(self):
        # 短信验证码错误，手动输入短信验证码
        forget = forget_username(self.driver,"15219451564")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_06.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_008(self):
        # 正常用例，数据都正确，手动输入正确的短信验证码和图片验证码
        fogret = forget_username(self.driver,"15219451564")
        sleep(2)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_07.png')

    @classmethod
    def tearDownClass(cls):
        pass


