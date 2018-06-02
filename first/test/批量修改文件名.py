#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 批量修改文件名.py
# @Author: WangZhiQiang
# @Date  : 2018/6/2
# @Desc  :

import os

# 获取当前目录所有文件
list  = os.listdir('./')

#   循环修改
for name in list:
    #获取oldName

    os.rename(name,'_'+'oldName')


