import os
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from appium import webdriver
from base.activity import *
from time import sleep
import unittest

# 启动app
class test(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        driver = desired_caps()
        sleep(4)

        swip1 = swipLeft(driver,500)
        sleep(1)
        swip2 = swipLeft(driver,500)
        sleep(1)
        swip3 = swipLeft(driver,500)
        driver = mainpage(driver)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_login_001(self):
        # 异常登录，密码错误
        login1 = login(self.driver,'peng','p12345')
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_login_photo_01.png')
        clean = login_clean(self.driver)

    def test_login_002(self):
        # 异常登录，用户名错误
        login2 = login(self.driver,'p12346','peng123')
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_login_photo_02.png')
        clean = login_clean(self.driver)

    # def test_login_003(self):
    #     # 异常登录，用户名为空
    #     login3 = login(self.driver,'','p123456')
    #     self.driver.get_screenshot_as_file(r'E:\images\test_login_photo_03.png')
    #     el7 = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[2]/android.view.View[2]")
    #     el7.click()
    #
    # def test_login_004(self):
    #     # 异常登录，密码为空
    #     login4 = login(self.driver,'peng','')
    #     sleep(1)
    #     self.driver.get_screenshot_as_file(r'E:\images\test_login_photo_04.png')
    #     el6 = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[1]/android.view.View")
    #     el6.click()
    #
    # def test_login_005(self):
    #     # 异常登录，连续四次没有登录成功
    #     login5 = login(self.driver,'p123456','p123456')
    #     sleep(1)
    #     self.driver.get_screenshot_as_file(r'E:\images\test_login_photo_05.png')
    #     clean = login_clean(self.driver)
    #
    # def test_login_006(self):
    #     # 账号被冻结
    #     login6 = login(self.driver,'p123456789','p123456789')
    #     sleep(0.4)
    #     self.driver.get_screenshot_as_file(r'E:\images\test_login_photo_06.png')
    #     clean = login_clean(self.driver)
    #
    # def test_login_007(self):
    #     # 密码明文显示
    #     el1 = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[2]").send_keys("p123456")
    #     el = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[2]/android.view.View[1]")
    #     el.click()
    #     sleep(1)
    #     self.driver.get_screenshot_as_file(r'E:\images\test_login_photo_07.png')
    #     el7 = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[2]/android.view.View[2]")
    #     el7.click()

    def test_login_008(self):
        # 正确的用户名密码
        login8 = login(self.driver,'peng','peng123')
        sleep(5)
        self.driver.get_screenshot_as_file(r'E:\images\test_login_photo_08.png')

if __name__ == "__main__":
    unittest.main()
















