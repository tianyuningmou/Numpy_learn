# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: 12_位操作.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/2/26 下午12:08

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/2/26 下午12:08
"""

"""
    Numpy中的位操作：
        bitwise_and：对数组元素执行位与操作
        bitwise_or：对数组元素执行位或操作
        invert：计算位非
        left_shift：向左移动二进制表示的位
        right_shift：向右移动二进制表示的位
"""

import numpy as np
print(bin(13), bin(17))
print(np.bitwise_and(13, 17))
print(np.bitwise_or(13, 17))
