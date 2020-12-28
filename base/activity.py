from time import sleep
from appium import webdriver
from PIL import Image
from PIL import ImageEnhance
import pytesseract
import time
import os
import logging
import datetime
from base.log import *
from coon.chaojiying import Chaojiying_Client

def desired_caps():
    d_caps = {'platformName': 'Android',
              'platformVersion': '5.1',
              'deviceName': '127.0.0.1:62025',
              'appPackage': 'com.hengyishuzi.digital',
              'appActivity': '.MainActivity',
              'unicodeKeyboard': True,
              'resetKeyboard' : True
              }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', d_caps)
    return driver

def jinrushouye(driver):
    swip1 = swipLeft(driver, 500)
    sleep(1)
    swip2 = swipLeft(driver, 500)
    sleep(1)
    swip3 = swipLeft(driver, 500)
    return driver

def mainpage(driver):
    element = driver.find_element_by_accessibility_id("立即体验").click()
    sleep(3)
    element2 = driver.find_element_by_accessibility_id("我的").click()
    sleep(1)
    element3 = driver.find_element_by_accessibility_id("点击登录赚钱").click()
    sleep(1)
    return driver

def login_clean(driver):
    el6 = driver.find_element_by_xpath(
    "//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[1]/android.view.View")
    el6.click()
    sleep(1)
    el7 = driver.find_element_by_xpath(
    "//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[2]/android.view.View[2]")
    el7.click()
    sleep(1)
    return driver

def login(driver,username,password):
    el3 = driver.find_element_by_xpath(
        "//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[1]")
    el3.send_keys(username)
    el4 = driver.find_element_by_xpath(
        "//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[2]")
    el4.send_keys(password)
    el5 = driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登录\"]").click()


def forget_username(driver,phonenumber,photocode):
    el1 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]")
    el1.send_keys(phonenumber)
    el2 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
    el2.send_keys(photocode)
    el3 = driver.find_element_by_accessibility_id("获取验证码").click()
    el4 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[3]")
    # sleep(20)
    el5 = driver.find_element_by_accessibility_id("确定找回").click()

def forget_Password(driver,username,phonenumber):
    el2 = driver.find_element_by_xpath(
        "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[1]")
    el2.send_keys(username)
    el2 = driver.find_element_by_xpath(
        "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]")
    el2.send_keys(phonenumber)
    el3 = driver.find_element_by_xpath(
        "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[3]")
    # sleep(1)
    el4 = driver.find_element_by_accessibility_id("获取验证码").click()
    el5 = driver.find_element_by_xpath(
        "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[4]")
    # sleep(2)
    el6 = driver.find_element_by_accessibility_id("确定重置").click()

def register(driver,username,phonenumber):
    el1 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]")
    el1.send_keys(username)
    el2 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
    el2.send_keys(phonenumber)
    el3 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[3]")
    el3.click()
    sleep(1)
    el4 = driver.find_element_by_accessibility_id("获取验证码").click()
    el5 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[4]")
    el5.click()
    el6 = driver.find_element_by_accessibility_id("下一步").click()

def register2(driver,password,querenmima):
    el7 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]")
    el7.send_keys(password)
    el8 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
    el8.send_keys(querenmima)
    el9 = driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"注册\"]")

# def photocode(driver,value):
#     # 此方法识别率太低，暂时不适用
#     element = driver.find_element_by_xpath(value)
#     photo1 = driver.get_screenshot_as_file("E:\\images\\photo1.png")
#     location = element.location
#     size = element.size
#     rangle = (int(location['x']+2),int(location['y']+2),int(location['x']+size['width']-2),int(location['y']+size['heigth']-2))
#     photo = Image.open("E:\\images\\photo1.png")
#     photo = photo.crop(rangle)
#     photo2 = photo.save("E:\\images\\photo2.png")
#     img = photo2.open("E:\\images\\photo2.png")
#     img = img.convert('RGB')
#     enhancer = ImageEnhance.Color(img)
#     enhancer = enhancer.enhance(0)
#     enhancer = ImageEnhance.Brightness(enhancer)
#     enhancer = enhancer.enhance(2)
#     enhancer = ImageEnhance.Contrast(enhancer)
#     enhancer = enhancer.enhance(8)
#     enhancer = ImageEnhance.Sharpness(enhancer)
#     img = enhancer.enhance(20)
#     text = pytesseract.image_to_string(img).strip()
#     return text

