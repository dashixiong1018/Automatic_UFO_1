from Page.menu_Page import menu_Page
from Page.basic_page import *
import unittest


class test_enterMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = InitDriver().driver

    @classmethod
    def tearDownClass(cls):
        cls.driver =InitDriver(). driver.quit()
        # self.driver.close_app()

    # @retry()
    def test_ShareUFO(self):
        try:

            menuPage1 = menu_Page(self.driver)
            menuPage1.enterMenupage()
            menuPage1.checkMenuPage()
            menuPage1.enterShareUFO()
            menuPage1.clickBackbtn()

        except:
            pass

    def test_HelpCenter(self):
        try:
            menuPage = menu_Page(self.driver)
            menuPage.enterHelpCenter()
            menuPage.click_back_key()

        except:
            pass


if __name__ == "__main__":
    unittest.main()
