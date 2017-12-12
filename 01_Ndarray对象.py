# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by easyto

FILE: 
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/11/4 下午2:44

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/11/4 下午2:44
"""


import numpy as np


def Ndarray(object, dtype=None, copy=True, order=None, subok=False, ndmin=0):
    """

    :param object: 任何暴露数组接口方法的对象都会返回一个数组或任何（嵌套）序列
    :param dtype: 数组的所需数据类型（可选）
    :param copy: 对象是够被复制，默认True（可选）
    :param order: C（按行）、F（按列）、A（任意， 默认）
    :param subok: 默认情况下，返回的数组强制为基类数组，如果为True，则返回子类
    :param ndmin: 指定返回数组的最小维数
    :return:
    """
    pass


# 一维array
array_first = np.array([1, 2, 3])

# 二维array
array_second = np.array([[1, 2], [3, 4]])

# 最小维度
array_third = np.array([1, 2, 3, 4], ndmin=3)

# dtype参数
array_forth = np.array([1, 2, 3], dtype=complex)

print(array_first, '\n', array_second, '\n', array_third, '\n', array_forth)
