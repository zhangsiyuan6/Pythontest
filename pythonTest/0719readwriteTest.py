# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:27:51 2019

@author: zsy15
"""
text = 'This is my first line.\nThis is my second line.\nThis is my third line.'
#print(text)
my_file = open('my file.txt','w')
my_file.write(text)
my_file.close()
