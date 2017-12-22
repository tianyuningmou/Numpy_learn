# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by easyto

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
"""

array_first = np.arange(0, 60, 5)
array_first = array_first.reshape(3, 4)

