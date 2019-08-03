# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:41:35 2019

@author: zsy15
"""
import pandas as pd

'''
#求均值
data = pd.read_csv('data.csv')
def GetMean(data):
    sum = 0 #存储数据的总和
    length = len(data) #存储数据的长度
 #  print(length)
    for i in range(len(data)):
        #循环求和
        sum = sum + float(data.loc[i])
    if length != 0 :
        #返回均值
        print(sum/length)
    else:
        print('此数据无均值')
GetMean(data)

'''
#求方差
'''
data = pd.read_csv('data.csv')
def GetMean(data):
    sum = 0 #存储数据的总和
    length = len(data) #存储数据的长度
 #  print(length)
    for i in range(len(data)):
        #循环求和
        sum = sum + float(data.loc[i])
    if length != 0 :
        #返回均值
        return (sum/length)
    else:
        return ('此数据无均值')
def GetVar(data):
    "计算方差"
    average = GetMean(data) #得到均值
    length = len(data)
    variance = 0
    for j in range(len(data)):
        #首先计算各值与均值差值的平方和
        variance = variance + pow(float(data.loc[j]) - average,2)
    if length != 0:
        print(variance/length) 
    else:
        print('无标准差') 
GetMean(data)
GetVar(data)

'''












