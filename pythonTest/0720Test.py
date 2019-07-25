# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:46:39 2019

@author: zsy15
"""
'''
text = 'aaa\nbbb\nccc'
file = open('file.txt','w')
file.write(text)
file.close()
'''

'''
appended_text = '\nddd'#向file.txt里新增
file = open('file.txt','a')
file.write(appended_text)
file.close()
'''
'''
文本文件的读取
file = open('file.txt','r')
content = file.read()
print(content)
'''


file = open('file.txt','r')
content = file.readlines()
print(content)