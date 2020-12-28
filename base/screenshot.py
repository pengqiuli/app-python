import os
# import pytesseract
# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base.appelement import *
from base.activity import *
from time import sleep
from PIL import Image
from PIL import ImageEnhance
import pytesseract

# 启动app
driver = desired_caps()
sleep(4)

swip1 = swipLeft(driver,500)
sleep(1)
swip2 = swipLeft(driver,500)
sleep(1)
driver = mainpage(driver)

el2 = driver.find_element_by_accessibility_id("忘记用户名")
el2.click()
sleep(1)
# 图片验证码的处理
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText[1]")
el1.send_keys("15219451564")

photo1 = driver.get_screenshot_as_file("E:\\images\\photo1.png")

imagelement = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ImageView")
# 获取验证码的位置（x,y坐轴）
location = imagelement.location
# 获取验证码的长宽
size = imagelement.size
print(location,size)
# 需要截取的位置坐标
rangle = (int(location['x']+2),int(location['y']+2),int(location['x']+size['width']-2),int(location['y']+size['height']-2))

Im = Image.open("E:\\images\\photo1.png")
# 从image中的crop函数进行再次截取，截取我们需要的面积
photo = Im.crop(rangle)
photo2 = photo.save("E:\\images\\photo2.png")
# picture = Image.open("E:\\images\\photo2.png")
# text1 = pytesseract.image_to_string(picture).strip()  #直接识别识别率低，识别不出来
# print(text1)
# 修改图片的灰度
img = Image.open("E:\\images\\photo2.png")
img = img.convert('RGB')
enhancer = ImageEnhance.Color(img)
enhancer = enhancer.enhance(0)
enhancer = ImageEnhance.Brightness(enhancer)
enhancer = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancer)
enhancer = enhancer.enhance(8)
enhancer = ImageEnhance.Sharpness(enhancer)
img = enhancer.enhance(20)
text2 = pytesseract.image_to_string(img).strip()
print(text2)

# 短信验证码的处理
# 样例
# 下拉屏幕，清空消息
x = driver.get_window_size()['width']
y = driver.get_window_size()['heigth']
y1 = 1
# 0.93 0.99 屏幕右下角的位置开始
x1 = x*0.93
y2 = x*0.99
driver.swipe(x1,y1,x1,y2)
sleep(1)
driver.find_element_by_id('com.android.systemui:id/delete').click() #点击清空信息通知按钮
driver.find_element_by_android_uiautomator('new UiSelector().text("获取验证码")').click()
sleep(15)
driver.swipe(x1,y1,x1,y2)
sleep(1)
Te = driver.find_element_by_id('android:id/text')
duanxinneirong = Te.text()  #获取短信内容
print('短信内容是：'+duanxinneirong)
# 拿到短信内容后，把状态栏拉回去 点击位置根据手机获取
driver.swipe(x1,y2,x1,y1)
# 截取验证码
yanzhengma = duanxinneirong[10,14]
print('短信验证码是：'+yanzhengma)

