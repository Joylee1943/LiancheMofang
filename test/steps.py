# -*- coding: utf-8 -*-


__author__ = 'Mio4kon'
import allure

from utils import L
from utils.environment import Environment


class Steps:
    @staticmethod
    @allure.step(title="获取账号和密码")
    def get_account():
        account = Environment().get_inited_config().account_success
        pwd = Environment().get_inited_config().password_success
        L.d('账号:%s 密码 %s' % (account, pwd))
        return [account, pwd]
    @allure.step(title="获取车架号和终端号")
    def get_vin_box(self):
        vin=Environment().get_inited_config().vin_success
        box=Environment().get_inited_config().box_success
        L.d('车架号:%s 盒子号 %s' % (vin, box))
        return [vin, box]






