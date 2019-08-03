# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:29:58 2019

@author: zsy15
"""

#距离相似度计算
'''
import numpy as np
p1 = np.array([1, 3, 4])
p2 = np.array([4, 2, 4])
# 或者
d = np.sqrt(np.sum(np.square(p1-p2)))#公式
print(d)
'''
#余弦相似度计算
import numpy as np
p1 = np.array([1, 3, 4])
p2 = np.array([4, 2, 4])
#np.linalg.norm()求矩阵的范数
d = np.dot(p1,p2)/(np.linalg.norm(p1)*(np.linalg.norm(p2)))#矩阵整体元素平方和开根号，不保留矩阵二维特性
print(d)
        
        
        
        
        
        
        
        
        
        
        
        