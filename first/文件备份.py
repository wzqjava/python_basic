#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 文件备份.py
# @Author: Feng
# @Date  : 2018/5/30
# @Desc  : 文件备份

#   创建备份文件名字
oldFileName = raw_input('请输入要备份的文件名字:')
oldFile = open(oldFileName,'r')
if oldFile:
    #   获取文件类型
    numFlag = oldFileName.rfind('.')
    print("numFlag:%d"%numFlag)
    if(numFlag>0):
        flagName = oldFileName[numFlag:]
        print("flagName:%s"%flagName)
    #   创建新文件的名字
    old = oldFileName[:numFlag] #不包含numFlag这个下标的元素
    print("old:%s"%old)
    newFileName = old + "[复件]" + flagName
    newFile = open(newFileName,'w')
    oldContent = oldFile.readlines()

    #   写入新文件
    for c in oldContent:
        newFile.write(c)
    #关闭
    oldFile.close()
    newFile.close()
