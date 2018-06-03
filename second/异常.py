#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 异常.py
# @Author: WangZhiQiang
# @Date  : 2018/6/3
# @Desc  :

try:
    num = 100;
    print(num)
except (NameError,IOError),errorMsg:
    print('抛出了异常%s'%errorMsg)
else:
    print('很开心,没有异常')
finally:
    print('我无论如何都执行到了')