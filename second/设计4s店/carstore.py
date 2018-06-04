#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : carstore.py
# @Author: WangZhiQiang
# @Date  : 2018/6/4
# @Desc  :
class CareStore(object):

    def __init__(self):
        self.factory = Factory()

    def order(self,type):
        return self.factory.select_car_by_type(type)


class Factory(object):
    def select_car_by_type(self, type):
        if type == "路虎":
            return LuHu()


class Car(object):

    def move(self):
        print("车在移动....")

    def music(self):
        print("正在播放音乐....")

    def stop(self):
        print("车在停止....")

class LuHu(Car):
    pass

car_store = CareStore()
car = car_store.order('路虎')
car.move()
car.music()
car.stop()