from appium import webdriver
from time import sleep

class AppElement:
    def __init__(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1',
                        'deviceName': '127.0.0.1:62025',
                        'appPackage': 'com.hengyishuzi.digital',
                        'appActivity': '.MainActivity',
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def mainpage(self):
        element = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="立即体验"]').click()
        sleep(3)
        element1 = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="同意，继续使用"]').click()
        sleep(1)
        element2 = self.driver.find_element_by_xpath('//android.view.View[@content-desc="我的"]').click()
        sleep(1)
        element3 = self.driver.find_element_by_xpath('//android.view.View[@content-desc="点击登录赚钱"]').click()
        sleep(1)

    def login(self, username, password):
        el1 = self.driver.find_element("xpath","//android.widget.ImageView[@content-desc=\"欢迎您登录恒亿数字～\n恒亿商城用户可直接登录\"]/android.widget.EditText[1]")
        el1.send_keys(username)
        el2 = self.driver.find_element("xpath","//android.widget.ImageView[@content-desc=\"欢迎您登录恒亿数字～\n恒亿商城用户可直接登录\"]/android.widget.EditText[2]")
        el2.send_keys(password)



