"""

import os
import unittest
from Page.basic_page import *
from appium import webdriver


class basic_unittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("--------------測試開始--------------")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 平台
        desired_caps['platformVersion'] = '7.1.1'  # 手机版本
        desired_caps['deviceName'] = 'vivo'  # 设备名称
        # desired_caps['platformVersion'] = '25'
        desired_caps['app'] = r'../Data/ufo.apk'
        desired_caps['appPackage'] = 'ufovpn.free.unblock.proxy.vpn'
        desired_caps['appActivity'] = 'ufovpn.free.unblock.proxy.vpn.home.ui.WelcomeActivity'
        desired_caps['noReset'] = True
        desired_caps['autoLaunch'] = False
        # desired_caps['automationName'] = "UiAutomator2"
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #cls.driver.find_element_by_accessibility_id()


    @classmethod
    def tearDownClass(cls):
        print("--------------測試結束--------------")
        time.sleep(3)
        cls.driver.quit()

"""