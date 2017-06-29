# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'
from base.action import ElementActions
from page.pages import *
from test.steps import Steps
from utils import L
import time
import allure


@allure.feature("车辆业务测试")
class TestLogin:
    pass
    # @allure.testcase("绑定车辆成功测试")
    # def test_login_empty_password(self, action: ElementActions):
    #     vin_box=Steps.get_vin_box()
    #     action.click(HomePage.个人中心)
    #     action.sleep(1)
    #     action.click(MenuPage.我的车辆)
    #     action.sleep(1)
    #     action.text(AddVehcilePage.车架号,vin_box[0])
    #     time.sleep(5)
    #     action.click(AddVehcilePage.添加)
    #     time.sleep(5)
    #
    #     assert action.is_text_displayed('终端')

