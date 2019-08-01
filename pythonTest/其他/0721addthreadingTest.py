# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:46:31 2019

@author: zsy15
"""
'''
import threading
import time
def thread_job():#定义添加的线程的工作
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')
def thread_job1():
    print('T2 start\n')
    print('T2 finish\n')
def main():
    add_thread = threading.Thread(target = thread_job)#添加线程 
    add_thread2 = threading.Thread(target = thread_job1)
    add_thread.start()#运行线程
    
    add_thread2.start()
    add_thread.join()
    add_thread2.join()
    print('all done')
#    print(threading.active_count())#查出激活线程的数目
#    print(threading.enumerate())#查看激活线程的名字
#    print(threading.current_thread())#查看正在运行程序用到的线程
if __name__ == '__main__':
    main()
 
'''

#queue功能
   
import threading 
import time
from queue import Queue
def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)

def multithreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[5,6,5],[6,9,8]]
    for i in range(4):
        t = threading.Thread(target = job,args = (data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)
        
if __name__ == '__main__':
    multithreading()








































