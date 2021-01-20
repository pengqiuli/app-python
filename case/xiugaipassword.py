import warnings
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from base.activity import *
from time import sleep
import unittest

class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        # 启动app
        cls.driver = desired_caps()
        sleep(4)
        cls.driver = jinrushouye(cls.driver)
        cls.driver = mainpage(cls.driver)
        login1 = login(cls.driver, "peng", "peng123")
        sleep(6)
        xiugaipd = xiugaipwd(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_xiugaipassword_001(self):
        # 原登录密码为空
        xgpassword = xiugaipassword(self.driver,"","peng123","peng123")
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_xiugaipassword_photo_01.png')
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[1]/android.view.View[2]")
        el2.click()
        sleep(0.5)
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[2]/android.view.View[2]")
        el3.click()

    def test_xiugaipassword_002(self):
        # 新密码为空
        xgpassword2 = xiugaipassword(self.driver,"peng123","","peng123")
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_xiugaipassword_photo_02.png')
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText/android.view.View[2]")
        el1.click()
        sleep(0.5)
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[2]/android.view.View[2]")
        el3.click()

    def test_xiugaipassword_003(self):
        # 确认密码为空
        xgpassword3 = xiugaipassword(self.driver,"peng123","peng123","")
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_xiugaipassword_photo_03.png')
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText/android.view.View[2]")
        el1.click()
        sleep(0.5)
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[1]/android.view.View[2]")
        el2.click()

    def test_xiugaipassword_004(self):
        # 旧密码错误
        xgpassword4 = xiugaipassword(self.driver,"peng1234","peng123","peng123")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_xiugaipassword_photo_04.png')
        clear = xgpassword_clear(self.driver)

    def test_xiugaipassword_005(self):
        # 新密码为5位
        xgpassword5 = xiugaipassword(self.driver,"peng123","peng1","peng1")
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_xiugaipassword_photo_05.png')
        clear2 = xgpassword_clear(self.driver)

    def test_xiugaipassword_006(self):
        # 新密码为6位英文
        xgpassword5 = xiugaipassword(self.driver, "peng123", "pengqi", "pengqi")
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_xiugaipassword_photo_06.png')
        clear3 = xgpassword_clear(self.driver)

    def test_xiugaipassword_007(self):
        # 新密码为6位数字
        xgpassword5 = xiugaipassword(self.driver, "peng123", "123456", "123456")
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_xiugaipassword_photo_07.png')
        clear4 = xgpassword_clear(self.driver)

    def test_xiugaipassword_008(self):
        # 新密码与确认密码不一致
        xgpassword5 = xiugaipassword(self.driver, "peng123", "peng123", "peng12")
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_xiugaipassword_photo_08.png')
        clear5 = xgpassword_clear(self.driver)

    def test_xiugaipassword_009(self):
        # 新密码和原密码符合要求
        xgpassword5 = xiugaipassword(self.driver, "peng123", "peng123", "peng123")
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_xiugaipassword_photo_09.png')

if __name__ == "__main__":
    unittest.main()