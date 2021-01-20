from appium import webdriver
from base.activity import *
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

driver = desired_caps()
sleep(4)
driver = jinrushouye(driver)
driver = mainpage(driver)
el2 = driver.find_element_by_accessibility_id("忘记用户名")
el2.click()
sleep(1)
# 控件内滑动，目前在网上没有找到比较好的解决方法，只能先用笨方法
el = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]").click()
sleep(1)
TouchAction(driver).press(x=134, y=1212).move_to(x=138, y=1125).release().perform()

