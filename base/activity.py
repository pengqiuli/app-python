from time import sleep
from appium import webdriver
from PIL import Image
# from PIL import ImageEnhance
# import pytesseract
import time
# import os
# import logging
# import datetime
from base.log import *
from coon.chaojiying import Chaojiying_Client
from appium.webdriver.common.touch_action import TouchAction

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
    sleep(1)
    return driver

def mainpage(driver):
    element = driver.find_element_by_accessibility_id("立即体验").click()
    sleep(3)
    element1 = driver.find_element_by_accessibility_id("同意，继续使用").click()
    element2 = driver.find_element_by_accessibility_id("我的").click()
    sleep(1)
    element3 = driver.find_element_by_accessibility_id("点击登录赚钱").click()
    sleep(1)
    return driver

# 清除登录输入框的相关操作
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

# 登录相关操作
def login(driver,username,password):
    el3 = driver.find_element_by_xpath(
        "//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[1]")
    el3.send_keys(username)
    el4 = driver.find_element_by_xpath(
        "//android.widget.ImageView[@content-desc=\"欢迎您登录HOYISELL\"]/android.widget.EditText[2]")
    el4.send_keys(password)
    el5 = driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登录\"]").click()

# 忘记用户名的相关操作,图片验证码为空或者错误
def forget_username(driver,phonenumber,photocode):
    el3 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]")
    el3.send_keys(phonenumber)
    el4 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
    el4.send_keys(photocode)
    el5 = driver.find_element_by_accessibility_id("获取验证码").click()
    el6 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[3]")
    # sleep(20)
    el7 = driver.find_element_by_accessibility_id("确定找回").click()

# 忘记用户名相关操作,图片验证码在unittest框架通过函数自动识别
def forget_username2(driver,phonenb):
    el = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]")
    sleep(1)
    TouchAction(driver).press(x=134, y=1212).move_to(x=138, y=1125).release().perform()
    sleep(1)
    el2 = driver.find_element_by_accessibility_id("确定").click()
    el3 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]")
    el3.send_keys(phonenb)

# 忘记密码相关操作
def forget_Password(driver,username,phonenumber):
    el1 = driver.find_element_by_xpath("//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[1]")
    el1.send_keys(username)
    sleep(1)
    el3 = driver.find_element_by_xpath(
        "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.view.View[1]").click()
    sleep(1)
    TouchAction(driver).press(x=134, y=1212).move_to(x=138, y=1125).release().perform()
    sleep(1)
    el7 = driver.find_element_by_accessibility_id("确定").click()
    el2 = driver.find_element_by_xpath(
        "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[2]")
    el2.send_keys(phonenumber)
    # el4 = driver.find_element_by_accessibility_id("获取验证码").click()
    # el5 = driver.find_element_by_xpath(
    #     "//android.view.View[@content-desc=\"验证成功后，新密码将以短信的方式发送到您的手机\"]/android.widget.EditText[4]")
    # # sleep(2)
    # el6 = driver.find_element_by_accessibility_id("确定重置").click()

# 注册相关操作
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

# 注册第二页输入密码的相关操作
def register2(driver,password,querenmima):
    el7 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]")
    el7.send_keys(password)
    el8 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[2]")
    el8.send_keys(querenmima)
    el9 = driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"注册\"]")

# 图片验证码的图片操作，此方法识别率太低，暂时没有使用
# def photocode(driver,value):
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

# 通过超级鹰来读取图片验证码，识别率很高，并且每次识别需要支付费用，图片验证码的类型要和超级鹰的验证码类型表对应
def code(driver,value):
    element = driver.find_element_by_xpath(value)
    photo1 = driver.get_screenshot_as_file("E:\\images\\photo1.png")
    location = element.location
    size = element.size
    rangle = (int(location['x'] + 2), int(location['y'] + 2), int(location['x'] + size['width'] - 2),
              int(location['y'] + size['height'] - 2))
    photo = Image.open("E:\\images\\photo1.png")
    photo = photo.crop(rangle)
    photo2 = photo.save("a.bmp")
    chaojiying = Chaojiying_Client("pql123","pql123","911227")
    im = open('a.bmp','rb').read()
    yanzhengma = chaojiying.PostPic(im,1004)['pic_str']
    photo.close()
    return yanzhengma

