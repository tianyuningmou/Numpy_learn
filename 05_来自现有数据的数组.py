# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by tianyuningmou

FILE: 
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/11/8 上午10:15

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/11/8 上午10:15
"""


import numpy as np


def array_attribute(asarray, frombuffer, fromiter):
    """

    :param asarray: 类似于array， 用于将python序列转换为ndarray。接受以下参数构造函数
               a:任意形式的输入参数，比如列表、列表的元组、元组、元组的元组、元组的列表
               dtype:输入数据的类型会应用到返回的ndarray
               order:'C'按行的C风格数组，'F'按列的Fortran风格数组
    :param frombuffer:此函数将缓冲区解释为一维数组，暴露缓冲区接口的任何对象都用作参数来返回ndarray。接受以下参数构造函数
               buffer:任意暴露缓冲区接口的对象
               dtype:返回数组的数据类型，默认为float
               count:需要读取的数据数量，默认为-1，读取所有数据
               offset:需要读取的起始位置，默认为0
    :param fromiter:此函数从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组。接受以下参数构造函数
               iterable:任何可迭代对象
               dtype:返回数组的数据类型
               count:需要读取的数据变量，默认为-1，读取全部数据
    :return:
    """

# 将列表转换成ndarray
list_first = [1, 2, 3]
array_first = np.asarray(list_first)
array_second = np.asarray(list_first, dtype=float)

# 将元组转换成adarray
tuple_first = (1, 2, 3)
array_third = np.asarray(tuple_first)

# 来自元组列表的ndarray
array_tuple = [(1, 2, 3), (4, 5)]
array_forth = np.asarray(array_tuple)

# frombuffer的用法
str_first = 'Hello world'.encode(encoding='utf-8')
array_sixth = np.frombuffer(str_first, dtype='S1')

# fromiter的用法
list_second = range(5)
iter_second = iter(list_second)
array_seventh = np.fromiter(iter_second, dtype=float)

print(array_first, '\n', array_second, '\n', array_third, '\n', array_forth, '\n', array_sixth, '\n', array_seventh)
