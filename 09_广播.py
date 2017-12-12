# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by easyto

FILE: 09_广播.py
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/11/8 下午2:12

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/11/8 下午2:12
"""


"""
    广播：指Numpy在算术运算期间处理不同形状的数组的能力，对数组的算术运算通常在相应的元素上进行。如果两个阵列具有完全相同的形状，则这些操作被无缝执行
    如果两个数组的维数不相同，则元素到元素的操作是不可能的。然而，在Numpy中仍然可以对形状不相似的数组进行操作，因为它拥有广播功能，较小的
        数组会广播到较大数组的大小，以便使它们的形状可兼容
    如果满足以下规则，可以进行广播：
        1.ndim较小的数组会在前面追加一个长度为1的维度
        2.输出数组的每个维度的大小是输入数组该维度大小的最大值
        3.如果输入在每个维度中的大小与输出大小匹配，或其值正好为1
        4.
"""


import numpy as np


array_first = np.array([1, 2, 3, 4])
array_second = np.array([10, 20, 30, 40])
array_third = array_first * array_second

print(array_third)
