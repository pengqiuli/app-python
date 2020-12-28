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
        swip2 = swipLeft(driver, 500)
        driver = mainpage(driver)
        # 进入忘记密码页面
        el1 = driver.find_element_by_accessibility_id("忘记密码")
        el1.click()

    def test_forget_password_001(self):
        # 用户名为空
        forget = forget_Password(self.driver,"","15419451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_01.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]/android.view.View")
        el2.click()

    def test_forget_password_002(self):
        # 手机号为空
        forget = forget_Password(self,"p123456","")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_02.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[1]/android.view.View")
        el2.click()

    def test_forget_password_003(self):
        # 图片验证码为空,验证码手动输入
        forget = forget_Password(self.driver,"p123456","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_03.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]/android.view.View")
        el2.click()

    def test_forget_password_004(self):
        # 短信验证码为空，验证码手动输入
        forget = forget_Password(self.driver,"p123456","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_04.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]/android.view.View")
        el2.click()

    def test_forget_password_005(self):
        # 用户名不存在
        forget = forget_Password(self.driver,"p12345","15419451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_05.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]/android.view.View")
        el2.click()

    def test_forget_password_006(self):
        # 用户名和手机号不匹配
        forget = forget_Password(self.driver,"p123456","15419451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_06.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]/android.view.View")
        el2.click()

    def test_forget_password_007(self):
        # 手机号未注册
        forget = forget_Password(self.driver,"p123456","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_07.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]/android.view.View")
        el2.click()

    def test_forget_password_008(self):
        # 手机号格式不正确
        forget = forget_Password(self.driver,"p12345","1500207681")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_08.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]/android.view.View")
        el2.click()

    def test_forget_password_009(self):
        # 图片验证码错误，手动输入错误
        forget = forget_Password(self.driver,"p12345","15002076811")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_09.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]/android.view.View")
        el2.click()

    def test_forget_password_010(self):
        # 短信验证码错误，手动输入错误
        forget = forget_Password(self.driver,"p12345","15002076811")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_10.png')
        el2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]/android.view.View")
        el2.click()

    def test_forget_password_011(self):
        # 填写的信息都正确，图片验证码和短信验证码手动输入正确
        forget = forget_Password(self.driver,"p123456","15002076811")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_11.png')

    @classmethod
    def tearDownClass(cls):
        pass






