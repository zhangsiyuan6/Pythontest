# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 08:42:15 2019

@author: zsy15
"""

import pickle

a_dict = {'a':5,'c':99,'b':[5,6],5:{9:5}}
file = open('example.pickle','wb')
pickle.dump(a_dict,file)
file.close()

file = open('example.pickle','rb')
a_dict1 = pickle.load(file)
file.close()
print(a_dict)





















