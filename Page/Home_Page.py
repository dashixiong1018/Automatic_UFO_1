from selenium.webdriver.common.by import By
from Page.basic_page import Basic_page


class Home_Page(Basic_page):

    SmartLocationbtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/tv_smart')
    ChooseLocationbtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/tv_choose')
    Connectionbtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/btn_connect')
    Actionbtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/img_right')
    Connectionstate = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/tv_state')
    # Connectionstate = (By.NAME,'Click the button to connect')
    # Connectionstate = (By.NAME,'Click the button to disconnect')
    # Connectionstate = (By.NAME,'Connecting')
    ConnectionFailed = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/btn_i_know')
    Adbtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/ad_action')





