from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base.activity import *
from time import sleep

def find_element(driver,ele_type,value):
    ele = None
    try:
        if ele_type == "id":
            # WebDriverWait(driver,5).until(lambda driver:driver.find_element_by_id(value))
            ele = driver.find_element_by_id(value)
        elif ele_type == "name":
            # WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_name(value))
            ele = driver.find_element_by_name(value)
        elif ele_type == "link_text":
            # WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_link_text(value))
            ele = driver.find_element_by_link_text(value)
        elif ele_type == "partial_link_text":
            # WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_partial_link_text(value))
            ele = driver.find_element_by_partial_link_text(value)
        elif ele_type == "tag_name":
            # WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_tag_name(value))
            ele = driver.find_element_by_tag_name(value)
        elif ele_type == "xpath":
            # WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(value))
            ele = driver.find_element_by_xpath(value)
        elif ele_type == "class_name":
            # WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_class_name(value))
            ele = driver.find_element_by_class_name(value)
    except ele_type as e:
        print("没有这种元素定位方式".format(e))


