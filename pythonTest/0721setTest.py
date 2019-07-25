# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:41:00 2019

@author: zsy15
"""
'''
#set :找出数列中重复的元素并删除
#和字典一样，无序输出;set里只能传一个列表

char_list = ['a','b','c','a','d','d']
sen = 'Welcome back to this country'
#print(set(sen))
unique_char = set(char_list)
unique_char.add('x')#只能单独加一个
#unique_char.clear()#清空
#unique_char.remove('a' )
#print(unique_char)
set2 = {'a','e','i'}
print(unique_char.difference(set2))#差集（不同的）
print(unique_char.intersection(set2))#交集（相同的）
'''




































