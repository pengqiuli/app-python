# -*-coding:gb18030-*-
# -*-coding:utf-8-*-
from base.activity import *
from time import sleep
import unittest

class test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 启动app
        cls.driver = desired_caps()
        sleep(4)
        cls.driver = jinrushouye(cls.driver)
        cls.driver = mainpage(cls.driver)
        log = login(cls.driver,"peng","peng123")

    def tearDownClass(cls) -> None:
        pass
