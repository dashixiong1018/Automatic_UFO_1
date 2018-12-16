from selenium.webdriver.common.by import By
from Page.basic_page import Basic_page
from Page.Init_driver import InitDriver
import unittest


class Login_page(Basic_page):
    # 进入侧栏
    Menu = (By.ID, 'ufovpn.free.unblock.proxy.vpn:id/btn_slide')
    SignPage = (By.ID, 'ufovpn.free.unblock.proxy.vpn:id/tv_sign')
    submitbtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/btn_sign')  # 提交button
    emailAddress = (By.ID, 'ufovpn.free.unblock.proxy.vpn:id/et_name')
    password = (By.ID, 'ufovpn.free.unblock.proxy.vpn:id/et_pwd')
    loginbtn = (By.ID, 'ufovpn.free.unblock.proxy.vpn:id/btn_sign')

    # 退出登录元素
    accountinfo = (By.ID, 'ufovpn.free.unblock.proxy.vpn:id/img_arrow')
    loginoubtn = (By.ID, 'ufovpn.free.unblock.proxy.vpn:id/tv_logout')

    #修改密码
    changepwd = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/item_change')
    Oldpwd = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/et_old')
    Newpwd = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/et_pwd')
    BacktoHomebtn =(By.ID,'ufovpn.free.unblock.proxy.vpn:id/tv_back')



    def enterLoginPage(self):
        self.find_element(*self.Menu).click()
        self.find_element(*self.SignPage).click()

    def enterInfoPage(self):
        self.find_element(*self.accountinfo).click()

    def loginAction(self, username, pwd):
        self.send_key(self.emailAddress, username)
        self.send_key(self.password, pwd)

    def loginBtnClick(self):
        self.find_element(*self.loginbtn).click()

    def logoutClick(self):
        #self.find_element(*self.accountinfo).click()
        self.find_element(*self.loginoubtn).click()

    def checkLogoutStates(self):
        if self.find_element(*self.SignPage):
            return True
        else:
            return False


    def changePassword(self,oldpwd,newpwd):
            try:
                self.find_element(*self.accountinfo).click()
            except:
                pass
            self.find_element(*self.changepwd).click()
            self.send_key(self.Oldpwd,oldpwd)
            self.send_key(self.Newpwd,newpwd)
            self.find_element(*self.submitbtn).click()
            self.find_element(*self.BacktoHomebtn).click()



