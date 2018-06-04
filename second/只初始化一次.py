#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 创建单例对象.py
# @Author: WangZhiQiang
# @Date  : 2018/6/4
# @Desc  :
class Dog(object):
    __instance  = None
    __flag_init = False
    def __new__(cls,name):

        if  cls.__instance == None:
            cls.__instance = object.__new__(cls)

            return cls.__instance
        else:
            return cls.__instance

    def __init__(self,name):
        if Dog.__flag_init == False:
            self.name = name
            Dog.__flag_init = True


a = Dog('a')
print(id(a))    #id相同
print(a.name)

b = Dog('b')    # 初始化一次,无法在改变对象的名字
print(id(b))
print(b.name)