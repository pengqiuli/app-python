import os
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base.activity import *
from time import sleep
import  unittest

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
        driver = mainpage(driver)

        # 进入注册页面
        el1 = driver.find_element_by_accessibility_id("注册")
        el1.click()
        sleep(1)

    def test_register_001(self):
        # 手机号为空
        register_1 = register(self.driver,"p12345","")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_02.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        sleep(1)

    def test_register_002(self):
        # 用户名为空
        register1 = register(self.driver," ","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_01.png')
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_003(self):
        # 图片验证码为空,手动输入图片验证码
        register3 = register(self.driver,"p12345","15219451564")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_03.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        sleep(1)
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_004(self):
        # 短信验证码为空，手动输入短信验证码
        register4 = register(self.driver,"p12345","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_04.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_005(self):
        # 用户名已注册,验证码手动输入
        register5 = register(self.driver,"p123456","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_05.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_006(self):
        # 用户名为1个字符
        register6 = register(self.driver,"p","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_06.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_007(self):
        # 用户名首位非英文
        register7 = register(self.driver,"123456p","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_07.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_008(self):
        # 用户名为纯数字
        register8 = register(self.driver,"123456","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_08.png')
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_009(self):
        # 手机号格式不正确
        register9 = register(self.driver,"p12345","1521945156")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_09.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_010(self):
        # 手机号已注册
        register10 = register(self.driver,"p12345","15002076811")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_10.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_011(self):
        # 图片验证码错误，手动输入验证码
        register11 = register(self.driver,"p12345","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_11.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_012(self):
        # 短信验证码错误，手动输入错误
        register12 = register(self.driver,"p12345","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_12.png')
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]/android.view.View")
        el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View")
        el3.click()

    def test_register_013(self):
        # 用户名和手机号都符合要求
        register13 = register(self.driver,"p12345","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_13.png')

    def test_register_014(self):
        # 登录密码为空
        register14 = register2(self.driver,"","p12345")
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_14.png')
        el5 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[2]")
        el5.click()

    def test_register_015(self):
        # 确认密码为空
        register15 = register2(self.driver,"p123456","")
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_15.png')
        el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[1]")
        el4.click()

    def test_register_016(self):
        # 登录密码为5位
        register16 = register2(self.driver,"p1234","p1234")
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_16.png')
        el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[1]")
        el4.click()
        el5 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[2]")
        el5.click()

    def test_register_017(self):
        # 登录密码为6位数字
        register17 = register2(self.driver,"123456","123456")
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_17.png')
        el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[1]")
        el4.click()
        el5 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[2]")
        el5.click()

    def test_register_018(self):
        # 登录密码为6位字母
        register18 = register2(self.driver,"qwerty","qwerty")
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_18.png')
        el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[1]")
        el4.click()
        el5 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[2]")
        el5.click()

    def test_register_019(self):
        # 登录密码与确认密码不一致
        register19 = register2(self.driver,"p12345","p123456")
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_19.png')
        el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[1]")
        el4.click()
        el5 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]/android.view.View[2]")
        el5.click()

    def test_register_020(self):
        # 登录密码和确认密码一致符合要求
        register20 = register2(self.driver,"p12345","p12345")
        self.driver.get_screenshot_as_file(r'E:\images\test_register_photo_20.png')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


