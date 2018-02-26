# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: 14_IO文件操作.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/2/26 下午2:04

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/2/26 下午2:04
"""

"""
    ndarray对象可以保存到磁盘文件并从磁盘文件加载；可用的IO功能有：
        load()和save()函数处理numPy二进制文件(带npy扩展名)
        loadtxt()和savetxt()函数处理正常的文本文件
"""

import numpy as np
a = np.array([1,2,3,4,5])
b = np.load('outfile.npy')
print(b)
