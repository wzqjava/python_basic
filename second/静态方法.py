#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 静态方法.py
# @Author: WangZhiQiang
# @Date  : 2018/6/3
# @Desc  :
class People:

    country = 'china'

    @staticmethod
    def getCountry():
        return People.country


print(People.getCountry())

