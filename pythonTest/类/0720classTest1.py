# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:45:54 2019

@author: zsy15
"""
'''
class Beautiful:#self必须加，不然会出错 init可以不固定值
    def __init__(self,name,price = 18,hight = 20):
        self.name = name
        self.p = price
        self.h = hight
    def add(self,x,y):
        result = x + y
        print(self.name)#函数内打印要加self
        print(result)
'''
'''
class Mark():
    def __init__(self,name,price):
        self.n = name
        self.p = price
        self.add(1,2)
    def add(self,x,y):
        result = x + y
        print(result)
'''
class dog():
    def __init__(self,name,age):
        self.n = name
        self.a = age
    def fun(self,x,y):
        result = x + y
        print(self.n)
        print(result)
    