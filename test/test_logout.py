# coding=utf-8
from base.action import ElementActions
from page.pages import *
from utils import L
import time
from test.test_home import login
import allure
from test.steps import Steps

@allure.feature("登录测试")
class TestLogin:
    pass
    # @allure.testcase("注销")
    # def t1est_logout(self, action: ElementActions):
    #     L.d('test_logout')
    #     time.sleep(5)
    #     #没有登录，先登录
    #     if action.is_text_displayed('登录'):
    #         account = Steps.get_account()
    #         login(account[0], account[1], action)
    #         action.sleep(20)
    #
    #     action.click(HomePage.个人中心)
    #     action.sleep(1)
    #     action.click(MenuPage.注销)
    #     action.sleep(1)
    #     action.click(MenuPage.确定)
    #     time.sleep(5)
    #     assert action.is_text_displayed('登录')