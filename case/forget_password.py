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
        # 进入忘记密码页面
        el1 = self.driver.find_element_by_accessibility_id("忘记密码")
        el1.click()
        sleep(1)

    def test_forget_password_001(self):
        # 用户名为空
        forget = forget_Password(self.driver,"","15419451564")
        el6 = self.driver.find_element_by_accessibility_id("确定重置").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_01.png')

    def test_forget_password_002(self):
        # 手机号为空
        forget = forget_Password(self,"peng","")
        el4 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_02.png')

    def test_forget_password_003(self):
        # 图片验证码为空,验证码手动输入
        forget = forget_Password(self.driver,"peng","15219451564")
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_03.png')

    def test_forget_password_004(self):
        # 短信验证码为空
        forget = forget_Password(self.driver,"peng","15219451564")
        photocode = code(self.driver,
                         "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.ImageView")
        el3 = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[3]")
        el3.send_keys(photocode)
        # el4 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        el6 = self.driver.find_element_by_accessibility_id("确定重置").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_04.png')

    def test_forget_password_005(self):
        # 用户名不存在
        forget = forget_Password(self.driver,"p12345","15419451564")
        photocode = code(self.driver,
                         "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.ImageView")
        el3 = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[3]")
        el3.send_keys(photocode)
        el4 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_05.png')

    def test_forget_password_006(self):
        # 用户名和手机号不匹配
        forget = forget_Password(self.driver,"peng1","15419451564")
        sleep(1)
        photocode = code(self.driver,
                         "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.ImageView")
        el3 = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[3]")
        el3.send_keys(photocode)
        el4 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_06.png')

    def test_forget_password_007(self):
        # 手机号未注册
        forget = forget_Password(self.driver,"peng","12312312312")
        sleep(1)
        photocode = code(self.driver,
                         "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.ImageView")
        el3 = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[3]")
        el3.send_keys(photocode)
        el4 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_07.png')

    def test_forget_password_008(self):
        # 手机号格式不正确
        forget = forget_Password(self.driver,"peng","1500207681")
        sleep(1)
        photocode = code(self.driver,
                         "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.ImageView")
        el3 = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[3]")
        el3.send_keys(photocode)
        el4 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_08.png')

    def test_forget_password_009(self):
        # 图片验证码错误
        forget = forget_Password(self.driver,"peng","15002076811")
        sleep(1)
        el3 = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[3]")
        el3.send_keys("1111")
        el4 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_09.png')

    def test_forget_password_010(self):
        # 短信验证码错误输入错误
        forget = forget_Password(self.driver,"peng","15002076811")
        sleep(1)
        photocode = code(self.driver,
                         "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.ImageView")
        el3 = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[3]")
        el3.send_keys(photocode)
        el4 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        el5 = self.driver.find_element_by_xpath(
                "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[4]")
        el5.send_keys("0000")
        el6 = self.driver.find_element_by_accessibility_id("确定重置").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_10.png')

    def test_forget_password_011(self):
        # 填写的信息都正确，图片验证码和短信验证码手动输入正确
        forget = forget_Password(self.driver,"peng","15002076811")
        sleep(1)
        photocode = code(self.driver,
                         "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.ImageView")
        el3 = self.driver.find_element_by_xpath(
            "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[3]")
        el3.send_keys(photocode)
        el4 = self.driver.find_element_by_accessibility_id("获取验证码").click()
        sleep(10)
        el6 = self.driver.find_element_by_accessibility_id("确定重置").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_11.png')

    def test_forget_password_012(self):
        # 国家地区代码未选择
        el1 = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[1]")
        el1.send_keys("peng")
        el6 = self.driver.find_element_by_accessibility_id("确定重置").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r'E:\images\test_forget_Password_photo_12.png')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()




