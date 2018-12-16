from time import sleep
from Page.Init_driver import InitDriver
from Page.Login_Page import Login_page
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = InitDriver().driver

    @classmethod
    def tearDownClass(cls):
       cls.driver = InitDriver().driver.quit()
        # self.driver.close_app()

    def test_1_login(self):
        ins_login = Login_page(self.driver)
        ins_login.enterLoginPage()
        ins_login.loginAction('18382342969@163.com','123456')
        ins_login.loginBtnClick()

    def test_2_changepassword(self):
        ins_log1 = Login_page(self.driver)
        ins_log1.changePassword('123456','1234567890')
        # self.assertEqual(ins_log1.checkChangePwdStates(), True)

    def test_3_changepasswordagain(self):
        ins_log = Login_page(self.driver)
        ins_log.changePassword('1234567890','123456')
        # self.assertEqua l(ins_log.checkChangePwdStates(),True)

    def test_4_logout(self):
        ins_logout = Login_page(self.driver)
        ins_logout.logoutClick()
        ins_logout.click_back_key()
        self.assertEqual(ins_logout.checkLogoutStates(),True)


if __name__ == "__main__":
    unittest.main()