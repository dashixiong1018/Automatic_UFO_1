from selenium.webdriver.common.by import By
from Page.basic_page import Basic_page


class menu_Page(Basic_page):

    #进入侧栏
    Search = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/tv_hint')
    Clearbtn = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/img_clear')
    SearchCancel = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/tv_cancel')
    DisplayCity = (By.ID,'ufovpn.free.unblock.proxy.vpn:id/img_arrow')
    Recommend = (By.NAME,'Recommend')
    All = (By.NAME,'All')