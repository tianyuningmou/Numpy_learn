# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by tianyuningmou

FILE:  10_在数组上的迭代.py
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/12/22 下午4:12

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/12/22 下午4:12
"""

import numpy as np

"""
    NumPy包包含一个迭代器对象numpy.nditer。它是一个有效的多维迭代器对象，可以用于在数组上进行迭代。数组的每个元素可使用Python的标准Iterator接口来访问
    如果两个数组是可广播的，nditer组合对象能够同时迭代它们。
"""

array_first = np.arange(0, 60, 5)
array_first = array_first.reshape(3, 4)
array_second = array_first.T
print('原始数组是：\n')
print(array_first)
print('\n')
print('原始数组的转置是：\n')
print(array_second)
print('\n')
print('修改后的数组是：(按C风格)\n')
for array_every in np.nditer(array_first, order='C'):
    print(array_every)
print('修改后的数组是：(按F风格)\n')
for array_every in np.nditer(array_first, order='F'):
    print(array_every)
