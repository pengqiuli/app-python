import os
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from appium import webdriver
from base.activity import *
from time import sleep
import unittest
import warnings

class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        # 启动app
        cls.driver = desired_caps()
        sleep(4)
        driver = jinrushouye(cls.driver)
        driver = mainpage(cls.driver)
        el2 = driver.find_element_by_accessibility_id("忘记用户名")
        el2.click()
        sleep(1)

    def test_forgot_username_001(self):
        # 忘记用户名，区号未选择
        el7 = self.driver.find_element_by_accessibility_id("确定找回").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_01.png')

    def test_forgot_username_002(self):
        # 忘记用户名,手机号为空
        el = self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]").click()
        sleep(1)
        TouchAction(self.driver).press(x=134, y=1212).move_to(x=138, y=1125).release().perform()
        sleep(1)
        el2 = self.driver.find_element_by_accessibility_id("确定").click()
        fogret = forget_username(self.driver,"","")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_02.png')

    def test_forgot_username_003(self):
        # 忘记用户名，图片验证码为空
        fogret = forget_username(self.driver,"15219451564","")
        sleep(0.8)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_03.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_004(self):
        # 忘记用户名，短信验证码为空
        fogret = forget_username2(self.driver,"15219451564")
        photocode = code(self.driver,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ImageView")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
        el4.send_keys(photocode)
        el7 = self.driver.find_element_by_accessibility_id("确定找回").click()
        sleep(0.8)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_04.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_005(self):
        # 忘记用户名，手机号未注册
        fogret = forget_username2(self.driver,"15219451565")
        photocode = code(self.driver,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ImageView")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
        el4.send_keys(photocode)
        el5 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_05.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_006(self):
        # 手机号格式错误
        fogret = forget_username2(self.driver,"1521945156")
        photocode = code(self.driver,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ImageView")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
        el4.send_keys(photocode)
        el5 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_06.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_007(self):
        # 图片验证码错误，手动输入图片验证码
        fogret = forget_username(self.driver,"15219451564","0000")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_07.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_008(self):
        # 短信验证码错误
        forget = forget_username2(self.driver,"15219451564")
        photocode = code(self.driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ImageView")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
        el4.send_keys(photocode)
        el5 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        el6 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[3]")
        el6.send_keys("0000")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_08.png')
        sleep(1)
        el6 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el6.click()

    def test_forgot_username_009(self):
        # 正常用例，数据都正确，手动输入正确的短信验证码
        fogret = forget_username2(self.driver,"15219451564")
        photocode = code(self.driver,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ImageView")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
        el4.send_keys(photocode)
        el5 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        el6 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[3]")
        sleep(2)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_username_photo_09.png')

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()

