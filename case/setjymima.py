# -*-coding:utf-8-*-
from base.activity import *
from time import sleep
import unittest

class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 启动app
        cls.driver = desired_caps()
        sleep(4)
        cls.driver = jinrushouye(cls.driver)
        cls.driver = mainpage(cls.driver)
        log = login(cls.driver,"plm123","plm123")
        sleep(6)
        el = cls.driver.find_element_by_accessibility_id("交易密码\n设置").click()

    def tearDownClass(cls):
        pass

    def test_setjymima_001(self):
        # 交易密码为空
        mima = setjymima(self.driver,"","123456")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_setjymima_photo_01.png')
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[2]/android.view.View[2]")
        el2.click()

    def test_setjymima_002(self):
        # 确认交易密码为空
        mima = setjymima(self.driver,"123456","")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_setjymima_photo_02.png')
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[1]/android.view.View[2]")
        el1.click()

    def test_setjymima_003(self):
        # 两次交易密码不一致
        mima = setjymima(self.driver,"321654","123456")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_setjymima_photo_03.png')
        clear = setjymima_clear(self.driver)

    def test_setjymima_004(self):
        # 交易密码为5位
        mima = setjymima(self.driver,"32165","32165")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_setjymima_photo_04.png')
        clear1 = setjymima_clear(self.driver)

    # def test_setjymima_005(self):
    #     # 交易密码符合规范
    #     mima = setjymima(self.driver,"321654","321654")
    #     sleep(1)
    #     self.driver.get_screenshot_as_file(r'E:\images\test_setjymima_photo_05.png')
    #     clear2 = setjymima_clear(self.driver)

if __name__ == "__main__":
    unittest.main()
