from appium import webdriver

class InitDriver():


    #[ro.build.version.release]: [5.1]
    #[ro.product.model]: [vivo X6D]
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 平台
        desired_caps['platformVersion'] = '8.0'  # 手机版本
        desired_caps['deviceName'] = 'vivo'  # 设备名称
        # desired_caps['platformVersion'] = '25'
        desired_caps['app'] = '/Users/monkey/Downloads/file/Automatic_UFO_1/Data/ufo.apk'
        desired_caps['appPackage'] = 'ufovpn.free.unblock.proxy.vpn'
        desired_caps['appActivity'] = 'ufovpn.free.unblock.proxy.vpn.home.ui.WelcomeActivity'
        desired_caps['noReset'] = True
        desired_caps['autoLaunch'] = True
        # desired_caps['automationName'] = "UiAutomator2"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def getServer(self):
       return self.driver

if __name__ == '__main__':
    s = InitDriver()
    s.getServer()


