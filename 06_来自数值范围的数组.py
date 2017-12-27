# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by tianyuningmou

FILE: 06_来自数值范围的数组.py
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/11/8 上午11:32

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/11/8 上午11:32
"""


import numpy as np


def array_attribute(arange, linspace, logspace):
    """

    :param arange: 此函数返回ndarray对象，包含给定范围内的等间隔值。接受以下参数构造函数
              start:范围的起始值，默认为0
              stop:范围的终止值（不包含）
              step:两个值的间隔，默认为1
              dtype:返回ndarray的数据类型，如果没有，则会使用输入数据的类型
    :param linspace:此函数类似于arange()函数，此函数中指定了范围之间的均匀间隔数量。接受以下参数构造函数
              start:序列的起始值
              stop:序列的终止值，如果endpoint为true，该值包含于序列中
              num:要生成的等间隔样例数量，默认为50
              endpoint:序列中是否包含stop值，默认为true
              retstep:如果为true，返回样例，以及连续数字之间的步长
              dtype:输出ndarray的数据类型
    :param logspace:此函数返回一个ndarray对象，其中包含在对数刻度上均匀分布的数字，刻度的开始和结束端点是某个底数的幂，通常为10.接受以下参数构造函数
              start:起始值是base**start
              stop:终止值是base**stop
              num:范围内的数值数量，默认是50
              endpoint:如果是true，终止值包含在输出数组中
              base:对数空间的底数，默认是10
              dtype:输出数组的数据类型，如果没有提供，则取决于其他参数
    :return:
    """

# arange的用法
list_first = np.arange(5 ,dtype=float)
list_second = np.arange(10, 20, 2)

# linspace的用法
array_third = np.linspace(10, 20, 5)
array_forth = np.linspace(10, 20, 5, endpoint=False)
array_fifth = np.linspace(10, 20, 5, retstep=True)

# logspace的用法
array_sixth = np.logspace(1.0, 2.0, num=10)
array_seventh = np.logspace(1, 10, num=10, base=2)

print(list_first, '\n', list_second, '\n', array_third, '\n', array_forth, '\n', array_fifth, '\n', array_sixth, '\n', array_seventh)
