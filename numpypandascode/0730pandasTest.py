# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:22:50 2019

@author: zsy15
"""
import pandas as pd
import numpy as np

#pandas介绍

s = pd.Series([1,3,6,np.nan,44,1])
print(s)
'''
dates = pd.date_range('20190730',periods=3)
#print(dates)
df = pd.DataFrame(np.random.randn(3,4),index = dates,columns=['a','b','c','d'])#随机产生数据，行名是dates，列名是abcd
#print(df)
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
#print(df1)
df2 = pd.DataFrame({'a':1,
                    'b':pd.Timestamp('20190730'),
                    'c':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'd':np.array([3]*4,dtype='int32'),
                    'e':pd.Categorical(["test","train","test","train"]),
                    'f':'foo'})
#print(df2) 
#print(df2.dtypes)#输出每一列数据的类型
#print(df2.index)#行的序号
#print(df2.columns)#输出每一列的名字
#print(df2.describe())#运算出数据中数字的数据个数，平均值，最小值等数据
#print(df2.T)#转置
#print(df2.sort_index(axis=1,ascending=False))#行不变，列倒序输出
#print(df2.sort_index(axis=0,ascending=False))#列不变，行倒序输出
print(df2.sort_values(by='e'))
'''

#pandas选择数据
'''
dates = pd.date_range('20190730',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
#print(df['A'],df.A)#输出'A'这一列，且结果一样
#print(df[0:3],df['20190730':'20190801'])#都是输出0,1,2这三行数据
#select by lable:loc
#print(df.loc['20190730'])#以标签形式选择
#print(df.loc[:,['A','B']])#打印AB这两列所有行
#print(df.loc['20190730',['A','B']])#打印20190370这一行的AB的这两列
#select by position:iloc
#print(df.iloc[3,1])#第三行第一列的value
#print(df.iloc[[1,3,5],1:3])#第1,3,5行，1,2列
#mixed selection:ix
#print(df.ix[:3,['A','C']])#0-3行，A,C这两列的数据
#Boolean indexing
print(df)
print(df[df.C>8])#输出C这列大于8的数据
'''
#pandas设置值
'''
dates = pd.date_range('20190730',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
#df.iloc[2,2] = 1111#修改2行2列的值为1111,只能输入几行几列
#df.loc['20190730','C'] = 2222，输入具体的哪一行那一列
#df.A[df.C>20] = 0#对于C这一列大于20的，在A中改为0
#df['F'] = np.nan#新增一列
df['E'] = pd.Series([1,2,3,4,5,6],index=dates)#新增一列
print(df) 
'''

#pandas处理丢失数据
'''
dates = pd.date_range('20190730',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
#print(df.dropna(axis = 0,how = 'any'))#某一行有nan，删除
#print(df.fillna(value=0))#将0填充进nan的位置
#print(df.isnull())#是nan则显示true，不是则为false
print(np.any(df.isnull())== True)#判断是否有nan
'''

#pandas 导入导出
'''
#可视化看数据用csv格式，把数据存储为csv格式
data = pd.read_csv('xxx.csv')#读取
print(data)
data.to_pickle('xxx.pickle')#存储
'''

#pandas
#concatenating
'''
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['A','B','C','D'])
#print(df1)
#print(df2)
#print(df3)
res = pd.concat([df1,df2,df3],axis=0)#竖向合并
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)#重新排序的竖向合并
#print(res)
'''
#join,['inner','outer']

df4 = pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'],index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*2,columns=['B','C','D','E'],index=[2,3,4])
#print(df4)
#print(df5)
res = pd.concat([df4,df5],join='outer',ignore_index = True)#只保留两者都有的
res1 = df1.append([df2,df3],ignore_index=True)#竖向合并

s = pd.Series([1,2,3,4],index=['A','B','C','D'])#新创建一行数据
res2 = df1.append(s,ignore_index=True)
print(res)



#pandas 合并 merge
'''
left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})
#print(left)
#print(right)
res = pd.merge(left,right,on='key')#通过key列合并
print(res)

'''
#pandas plot画图
import matplotlib.pyplot as plt
#plot data
'''
#Series
data = pd.Series(np.random.randn(1000))
data = data.cumsum()#累加的过程

#DataFrame
data = pd.DataFrame(np.random.randn(1000,4),#1000个数据，4个属性
                    index=np.arange(1000),
                    columns=['A','B','C','D'])
data = data.cumsum()
print(data.head())#默认输出前5个数据
#plot methods:
#'bar','hist','box','kde','area','scatter','hexbin','pie'
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')

data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)
plt.show()#显示

'''



