# -*- coding: utf-8 -*-

"""
Copyright () 2017

All rights reserved by tianyuningmou

FILE: 
AUTHOR:  tianyuningmou
DATE CREATED:  @Time : 2017/11/4 下午3:00

DESCRIPTION:  .

VERSION: : #1 $
CHANGED By: : tianyuningmou $
CHANGE:  :  $
MODIFIED: : @Time : 2017/11/4 下午3:00
"""


import numpy as np


def data_type(bool, int_, intc, intp, int8, int16, int32, int64, uint8, uint16, uint32, uint64, float_, float16, float32, float64, complex_, complex64, complex128):
    """

    :param bool: 存储一个字节的布尔值（真/假）
    :param int_: 默认整数，相当于C的long，通常为int32或int64
    :param intc: 相当于C的int， 通常为int32或int64
    :param intp: 用于索引的整数，相当于C的size_t，通常为int32或int64
    :param int8: 字节（-128~127）
    :param int16: 16位整数（-32768~32767）
    :param int32: 32位整数（-2147483648~2147483647）
    :param int64: 64位整数（-9223372036854775808~9223372036854775807）
    :param uint8: 8位无符号整数（0~255）
    :param uint16:16无符号整数（0~65535）
    :param uint32:32位无符号整数（0~4294967295）
    :param uint64:64位无符号整数（0~1818446744073709551615）
    :param float_:float64的简写
    :param float16:半精度浮点：符号位、5位指数、10位尾数
    :param float32:单精度浮点：符号位、8位指数、23位尾数
    :param float64:双精度浮点：符号位、11位指数、52位尾数
    :param complex_:complex128的简写
    :param complex64:复数，由两个32位浮点表示
    :param complex128:复数，由两个64位浮点表示
    :return:
    """


"""   
    数据类型对象描述了对应于数组的固定内存块的解释，取决于以下方面：
      1.数据类型（整数、浮点或者Python对象）
      2.数据大小
      3.字节序（小端或大端）
      4.在结构化类型的情况下，字段的名称，每个字段的数据类型，和每个字段占用的内存块部分
      5.如果数据类型是子序列，它的形状和数据类型
"""


def dtype(object, align, copy):
    """

    :param object: 被转换为数据类型的对象
    :param align: 如果为True， 则向字段添加间隔，使其类似C地结构体
    :param copy: True：生成dtype对象的新副本；False， 结果是内建数据类型对象的引用
    :return:
    """


# 使用数组标量类型
dt_first = np.dtype(np.int32)

# int8， int16， int32， int64可替换为等价的字符串'i1', 'i2'，'i4'，'i8'等
dt_second = np.dtype('i8')

# 使用端记号
dt_third = np.dtype('>i4')

# 将dtype应用于ndarray对象
dt_forth = np.dtype([('age', np.int8)])
array_forth = np.array([(10, ), (20, ), (30, )], dtype=dt_forth)


# 文件名称用于访问age列的内容
result = array_forth['age']


print(dt_first, '\n', dt_second, '\n', dt_third, '\n', array_forth, '\n', result)
