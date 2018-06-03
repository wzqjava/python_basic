#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 调用父类的两种方法.py
# @Author: WangZhiQiang
# @Date  : 2018/6/3
# @Desc  :
class Cat:
    def __init__(self,name):
        self.name = name
        self.collor = 'yello'
    def sayHello(self):
        print('----cat')


class BoSi:
    # def __init__(self,name):
        # 第一种  ???
        # Cat.__init__(self,name)
        #   第二种方法,两种都没有实现;
        # super().__init__(self,name)

    def sayHello(self):
        print('----BoSi')

bosi = BoSi('cata')
bosi.sayHello()