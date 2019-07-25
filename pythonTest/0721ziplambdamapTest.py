# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 15:30:46 2019

@author: zsy15
"""

#zip
'''
a = [1,2,3]
b = [4,5,6]
print(list(zip(a,a,b)))#对应index的元素组成一个新数组
for i,j,k in zip(a,a,b):
    print(i/2,j*2,k*3)
   
a = [1,2,3]
b = [4,5,6]
print(list(zip(a,b)))
for i,j in zip(a,b):
    print(i/2,j*2)
'''
#lambda
'''
def fun(x,y):
    return(x+y)
print(fun(2,3))
'''
#fun1 = lambda x,y:x+y#定义比较简单的方程
#print(fun1(1,2))

#map
'''
print(list(map(fun1,[1],[2])))#将已知的功能函数与参数绑定在一起
#[1]是参数x，[2]是参数y
print(list(map(fun1,[1,2],[2,3])))#数组里index相同的数相加，组成新的数组
'''












