# 短信验证码的相关操作
def phonecode(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['heigt']
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

# 昵称的相关操作
def nicheng(driver,name):
    el11 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText")
    el11.send_keys(name)
    el3 = driver.find_element_by_accessibility_id("确认").click()

def clean_nicheng(driver):
    el6 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText/android.view.View")
    el6.click()

# 意见反馈的相关操作，输入错误图片验证码或者是不传图片验证码
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

# 意见反馈的相关操作，验证码需要单独在unittest框架里面自行调用图片验证码的函数
def feedback2(driver,advices,newtype,newnumber):
    el = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
    el.send_keys(advices)
    sleep(1)
    el1 = driver.find_element_by_accessibility_id("联系方式\n电话").click()
    if newtype == "phone":
        el2 = driver.find_element_by_accessibility_id("电话").click()
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]")
        el3.send_keys(newnumber)
    else:
        el2 = driver.find_element_by_accessibility_id("邮箱").click()
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]")
        el3.send_keys(newnumber)
        sleep(1)

# 清除意见反馈的相关输入框
def clean_feedback(driver):
    el = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
    el.clear()
    el = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]")

# 进入添加银行卡页面
def add_yhk(driver):
    el = driver.find_element_by_accessibility_id("收款账户\n1张").click()
    sleep(1)
    el1 = driver.find_element_by_accessibility_id("+\n添加收款账户").click()
    el2 = driver.find_element_by_accessibility_id("添加银行卡").click()

# 添加银行卡的相关操作
def tianjiayhk_01(driver,name,cardnumber):
    el = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]")
    el.send_keys(name)
    sleep(1)
    el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]")
    el1.send_keys(cardnumber)
    sleep(1)

# 添加银行卡的相关操作第二步
def tianjiayhk_02(driver,phonenumber):
    el2 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]").click()
    sleep(1)
    TouchAction(driver).press(x=134, y=1212).move_to(x=138, y=1120).release().perform()
    sleep(1)
    el3 = driver.find_element_by_accessibility_id("确定").click()
    el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]")
    el4.send_keys(phonenumber)
    photocode = code(driver,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView[2]")
    el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]")
    el5.send_keys(photocode)
    # el6 = driver.find_element_by_accessibility_id("获取验证码").click()

# 进入移除银行卡页面
def yichu_yhk(driver):
    el = driver.find_element_by_accessibility_id("收款账户\n1张").click()
    sleep(1)
    el1 = driver.find_element_by_accessibility_id("招商银行\n默认收款账户\n储蓄卡\n**** **** **** 7869 ").click()
    sleep(1)
    el2 = driver.find_element_by_accessibility_id("解绑银行卡")

# 进入修改登录密码页面
def xiugaipwd(driver):
    el = driver.find_element_by_accessibility_id("设置中心").click()
    el2 = driver.find_element_by_accessibility_id("修改登录密码").click()
    sleep(1)

# 修改登录密码
def xiugaipassword(driver,oldpassword,newpassword,password):
    el = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText")
    el.send_keys(oldpassword)
    el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[1]")
    el1.send_keys(newpassword)
    el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[2]")
    el2.send_keys(password)
    el4 = driver.find_element_by_accessibility_id("确认")
    el4.click()

# 修改登录密码清除输入框的操作
def xgpassword_clear(driver):
    el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText/android.view.View[2]")
    el1.click()
    sleep(0.5)
    el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[1]/android.view.View[2]")
    el2.click()
    sleep(0.5)
    el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[2]/android.view.View[2]")
    el3.click()

# 进入设置交易密码页面
def setjymima(driver,mima,qrmima):
    el = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[1]")
    el.send_keys(mima)
    el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[2]")
    el1.send_keys(qrmima)
    el2 = driver.find_element_by_accessibility_id("确认").click()

# 设置交易密码清除输入框操作
def setjymima_clear(driver):
    el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[1]/android.view.View[2]")
    el1.click()
    sleep(1)
    el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.EditText[2]/android.view.View[2]")
    el2.click()

# 通过坐标定位
# 重新封装点击某一点相对坐标的方法
def tapA(driver,x,y):
    # 比例系数
    x1 = x/1080
    y1 = y/2340
    # 获取新测试机屏幕宽、高
    w = driver.get_window_size()['width']
    h = driver.get_window_size()['height']
    # 屏幕宽高乘以A点的比例系数，即可得A点在新测试机上坐标
    driver.tap(x1*w, y1*h)

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
def getTime():
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












