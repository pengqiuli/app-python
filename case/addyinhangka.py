import warnings
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from base.activity import *
from time import sleep
import unittest

class test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # 启动app
        self.driver = desired_caps()
        sleep(4)
        self.driver = jinrushouye(self.driver)
        self.driver = mainpage(self.driver)
        login1 = login(self.driver,"peng","peng123")
        sleep(6)
        addyinhangka = add_yhk(self.driver)
        sleep(1)

    def test_addyinhangka_001(self):
        # 持卡人为空
        # yinhangka = tianjiayhk_01(self.driver,"","6214838652327869")
        el = self.driver.find_element_by_accessibility_id("确认提交").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_01.png')

    def test_addyinhangka_002(self):
        # 银行卡号为空
        yinhangka = tianjiayhk_01(self.driver,"彭秋丽","")
        el = self.driver.find_element_by_accessibility_id("确认提交").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_02.png')

    def test_addyinhangka_003(self):
        # 国家地区代码为空
        yinhangka = tianjiayhk_01(self.driver, "彭秋丽", "6214838652327869")
        el = self.driver.find_element_by_accessibility_id("确认提交").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_03.png')

    def test_addyinhangka_004(self):
        # 手机号为空
        yinhangka = tianjiayhk_01(self.driver, "彭秋丽", "6214838652327869")
        yinhangka2 = tianjiayhk_02(self.driver,"")
        el = self.driver.find_element_by_accessibility_id("确认提交").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_04.png')

    def test_addyinhangka_005(self):
        # 图片验证码为空
        yinhangka = tianjiayhk_01(self.driver,"彭秋丽","6214838652327869")
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]").click()
        sleep(1)
        TouchAction(self.driver).press(x=134, y=1212).move_to(x=138, y=1120).release().perform()
        sleep(1)
        el3 = self.driver.find_element_by_accessibility_id("确定").click()
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]")
        el4.send_keys("15219451564")
        el5 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]")
        el5.send_keys("")
        el = self.driver.find_element_by_accessibility_id("确认提交").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_05.png')

    def test_addyinhangka_006(self):
        # 短信验证码为空
        yinhangka = tianjiayhk_01(self.driver, "彭秋丽", "6214838652327869")
        yinhangka2 = tianjiayhk_02(self.driver, "15219451564")
        el6 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(1)
        el = self.driver.find_element_by_accessibility_id("确认提交").click()
        sleep(0.5)
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_06.png')

    def test_addyinhangka_007(self):
        # 未选择银行卡类型
        yinhangka = tianjiayhk_01(self.driver,"彭秋丽","6230580000079803735")
        el = self.driver.find_element_by_accessibility_id("确认提交").click()
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_07.png')

    def test_addyinhangka_008(self):
        # 银行卡类型与卡号不符
        yinhangka = tianjiayhk_01(self.driver, "彭秋丽", "6230580000079803735")
        el = self.driver.find_element_by_accessibility_id("卡类型\n选择银行").click()
        sleep(1)
        el1 = self.driver.find_element_by_accessibility_id("b\n北京农村商业银行").click()
        sleep(1)
        el2 = self.driver.find_element_by_accessibility_id("确认提交").click()
        sleep(0.3)
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_08.png')

    def test_addyinhangka_009(self):
        # 手机号格式错误
        yinhangka = tianjiayhk_01(self.driver, "彭秋丽", "6214838652327869")
        yinhangka2 = tianjiayhk_02(self.driver,"1521945156")
        el6 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_09.png')

    def test_addyinhangka_010(self):
        # 手机号未注册
        yinhangka = tianjiayhk_01(self.driver, "彭秋丽", "6214838652327869")
        yinhangka2 = tianjiayhk_02(self.driver, "15219451565")
        el6 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_010.png')

    def test_addyinhangka_011(self):
        # 图片验证码错误
        yinhangka = tianjiayhk_01(self.driver, "彭秋丽", "6214838652327869")
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]").click()
        sleep(1)
        TouchAction(self.driver).press(x=134, y=1212).move_to(x=138, y=1120).release().perform()
        sleep(1)
        el3 = self.driver.find_element_by_accessibility_id("确定").click()
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]")
        el4.send_keys("15219451564")
        el5 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]")
        el5.send_keys("0000")
        el6 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_011.png')

    def test_addyinhangka_012(self):
        # 短信验证码错误
        yinhangka = tianjiayhk_01(self.driver, "彭秋丽", "6214838652327869")
        yinhangka2 = tianjiayhk_02(self.driver,"15219451564")
        el6 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        el7 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[5]")
        el7.send_keys("0000")
        sleep(1)
        el2 = self.driver.find_element_by_accessibility_id("确认提交").click()
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_012.png')

    def test_addyinhangka_013(self):
        # 所有信息都正确,手机号手动输入
        yinhangka = tianjiayhk_01(self.driver, "彭秋丽", "6214838652327869")
        yinhangka2 = tianjiayhk_02(self.driver, "15219451564")
        el6 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        el7 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[5]")
        sleep(10)
        el2 = self.driver.find_element_by_accessibility_id("确认提交").click()
        self.driver.get_screenshot_as_file(r'E:\images\test_addyinhangka_photo_013.png')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()