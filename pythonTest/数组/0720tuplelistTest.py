# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:22:09 2019

@author: zsy15
"""

#tuple元组 list列表
'''
a_tuple = (12,9,4,55,5,6,2)
another_tuple = 12,8,87,7,4,5
a_list = [56,89,4,6,8,7,32,5]
for content in another_tuple:
    print(content)
'''
'''
a_tuple = (2,6,3,5,9,8)
another_tuple = 2,6,3,5,9,8
a_list = [6,8,7,9,6,5]
for content in a_list:
    print(content)
for index in range(len(a_tuple)):#len:即a_list列表的长度，range(5)意思是从0到4
    print('index =',index,'num in list = ',a_tuple[index])
print(a_list[1]) 
''' 
'''
a = [2,6,9,8,4,3,2,77] 
#a.append(0)  #增添元素
#a.insert(1,0)#1表示增添元素的位置，0表示增添的元素
#a.remove(2)#直接删除掉第一次出现的某个值，而不是index(位置)
print(a[-1])#-1表示最后一位，因为没有-0
print(a[0:3])#0表示从0卡死，3表示前三位，即输出0，1,2位的元素
print(a[2:5])  
print(a.index(77))#打印出77这个元素的索引
print(a.count(2))#打印出2出现的次数
a.sort()#从大到小排序
print(a)
a.sort(reverse=True)#从小到大排序，默认reverse=False
print(a)
'''
'''
b = [2,6,9,8,7,2]
#b.append(0)
#b.insert(0,1)
#b.remove(2)
#print(b.index(9))
#print(b.count(2))
#b.sort()
#b.sort(reverse=True)
print(b[0:5])    
'''

#多维列表
'''
multi_dim_a = [[1,2,3],
               [2,3,4],
               [3,4,5]] 
print(multi_dim_a[0][0]) 
'''
a = [[1,2,3],
    [2,3,4],
    [3,4,5]] 
print(a[0][0])   
    
    
    
    
    
    
    
    
    
    