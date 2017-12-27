# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by tianyuningmou

FILE: 08_高级索引.py
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/11/8 下午12:24

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/11/8 下午12:24
"""


"""
    如果一个Ndarray是非元组序列，数据类型为整数或布尔值的Ndarray，或者至少一个元素为序列对象的元组，我们就能够用它来索引Ndarray。高级索引
    始终返回数据的副本，与此相反，切片只提供了一个视图
    整数索引：这种机制有助于基于N维索引来获取数组中任意元素。每个整数数组表示该维度的下标值。当索引的元素个数就是目标Ndarray的维度时，会变得相当直接
        高级和基本索引都可以通过使用切片或省略号与索引数组组合。
        当切片用于两者时，结果是相同的，但高级索引会导致复制，并且可能有不同的内存布局
    布尔索引：当结果对象是布尔运算的结果时，将使用此类型的高级索引
"""


import numpy as np


array_first = np.array([[1, 2], [3, 4], [5, 6]])
array_second = array_first[[0 ,1, 2], [0, 1, 0]]

array_third = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
rows = np.array([[0, 0], [3, 3]])
clos = np.array([[0, 2], [0, 2]])
array_forth = array_third[rows, clos]

# 切片
array_fifth = array_third[1:4, 0:3]
# 对列使用高级索引
array_sixth = array_third[1:4, [0, 1, 2]]

# 布尔运算
array_seventh = array_third[array_third > 5]

array_eighth = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])


print(array_second, '\n', array_forth, '\n', array_fifth, '\n', array_sixth, '\n', array_seventh, '\n', array_eighth[~np.isnan(array_eighth)])
