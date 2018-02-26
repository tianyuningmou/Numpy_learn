# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: 11_数组操作.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/2/26 上午9:53

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/2/26 上午9:53
"""

"""
    Numpy中的几个关于数组操作的方法：
        reshape：不改变数据的情况下修改形状
        flat：数组上的一维迭代器
        flatten：返回折叠为一维的数组副本
        ravel：返回连续的展开数组
    Numpy中关于数组翻转的方法：
        transpose：翻转数组的纬度（转置）
        rollaxis：向后滚动指定的轴
        swapaxes：互换数组的两个轴
    Numpy中关于修改纬度的方法：
        broadcast：产生模仿广播的对象
        broadcast_to：将数组广播到新形状
        expand_dims：扩展数组的形状
        squeeze：从数组的形状中删除单维条目
    Numpy中关于数组连接的方法：
        concatenate：沿着现存的轴连接数据序列
        stack：沿着新轴连接数据序列
        hstack：水平堆叠序列中的数组
        vstack：竖直堆叠序列中的数组
    Numpy中关于数组分割的方法：
        split：将一个数组分割成多个子数组
        hsplit：将一个数组水平分割成多个子数组
        vsplit：将一个数组竖直分割成多个子数组
    Numpy中删除/添加元素的方法：
        resize：返回指定形状的新数组
        append：将值添加到数组末尾
        insert：沿指定轴将值插入到指定坐标之前
        delete：返回删掉某个轴的子数组的新数组
        unique：寻找数组内的唯一元素
"""

import numpy as np

array_one = np.zeros(3)
array_two = np.reshape(array_one, (3,1))
print(array_two)
