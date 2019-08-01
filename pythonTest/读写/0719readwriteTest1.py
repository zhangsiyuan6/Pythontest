# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:27:51 2019

@author: zsy15
"""
'''
appended_text = '\nThis is appended file.'
#print(text)
my_file = open('my file.txt','a')#a:appended
my_file.write(appended_text)
my_file.close()
'''

'''
text = 'This is aaa.\nThis is bbb.\nThis is ccc.'
her_file = open('her_file.txt','w')
her_file.write(text)
her_file.close()
'''
'''
text = 'wow'
his_file = open('his_file.txt','w')
his_file.write(text)
his_file.close()
'''
'''
appended_text = 'hi'
his_file = open('his_file.txt','a')
his_file.write(appended_text)
his_file.close()
'''
'''
appended_text = '\nibibibibiib.'
file = open('his_file.txt','a')
file.write(appended_text)
file.close()
'''
'''
file = open('my file.txt','r')
content = file.read()#将内容存放到content里
print(content)
'''
file = open('my file.txt','r')
content = file.readlines()#读所有内容到Excel
print(content)

 