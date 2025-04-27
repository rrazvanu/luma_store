from browser import Browser
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.order_placement_page import OrderPlacementPage

def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()
    context.order_placement_page = OrderPlacementPage()


def after_all(context):
    context.browser.close()
