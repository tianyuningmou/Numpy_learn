# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by easyto

FILE: 
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/11/4 下午4:09

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/11/4 下午4:09
"""


import numpy as np


def array_attribute(shape, reshape, ndim, itemsize, flags):
    """
    
    :param shape:此属性返回一个包含数组维度的元组，它可以用于调整数组大小
    :param reshape:此函数用来调整数组大小
    :param ndim:此属性返回数组的维数
    :param itemsize:此属性返回数组中每个元素的字节单位长度
    :param flags:返回以下属性的当前值
              C_CONTIGUOUS(C)：数组位于单一的、C风格的连续区段内
              F_CONTIGUOUS(F)：数组位于单一的、Fortran风格的连续区段内
              OWNDATA(O)：数组的内存从其他对象处调用
              WRITEABLE(W)：数据区域可写入。将它设置为false会锁定数据，使其只读
              ALIGNED(A)：数据和任何元素会为硬件适当对齐
              UPDATEIFCOPY(U)：这个数组是另一个数组的副本，当这个数组释放时，源数组会由这个数组中的元素更新
    :return:
    """

# 调整数组大小
array_first = np.array([[1, 2, 3], [4, 5, 6]])
# array_first.shape = (3, 2)
array_second = array_first.reshape(3, 2)

arange_first = np.arange(24)
arange_second = arange_first.reshape(2, 4, 3)

# 数组的dtype为int8(一个字节)
array_third = np.array([1, 2, 3, 4, 5], dtype=np.float32)
array_forth = array_third

# print(array_first, '\n', array_second, '\n', arange_first, '\n', arange_first.ndim, '\n', arange_second)
print(array_third.itemsize, '\n', array_third.flags, '\n', array_forth.flags)
