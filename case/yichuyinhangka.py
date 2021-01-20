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
        yichu = yichu_yhk(cls.driver)
        sleep(1)

    def tearDownClass(cls) -> None:
        pass

    def test_yichuyinhangka_001(self):
        # 图片验证码为空
        el = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_yichuyinhangka_photo_01.png')

    def test_yichuyinhangka_002(self):
        # 图片验证码错误
        el = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
        el.clear()
        el.send_keys("0000")
        el2 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_yichuyinhangka_photo_02.png')

    def test_yichuyinhangka_003(self):
        # 短信验证码为空
        el = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
        el.clear()
        photocode = code(self.driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView")
        el.send_keys(photocode)
        el6 = self.driver.find_element_by_accessibility_id("确认")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_yichuyinhangka_photo_03.png')

    def test_yichuyinhangka_004(self):
        # 短信验证码为错误
        el = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
        el.clear()
        photocode = code(self.driver,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView")
        el.send_keys(photocode)
        el2 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        el3 = self. driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]")
        el3.send_keys("0000")
        el6 = self.driver.find_element_by_accessibility_id("确认")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_yichuyinhangka_photo_04.png')

    def test_yichuyinhangka_005(self):
        # 短信验证码手动输入正确
        el = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
        el.clear()
        photocode = code(self.driver,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView")
        el.send_keys(photocode)
        el2 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(10)
        el6 = self.driver.find_element_by_accessibility_id("确认")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_yichuyinhangka_photo_05.png')

if __name__ == "__main__":
    unittest.main()
