#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 烤地瓜.py
# @Author: WangZhiQiang
# @Date  : 2018/6/3
# @Desc  :
class SweetPotato:

    def __init__(self):
       self.level = 0
       self.cookedString='生的'
       self.condiments=[]

    def __str__(self):

        msg = self.cookedString + '地瓜'
        num =len(self.condiments)
        print(num)
        if( num> 0):
            msg = msg + '('
            for temp in self.condiments:
                msg = msg + temp+','
            msg = msg.strip(',')
            msg = msg+')'

        return msg



        return  msg

    def cook(self,time):
        self.level +=time
        if self.level>8:
            self.cookedString = '烤成灰了'
        elif(self.level>5):
                self.cookedString = '烤熟了'
        elif(self.level>5):
            self.cookedString = '烤熟了'
        elif(self.level>3):
            self.cookedString = '半生不熟'
        else:
            self.cookedString = '生的'

    def addCondiments(self,temp):
        self.condiments.append(temp)


potato = SweetPotato()
potato.cook(2)
print(potato)


potato.cook(5)
potato.addCondiments('油')
print(potato)



