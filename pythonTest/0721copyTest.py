# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:21:48 2019

@author: zsy15
"""

#copy&deepcopy
import copy

'''
a = [1,2,3]
b = a #地址相同，改变a，b也跟着改变
a[0] = 0
print(a)
print(b)
b[0] = 1
print(a)
print(b)

c = copy.copy(a)#import的一个模块，浅复制，只第一层数组不共用
print(id(a)==id(c))
print(c)
c[0] = 222
print(a)
print(c)
'''

#copy只会复制父对象，而子对象是共用的；
'''
a = [1,2,[3,33]]
d = copy.copy(a)
print(id(a[2])==id(d[2]))
d[2][0] = 3333
print(d)
print(a)
d[0] = 0
print(a)
print(d)
'''
a = [1,2,[3,33]]
e = copy.deepcopy(a)#deepcopy完全复制所有的父子对象,不相互影响
print(id(a[2])==id(e[2]))
e[2][0] = 3333
print(e)
print(a)
e[0] = 0
print(a)
print(e)










