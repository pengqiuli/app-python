import warnings
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from base.activity import *
from time import sleep
import unittest

class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.driver = desired_caps()
        sleep(4)
        driver = jinrushouye(cls.driver)
        driver = mainpage(cls.driver)
        login1 = login(driver,"peng","peng123")
        sleep(8)
        el = driver.find_element_by_accessibility_id("服务中心").click()
        el1 = driver.find_element_by_accessibility_id("意见反馈\n不好用 快来吐槽").click()
        sleep(1)

    def test_feedback_001(self):
        # 意见输入框为空
        feedback1 = feedback(self.driver,"","phone","15002076811","")
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_01.png')

    def test_feedback_002(self):
        # 意见反馈少于10个字符
        feedback2 = feedback(self.driver, "123456789", "phone", "15002076811", "dhng")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_02.png')

    def test_feedback_003(self):
        # 意见反馈为10个字符，电话号码少一位
        clean = clean_feedback(self.driver)
        feedback3 = feedback(self.driver, "1234567890", "phone", "1500207681", "dhng")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_03.png')

    def test_feedback_004(self):
        # 意见反馈为10字符，电话号码为空
        clean = clean_feedback(self.driver)
        feedback5 = feedback(self.driver, "1234567890", "phone", "", "dhng")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_04.png')

    def test_feedback_005(self):
        # 意见反馈为10个字符，邮箱格式不正确
        clean = clean_feedback(self.driver)
        feedback5 = feedback(self.driver,"1234567890","youxiang","124588@qq","dhng")
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_05.png')

    def test_feedback_006(self):
        # 意见反馈为10个字符，邮箱为空
        clean = clean_feedback(self.driver)
        feedback6 = feedback(self.driver,"1234567890","youxiang","","dhng")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_06.png')

    def test_feedback_007(self):
        # 图片验证码为空
        clean = clean_feedback(self.driver)
        feedback7 = feedback(self.driver,"1234567890","phone","15107174290","")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_07.png')

    def test_feedback_008(self):
        # 图片验证码错误
        clean = clean_feedback(self.driver)
        feedback8 = feedback(self.driver, "1234567890", "phone", "15107174290", "1111")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_08.png')

    def test_feedback_009(self):
        # 以电话类型提交，所有数据都正确
        clean = clean_feedback(self.driver)
        feedback8 = feedback2(self.driver, "1234567890", "phone", "15107174290")
        yanzhengma = code(self.driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]")
        el4.send_keys(yanzhengma)
        el5 = self.driver.find_element_by_accessibility_id("确认").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_09.png')

    def test_feedback_010(self):
        el1 = self.driver.find_element_by_accessibility_id("意见反馈\n不好用 快来吐槽").click()
        sleep(1)
        feedback8 = feedback2(self.driver, "1234567890", "youxiang", "1151853956@qq.com")
        yanzhengma = code(self.driver, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]")
        el4.send_keys(yanzhengma)
        el5 = self.driver.find_element_by_accessibility_id("确认").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_feedback_photo_010.png')

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()

