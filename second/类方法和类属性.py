#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 类方法和类属性.py
# @Author: WangZhiQiang
# @Date  : 2018/6/3
# @Desc  :
class People:
    country = 'china'

    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls,country):
        cls.country = country


p = People()
print(People.country)
print(p.getCountry())

p.setCountry('japan')
print(p.country)
print(p.getCountry())
