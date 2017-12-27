# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by tianyuningmou

FILE: 
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/11/7 下午3:39

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/11/7 下午3:39
"""


import numpy as np


def array_attribute(empty, zeros, ones):
    """

    :param empty:用来创建指定形状和dtype的未初始化数据，使用以下属性构造函数
              shape：空数组的形状，整数或整数元组
              dtype：所需的输出数组类型，可选
              order：'C'为按行的C风格数组， 'F'为按列的Fortran风格数组
    :param zeros:返回特定大小，以0填充的新数组，使用以上属性构造函数
    :param ones:返回特定大小，以1填充的新数组，使用以上属性构造函数
    :return:
    """


array_first = np.empty([3, 2], dtype=int)

array_second = np.zeros(5)

array_third = np.zeros((5, ), dtype=np.int)

array_forth = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])

array_fifth = np.ones(5)

array_sixth = np.ones([2, 2], dtype=int)

print(array_first, '\n', array_second, '\n', array_third, '\n', array_forth, '\n', array_fifth, '\n', array_sixth)
