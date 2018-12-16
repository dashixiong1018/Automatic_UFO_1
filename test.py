# -*- coding: utf-8 -*-
from appium import webdriver
import os,time


desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platformVersion': '5.1',
        'appPackage': 'com.pujiadev.LegacyCostCHN',
        'appActivity': 'com.pujiadev.LegacyCostCHN.SplashActivity',
        'noReset': True,
        'autoLaunch':True
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)


def getRXP():

    try:

        X = driver.get_window_size()['width']
        Y = driver.get_window_size()['height']

        driver.launch_app()
        time.sleep(6)
        # os.system('adb shell am start com.android.settings/.Settings')
        driver.tap((520/X)*X,(840/Y)*Y)#点击金币
        driver.tap((930/X)*X,(666/Y)*Y)#点击经验

        driver.find_element_by_class_name('android.widget.ImageView')
        time.sleep(35)
        driver.find_element_by_id('com.pujiadev.LegacyCostCHN:id/material_dialog_btn_p').click()
        driver.tap((520/X)*X,(840/Y)*Y)  #经验ok
        # driver.tap((540/X)*X,(1280/Y)*Y)#经验关闭
        driver.tap((886/X)*X,(147/Y)*Y)#获取宝珠
        driver.tap((484/X)*X,(900/Y)*Y)#观看广告

        time.sleep(35)

        driver.find_element_by_class_name('android.widget.ImageView')
        driver.find_element_by_id('com.pujiadev.LegacyCostCHN:id/material_dialog_btn_n').click()

        driver.close()
        driver.start_activity('com.android.settings','.Settings')

    except:
        pass

if __name__ == '__main__':
    getRXP()