def code(driver,value):
    element = driver.find_element_by_xpath(value)
    photo1 = driver.get_screenshot_as_file("E:\\images\\photo1.png")
    location = element.location
    size = element.size
    rangle = (int(location['x'] + 2), int(location['y'] + 2), int(location['x'] + size['width'] - 2),
              int(location['y'] + size['heigth'] - 2))
    photo = Image.open("E:\\images\\photo1.png")
    chaojiying = Chaojiying_Client("pql123","pql123","911227")
    im = open(photo,"rb").read()
    yanzhengma = chaojiying.PostPic(im,"1004")['pic_str']
    return yanzhengma

def phonecode(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['heigth']
    y1 = 1
    x1 = x * 0.93
    y2 = x * 0.99
    driver.swipe(x1, y1, x1, y2)
    sleep(1)
    driver.find_element_by_id('com.android.systemui:id/delete').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("获取验证码")').click()
    sleep(15)
    driver.swipe(x1, y1, x1, y2)
    sleep(1)
    Te = driver.find_element_by_id('android:id/text')
    duanxinneirong = Te.text()
    driver.swipe(x1, y2, x1, y1)
    code = duanxinneirong[10, 14]
    return code

def nicheng(driver,name):
    el11 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText")
    el11.send_keys(name)
    el3 = driver.find_element_by_accessibility_id("确认").click()

def clean_nicheng(driver):
    el6 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText/android.view.View")
    el6.click()

def feedback(driver,advices,tyep,nubmer,photocode):
    el = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
    el.send_keys(advices)
    sleep(1)
    el1 = driver.find_element_by_accessibility_id("联系方式\n电话").click()
    if tyep == "phone":
        el2 = driver.find_element_by_accessibility_id("电话").click()
        el3= driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]")
        el3.send_keys(nubmer)
    else:
        el2 = driver.find_element_by_accessibility_id("邮箱").click()
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]")
        el3.send_keys(nubmer)
        sleep(1)
    el4 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]")
    el4.send_keys(photocode)
    el5 = driver.find_element_by_accessibility_id("确认").click()

def feedback2(driver,advices,newtype,phonenumber):
    el = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
    el.send_keys(advices)
    sleep(1)
    el1 = driver.find_element_by_accessibility_id("联系方式\n电话").click()
    if newtype == "phone":
        el2 = driver.find_element_by_accessibility_id("电话").click()
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]")
        el3.send_keys(phonenumber)
    else:
        el2 = driver.find_element_by_accessibility_id("邮箱").click()
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]")
        el3.send_keys(phonenumber)
        sleep(1)

def clean_feedback(driver):
    el = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
    el.clear()
    el = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]")

# 获取屏幕大小尺寸
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def swipeUp(driver, t):
    '''向上滑动屏幕'''
    l = getSize(driver)
    x1 = int(l[0]*0.5)  # x坐标
    y1 = int(l[1]*0.75)  # 起始y坐标
    y2 = int(l[1]*0.25)  # 终点y坐标
    driver.swipe(x1,y1,x1,y2,t)

def swipeDown(driver, t):
    '''向下滑动屏幕'''
    l = getSize(driver)
    x1 = int(l[0]*0.5)  # x坐标
    y1 = int(l[1]*0.25)  # 起始y坐标
    y2 = int(l[1]*0.75)  # 终点y坐标
    driver.swipe(x1,y1,x1,y2,t)

def swipLeft(driver,t):
    # 向左滑动屏幕
    l=getSize(driver)
    x1=int(l[0]*0.5)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,t)

def swipeRight(driver,t):
    '''向右滑动屏幕'''
    l=getSize(driver)
    x1=int(l[0]*0.05)
    y1=int(l[0]*0.5)
    x2=int(l[0]*0.5)
    driver.swipe(x1,y1,x2,y1,t)

# 获取时间戳
def getTime(self):
    tamp = int(time.time())
    return tamp

# 保存截图
def screenshot(self):
    tamp = self.getTime()
    filename = '../jpg/ %s.png'%tamp
    self.driver.get_screenshot_as_file(filename)

# 打印日志
def start_log():
    cmd = "adb logcat AndroidRuntime:E *:S"
    lines = os.popen(cmd).readlines()
    if len(lines) > 0:
        logger = LogConfig.getLogger()
        for line in lines:
            if 'E' in line:
                string = line.strip('\n').split('):')[-1]
                logger.error('crash: ' + string)
# 结束打印
def end_log():
    os.system('adb kill-server')











