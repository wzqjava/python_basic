#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 创建单例对象.py
# @Author: WangZhiQiang
# @Date  : 2018/6/4
# @Desc  :
class Student(object):
    __instance  = None

    def __new__(cls):
        if  cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance



a = Student()
print(id(a))    #id相同

b = Student()
print(id(b))