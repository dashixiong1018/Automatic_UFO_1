from Page.Login_Page import *
import logging


class menu_Page(Basic_page):

    #进入侧栏
    Menu = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/btn_slide')
    Recommend = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/tv_recommend')
    Translate = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/item_language')
    HelpCenter = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/item_help')
    Feedback = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/item_feedback')
    InviteFriends = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/item_share')
    RateUFO = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/item_rate')
    AboutUFO = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/item_about')
    FB = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/like_fb')
    Ins = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/like_instagram')
    Telegrame = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/like_telegram')
    Logo = {By.ID, 'ufovpn.free.unblock.proxy.vpn:id/img_logo'}
    ShareUFObtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/img_pro_bg')
    Retweetbtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/btn_cta')
    Backbtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/btn_back')

    def enterMenupage(self):
        self.find_element(*self.Menu).click()

    def enterShareUFO(self):
        self.find_element(*self.ShareUFObtn).click()

    def checkSharePage(self):
        logging.info('check share UFO page')
        if self.find_element(*self.Retweetbtn):
            logging.info('enter share UFO page success')
            return True
        else:
            logging.info('enter share UFO page failed')
            self.get_current_activity_name()
            self.get_screenshot()
            return False

    def checkMenuPage(self):
        logging.info('check menu page')

        if self.find_element(*self.AboutUFO):
            logging.info('enter menu page success')
            return True
        else:
            logging.info('enter menu page page failed')
            self.get_current_activity_name()
            self.get_screenshot()
            return False

    def enterHelpTrans(self):
        self.find_element(*self.Translate).click()

    def enterHelpCenter(self):
        self.find_element(*self.HelpCenter).click()

    def enterFeedback(self):
        self.find_element(*self.Feedback).click()

    def enterInviteFriends(self):
        self.find_element(*self.InviteFriends).click()

    def enterRateUFO(self):
        self.find_element(*self.RateUFO).click()

    def enterAbout(self):
        self.find_element(*self.AboutUFO)

    def clickBackbtn(self):
        self.find_element(*self.Backbtn).click()