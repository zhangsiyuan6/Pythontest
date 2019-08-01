# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:35:50 2019

@author: zsy15
"""

import matplotlib.pyplot as plt
import numpy as np
#基本用法

x = np.linspace(-1,1,50)
y = 2*x + 1
plt.plot(x,y)
plt.show()


#figure图像
'''
x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2
#plt.figure()#不用figure两图在同一坐标轴中
plt.plot(x,y1,color = 'red',linewidth=3.0,linestyle='--')#设置线的颜色，宽度，和形式
#plt.figure()
plt.plot(x,y2,color = 'green',linewidth=3.0,linestyle='--')
plt.show()
'''
#设置坐标轴
'''
x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2
#plt.figure()
plt.plot(x,y1,color = 'red',linewidth=3.0)#设置线的颜色，宽度，和形式(linestyle)0
plt.plot(x,y2,color = 'green',linewidth=3.0)
plt.xlim((-1,2))#x轴取值范围
plt.ylim((-2,3))#y轴取值范围
plt.xlabel('i am x') 
plt.ylabel('i am y')
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)#设置x轴间距
plt.yticks([-2,-1.8,-1,1.22,3,],
            [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])#一个数字对应一个名字,前后加$变成斜体，空格前必须加\才能被识别,\alpha等于α

#gca = 'get current axis'#把现在的轴拿出来
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#将底部的轴设置成x轴
ax.yaxis.set_ticks_position('left')#将左边的轴设置成y轴
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.show()
'''
#legend图例
'''
x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2
plt.xlim((-1,2))#x轴取值范围
plt.ylim((-2,3))#y轴取值范围
plt.xlabel('i am x') 
plt.ylabel('i am y')
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)#设置x轴间距
plt.yticks([-2,-1.8,-1,1.22,3,],
            [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])#一个数字对应一个名字,前后加$变成斜体，空格前必须加\才能被识别,\alpha等于α


plt.plot(x,y1,color = 'red',linewidth=3.0,label='down')#设置线的颜色，宽度，和形式(linestyle)0
plt.plot(x,y2,color = 'green',linewidth=3.0,linestyle='--',label='up')

#plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')#loc表示自动找比较合适的地方放置，handles是需要放置legend的线，labels线的名字
plt.legend()
plt.show()

'''

#annotation标注
'''
x = np.linspace(-3,3,50)
y1 = 2*x + 1
plt.plot(x,y1,color = 'red',linewidth=3.0)#设置线的颜色，宽度，和形式(linestyle)0

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

x0 = 1
y0 = 2*x0 +1
plt.scatter(x0,y0,s=50,color='b')#散点图
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)#生成一条线
plt.annotate(r'$2x+1=%s$' %y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),
             textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
plt.text(-3.7,3,r'$This\ is\ the\ text.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})
plt.show()
'''

#tick能见度
'''
x = np.linspace(-3,3,50)
y1 = 2*x + 1
plt.plot(x,y1,color = 'red',linewidth=10.0,zorder=1)#设置线的颜色，宽度，和形式(linestyle)0

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_zorder(2)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.9))#设置坐标颜色，边框颜色，透明度
    
plt.show()
'''
#scatter散点图
'''
n=1024
X = np.random.normal(0,1,n)#随机生成
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)#随机生成颜色
plt.scatter(X,Y,c=T,alpha=0.5)
#plt.scatter(np.arange(5),np.arange(5))#一条直线的散点图

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(())#把坐标消除
plt.yticks(())
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
plt.show()
'''


















