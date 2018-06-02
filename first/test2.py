#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test2.py
# @Author: WangZhiQiang
# @Date  : 2018/5/30
# @Desc  :

i = 1
total = 0
while i<101:
    if i%2==0:
        total+=i
    i += 1

print("toatal:%d"%total)