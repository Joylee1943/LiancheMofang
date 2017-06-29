# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'
from base.action import ElementActions
from page.pages import *
from test.steps import Steps
from utils import L
import time,sys
import allure

#login_data=[('13701837591','','密码不能为空'),('13701837591','123456','密码格式错误')]

@allure.feature("登录测试")
class TestLogin:
    @allure.testcase("登录失败测试")
    def test_login_empty_password(self, action: ElementActions):
        account = Steps.get_account()
        time.sleep(20)
        action.swip_left(3)
        time.sleep(5)
        L.d('test_login_empty_password')
        L.i('账户{0},密码为空'.format(account[0]))
        action.click(HomePage.登录)
        login(account[0],"",action)
        action.sleep(5)
        try:
            assert action.is_text_displayed('密码能为空1')
        except Exception as e:
            action.save_failure_pic(sys._getframe().f_code.co_name)

    # def test_login_wrong_tpye_password(self, action: ElementActions):
    #     account = Steps.get_account()
    #     L.d('test_login_with_wrong_tpye_password')
    #     L.i('账户{0},密码为 123456'.format(account[0]))
    #     action.click(HomePage.登录)
    #     login(account[0], "123456",action)
    #     action.sleep(5)
    #     assert action.is_text_displayed('密码格式错误')
    #
    # def t1est_login_wrong_password(self, action: ElementActions):
    #     account = Steps.get_account()
    #     L.d('test_login_with_wrong_password')
    #     L.i('账户{0},密码为 a000000'.format(account[0]))
    #     action.click(HomePage.登录)
    #     login(account[0], "a000000",action)
    #     action.sleep(20)
    #     assert action.is_text_displayed('密码错误')
    #
    # @allure.testcase("登录成功")
    # def t1est_login_success(self, action: ElementActions):
    #     L.d('test_login')
    #     account = Steps.get_account()
    #     action.click(HomePage.登录)
    #     login(account[0],account[1],action)
    #     action.sleep(20)
    #     assert action.is_text_displayed('检测') or action.is_text_displayed("添加您的汽车")


def login(account, password,action: ElementActions):
    time.sleep(5)
    # action.driver.find_element_by_id('com.shautolinked.car:id/btnLeft').click()

    action.text(LoginPage.用户名, account,clear_first=True)
    action.text(LoginPage.密码, password,clear_first=True)
    action.sleep(1)
    action.click(LoginPage.登录)