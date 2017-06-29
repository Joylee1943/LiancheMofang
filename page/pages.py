# -*- coding: utf-8 -*-
__author__ = 'Mio4kon'
from page import tools

pages = tools.parse()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class AddVehiclePage:
    输入车架号 = get_locater('AddVehiclePage', '输入车架号')
    添加 = get_locater('AddVehiclePage', '添加')

    
class HomePage:
    登录 = get_locater('HomePage', '登录')
    个人中心 = get_locater('HomePage', '个人中心')
    马上检测 = get_locater('HomePage', '马上检测')
    地图 = get_locater('HomePage', '地图')

    
class LoginPage:
    用户名 = get_locater('LoginPage', '用户名')
    密码 = get_locater('LoginPage', '密码')
    登录 = get_locater('LoginPage', '登录')
    找回密码 = get_locater('LoginPage', '找回密码')
    注册账号 = get_locater('LoginPage', '注册账号')

    
class MapPage:
    停车场 = get_locater('MapPage', '停车场')
    洗车 = get_locater('MapPage', '洗车')
    维修 = get_locater('MapPage', '维修')
    加油站 = get_locater('MapPage', '加油站')

    
class MenuPage:
    个人中心 = get_locater('MenuPage', '个人中心')
    注销 = get_locater('MenuPage', '注销')
    我的车辆 = get_locater('MenuPage', '我的车辆')
    确定 = get_locater('MenuPage', '确定')
    取消 = get_locater('MenuPage', '取消')

    
class RegistPage:
    手机号 = get_locater('RegistPage', '手机号')
    获取验证码 = get_locater('RegistPage', '获取验证码')
    验证码 = get_locater('RegistPage', '验证码')
    密码 = get_locater('RegistPage', '密码')
    确认密码 = get_locater('RegistPage', '确认密码')
    提交 = get_locater('RegistPage', '提交')
    返回 = get_locater('RegistPage', '返回')

    
class UserInfoPage:
    个人中心 = get_locater('UserInfoPage', '个人中心')
    昵称 = get_locater('UserInfoPage', '昵称')

    



