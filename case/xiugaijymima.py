from base.activity import *
from time import sleep
import unittest

class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 启动app
        cls.driver = desired_caps()
        sleep(4)
        cls.driver = jinrushouye(cls.driver)
        cls.driver = mainpage(cls.driver)
        log = login(cls.driver,"plm123","plm123")
        sleep(6)
        el = cls.driver.find_element_by_accessibility_id("交易密码\n重置").click()

    @classmethod
    def tearDownClass(cls) -> None:
        pass