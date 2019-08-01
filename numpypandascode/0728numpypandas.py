# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 22:40:09 2019

@author: zsy15
"""
import numpy as np
'''
array = np.array([[6,9,8],
                  [5,6,8]])
print('number of dim',array.ndim)#维度
print('shape',array.shape)#几行几列
print('size',array.size)#总共有多少元素

#numpy的创建array


array = np.array([[6,9,8],
                  [5,6,8]])#生成2行3列的矩阵
print(array)
array1 = np.zeros((1,2))#要填写shape，也就是几行几列
array2 = np.ones((1,2))
print(array1) 
print(array2)
'''
'''
a = np.arange(10,20,2)#生成一个10-20的有序数列，步长为2
b = np.arange(9).reshape((3,3))#生成一个0-15，共16个数字的矩阵，四行四列
c = np.linspace(1,10,5)#生成从1-10的线段，分成5段
d = np.linspace(1,10,6).reshape((2,3))
#上面先把1-10分为6段，再生成2行3列的矩阵
print(a) 
print(b) 
print(c) 
print(d) 
'''
#numpy的基础运算
'''
a = np.array([10,20,30,40])
b = np.arange(5,13,2)
#print(a,b)
#c = a + b#逐位相加
#c = b**2#逐位的平方
#c = np.sin(a)#逐位求a各元素的正弦
#print(b<9)#判断b的各个元素是否小于9，输出结果为true/false
#print(b==9)#判断b的哪个元素等于9，输出结果为true/false

d = np.array([[1,2],
              [3,4]])
e = np.arange(4).reshape((2,2))
f = d*e#矩阵各个位相乘
g_dot = np.dot(d,e)#矩阵乘法
g_dot2 = d.dot(e)
print(d)
print(e)
print(g_dot)
print(g_dot2)
'''

'''
a = np.random.random((2,2))#生成一个2行2列的随机矩阵
b = np.array([[1,2],
              [2,1]])
print(a)               #1是行，0是列
print(np.sum(b,axis=1))#每一行的数字相加
print(np.max(a,axis=0))#每一列的最大值
print(np.min(a))
'''
'''
A = np.arange(0,4).reshape((2,2))

print(A)


print(np.argmax(A))#最大值的索引
print(np.argmin(A))#最小值的索引
print(np.mean(A))#求平均数
print(np.average(A))#求平均数,这两种方式都可以
print(np.median(A))#求中位数(排序后中间两个数的平均数就是中位数)
print(np.cumsum(A))#逐位累加(第一个数是第一位，第二个数是前两个数相加，第三个数是前三个数相加，类推)
print(np.diff(A))#每相邻两个数的差

#print(np.nonzero(A))#输出不是0的元素位置
#print(np.sort(A))#对每一行进行从小到大排序
print(np.transpose(A))#转置
print(A.dot(A.T))#转置
print(np.clip(A,1,2))#对于A矩阵，小于1的数变为1，大于2得数变为2，其余不变
print(np.average(A,axis=1))#行的平均数

'''
'''
#numpy的索引
a = np.arange(3,15).reshape((3,4))
print(a)
print(a[2][2])#输出第2行第2列的元素
#print(a[1,1:3])#输出矩阵第1行，1-3位元素
#print(a.T)
for row in a:#输出每一行
    print(row)

'''
#numpy的合并
'''
a = np.array([1,1,1])[:,np.newaxis]#列上增加一个维度，成为矩阵
#a = np.array([1,1,1])[np.newaxis,:]#行上增加一个维度，成为矩阵
b = np.array([2,2,2])[:,np.newaxis]
#print(np.vstack((a,b)))#上下合并
#print(np.hstack((a,b)))#左右合并
c = np.concatenate((a,b,b,a),axis = 1)#行向合并,行不变，列增加
d = np.concatenate((a,b,b,a),axis = 0)#列向合并，列不变，行增加
print(c)
print(d)

'''

#numpy的array分割
'''
a = np.arange(12).reshape(3,4)
print(a)

#print(np.split(a,2,axis = 1))#行向分割为2块，行不变，列减少
#print(np.split(a,3,axis = 0))#列向分割为3块，列不变，行减少
print(np.vsplit(a,3))#列向分割为3块
print(np.hsplit(a,2))#行向分割为2块

'''

#numpy的copy&deep copy

a = np.arange(4)

'''
print(a)
b = a 
c = a
d = b
a[0] = 5
print(b)
b[0] = 6
print(a)
d[0] = 8
print(a)
'''
e = a.copy()  #deep copy：只复制a的值
print(e)
e[0] = 5
print(a)












