# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by easyto

FILE: 07_切片和索引.py
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/11/8 下午12:00

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/11/8 下午12:00
"""


"""
    nsarray对象的内容可以通过索引或切片来访问和修改
    ndarray有三种可用的索引方法类型：字段访问、基本切片、高级索引
    基本切片是Python中基本切片概念到n维的扩展，通过将start， stop， step参数提供给内置的slice函数来构造一个Python slice对象
    切片还可以包含省略号(...)，用来选择元组的长度与数组的维度相同，如果在行位置使用省略号，它将返回包含行中元素的ndarray
"""

import numpy as np

# 以为Ndarray对象
array_first = np.arange(10)
slice_first = slice(2, 7, 2)
slice_second = array_first[2: 7: 2]

# 多为Ndarray对象
array_second = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 第二列的元素
slice_third = array_second[..., 1]
slice_forth = array_second[1, ...]
slice_fifth = array_second[..., 1: ]


print(array_first[slice_first], '\n', slice_second, '\n', array_second[2:], '\n', slice_third, '\n', slice_forth, '\n', slice_fifth)
