# -*- coding: utf-8 -*-

# list 列表

# classmates = ['Michael', 'Bob', 'Tracy']
# classmates.append('uuu')
# print(classmates)

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


# height = 1.75
# weight = 80.5
# s = (weight/height)**2
# print(s)

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name,names)
# x =list( range(5))
# print(x,range(2))

# sum = 0
# print(range(101),888)
# for x in range(101):
#     sum = sum + x
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print('Hello, '+name)

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# d['Michael'] = 100
# print(d)

# a = input()
# a = int(a)
# if a < 100:
#     print('小于100')
# else:
#     print('大于100')


# list

# listData = ['a', 'b', 'c']

# for a in listData:
#     print(a)
#  list 列表 [1,2,3,4,5] tuple 元组（1,2,3,4,5）
# sum = 0
# sumList = [1,2,3,4,5,6]
# for index in sumList:
#     sum += index
# print(sum)
# tuple 元组
# names1 = {1,2,3,4}

# list 列表
# names = [{'Michael1': 195},{'Michael2': 295},{'Michael3': 395},{'Michael4': 495}]
# print(len(names))
# 字典 dict 对象
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d['Adam'] = 67
# print(d.get('Michaefdl'))
# set
# a = set([1,1,5,6,2,4,2,3,4,5])
# print(a)

# a = '22a'

# print(abs(a))
# list 列表
# a = [1,2,3,4,5]

# tuple 元组
# b = (1,2,3,4,5,6)

# print(max(a),max(b))

# def my_abs(x):
#     if x <=200:
#         return x
#     else:
#         return -x

# print(my_abs(-500))

# def power(x,n):
#     s = 1
#     for item in range(n):
#         s = s * x
#     return s

# print(power(2,3))

# def add_end(l = None):
#     if l is None:
#         l = []
#     l.append('END')
#     return l
# print(add_end(['12']))
# print(add_end(['13']))
# print(add_end(['14']))

# def calc(*numbers):
#     sum = 0
#     for name in numbers:
#         sum = sum + name*name
#     return sum
# sums = [1,2,3]
# sums1 = [1,2,3,3,4]
# print(calc(*sums))
# print(calc(*sums1))


# def person(name,age,**kw):
#     print('name:', name, 'age:', age, 'other:', kw)
# print(person(1,2,city='chongqing'))
# 递归
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)

# print(fact(3))


# def add():
#     l = []
#     n = 1
#     while n <= 99:
#         l.append(n)
#         n = n + 2
#     print(l,99)
# print(add())
# 切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print(L[0:2])

# L = dict(range(100))
# print(L)
# 迭代 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# from collections import Iterable

# a = [1,2,3,4,5]
# b = {'a':1,'b':2,'c':3}
# c = 'abc'
# d = 123
# e = [(1,2),(1,2),(1,2),(1,2)]
# def diff(pram):
#     if(isinstance(pram, Iterable)):
#         for x,y in pram:
#             print(x,y)
#     else:
#         print('pass')
#         pass
# # diff(a)
# # diff(b)
# # diff(c)
# # diff(d)
# diff(e)

# 列表生成器
# A = list(range(0,11))
# # print(A)

# B = (x*x for x in A if x%2==0)
# for n in B:
#     print(n)

# C = [m+n for m in 'ABC' for n in '123']
# print(C)

# import os
# print(os)
# [d for d in os.listdir]

#  d = {'x': 'A', 'y': 'B', 'z': 'C' }
#  C = [ k + '=' + v for k,v in d.items()]
#  print(C)

# 生成器
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a+b
#         n = n+1
#     return 'done'
# fib(8)

# 高阶函数

# def add(x,y,f):
#     return f(x)+f(y)
# def un(x):
#     x = -x
#     return x 
# x = -5 
# y = 10

# print(add(x,y,un))

# map
# l = [1,23,4,5,6,77,8]

# i = map(str,l)
# print(list(i))

# reduce
# from functools import reduce
# def fn(x,y):
#     return x*10+y

# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     print(s,digits[s])
#     return digits[s]
# print(reduce(fn,map(char2num,'13579')))
# print(reduce(fn,[1,3,5,7,9]))

# filter 过滤
# l = [1,2,34,5,5,6,7]

# def filters(x):
#     return x%2 == 1
# a = list(filter(filters,l))
# print(a)

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# sorted 排序
# l = [1,32,5,67,13,5,71,-1,-23,5]

# print(sorted(l))
# print(sorted(l,key=abs))

# b = ['bob', 'about', 'Zoo', 'Credit']
# print(sorted(b,key=str.lower,reverse=True))

# 返回函数

# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax +n
#         return ax
#     return sum

# f = lazy_sum(1,3,5,7,9)

# print(f())

# 匿名函数

# f = lambda x:x*x
# print(f(2))


# l  = int('12',base=8)
# print(l)

# def lin(x,base = 2):
#     return int(x,base)

# print(lin('100'))


# import functools

# int2 = functools.partial(int,base=2)
# print(int2('100'))

# import hell
# print(hell.test())

# 面向对象编程

# std1 = { 'name': 'Michael', 'score': 928 }
# std2 = { 'name': 'Bob', 'score': 81 }

# def print_score(std):
#     print(std['name'], std['score'])
# print_score(std1)

# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print(self.name,self.score)
        
# bart = Student('Bart Simpson', 59)
# bart.print_score()
        
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print(self.name, self.score)

# bart = Student('Bart Simpson', 59)
# bart.print_score()
# print('master')
# print('dev')
# print('bug')
# print('43444')

# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score

# bart = Student('fdsa',2321)
# print(bart.name,Student)

#  继承和多态
# class Animal(object):
#     def run(self):
#         print('Animal is running')

#     def eat(self):
#         print('Eating meat...')

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# dog = Dog()
# print(dog.run())

# 获取对象信息
# l = type(123)
# print(l)

# print(type(a))

# print(dir('afds'))
# print('fas'.__len__())
# class MyObject(object):
#     def __init__(self):
#         self.x = 9

#     def power(self):
#         return self.x * self.x
# obj = MyObject()
# print(hasattr(obj,'x'))

# 使用__slots__

# class Student(object):
#     __slots__ = ('name','age')

# s = Student()

# s.name = 'yushaoxia'
# s.age = 25

# 使用@preperty
# class Student(object):
#     @property
#     def score(self):
#          return self._score
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.score = 60
# print( s.score)

# 定制类

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name: %s)' %self.name

# print(Student('yuhongyang'))

# class Fib(object):
#     def __init__(self):
#         self.a ,self.b = 0,1

#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a , self.b = self.b ,self.a+self.b
#         if self.a > 1000:
#             raise StopIteration()
#         return self.a
# # for n in Fib():
# #     print(n)
# print()[5]

# class Fib(object):
#     def __getitem__(self,n):
#         a ,b = 1,1
#         for x in range(n):
#             a,b=b ,a+b
#         return a
# f = Fib()
# print(f[0])

# class Fib(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a,b=1,1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a,b = b,a+b
#             return L

# f = Fib()
# print(f[0])

# class Chain(object):
#     def __init__(self,path=''):
#         self._path = path

#     def __getattr__(self,path):
#         return Chain('%s/%s' %(self._path,path))
#     def __str__(self):
#         return self._path
#     __repr__ = __str__

# print(Chain().status.sdfds.fsdf.listf)

# from enum import Enum,unique
# @unique
# class Weekday(Enum):
#     s = 1
#     q = 2
#     r = 3
#     t = 4
#     y = 5
# dya1 = Weekday.s
# print(dya1,dya1.value)

# class Hello(object):
#     def hello(self,name="world"):
#         print('Hello,%s' % name)
# h = Hello()
# print(type(Hello))

# def fn(self, name='world'): # 先定义函数
#     print('Hello, %s.' % name)

# Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
# h = Hello()
# print(h.hello(),type(h))
# 错误处理
# def foo():
#     r = some_function()
#     if r == (-1):
#         return(-1)
#     return r
# def bar():
#     r = foo()
#     if r == (-1):
#         print('Error')
#     else:
#         pass
# bar()

# try:
#     print('try...')
#     r = 10/2
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally:')
# print('END')

# try:
#     print('try...')
#     r = 10/int('2')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)
# else:
#     print('no error')
# finally:
#     print('finally...')
# print('END')

# try:
#     foo()
# except ValueError as e:
#     print('ValueError:',e)
# except UnicodeError as e:
#     print('UnicodeError')
# def foo(s):
#     return 10/int(s)

# def bar(s):
#     return foo(s)*2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:',e)
#     finally:
#         print('finally...')
# import logging
# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('END')

# class FooError(ValueError):
#     pass

# def foo(s):
#     n = int(s)
#     if n ==0:
#         raise FooError('invalid value: %s' %s)
#     return 10 / n
# foo('0')

# def foo(s):
#     n = int(s)
#     if n ==0:
#         raise ValueError('invalid value: %s' %s)
#     return 10 / n
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError')
#         raise
# bar()

# def foo(s):
#     n = int(s)
#     assert n != 0,'n is zero'
#     return 10 /n
# def main():
#     foo('0')
# main()

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# import pdb

# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n)
# 单元测试
# d = dict(a=1,b=2)
# print(d['a'])

# import unittest
# from mydict import Dict

# class TestDict(unittest.TestCase):
#    def test__init(self):
#         d = Dict(a=1,b='test')
#         self.assertEqual(d,a,1)
#         self.assertEqual(d,b,'test')
#         self.assertTrue(isinstance(d,dict))
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key,'value')
#     def test_attr(self):
#         d = Dict()
#         d.key

# def abs(n):
#     '''
#     Function to get absolute value of number.
    
#     Example:
    
#     >>> abs(1)
#     1
#     >>> abs(-1)
#     1
#     >>> abs(0)
#     0
#     '''
#     return n if n >= 0 else (-n)
# print(abs(-2))

# 文件读写
# try:
#     f = open('./python-/test.text3','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#         print('END')

# with open('./python-/test.text','r') as f:
#     print(f.read())

# f = open('./python-/test.text','a')
# f.write('11133311')
# f.close()
# for line in f.readlines():
#     print(line.strip())

# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# print(f)
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# import os
# print(os.path.abspath('.'))
# # os.path.join('/E/项目/04python/Git-python/python-','testdir')
# os.mkdir('E:/项目/04python/Git-python/python-/inflf')
# os.rmdir('E:/项目/04python/Git-python/python-/inflf')
# os.rename('aaa.py','fff.test')

# 序列化

# import pickle
# d = dict(name='Bob',age=20,score=88)
# pickle.dumps(d)

# f= open('fff.test','rb')
# d = pickle.load(f)
# f.close()
# print(d)

# import json
# d = dict(name='yuhongyang',age=22,score=88)
# print(d,json.dumps(d))

# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))

# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' %(name,os.getpid()))
# if __name__ == '__main__':
#     print('Parent process will start')
#     p = Process(target=run_proc,args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# from multiprocessing import Process,Queue
# import os,time,random

# 写数据进程执行的代码
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A','B','C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# 读数据进程执行的代码
# def read(q):
#     print('Process to read: %s' %os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' %value)
# if __name__ == '__main__':
#     # 父进程创建Queue,并传给各个子进程
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     # 启动子进程pw,写入：
#     pw.start()
#     # 启动子进程pr，读取
#     pr.start()
#     # 等待pw结束：
#     pw.join()
#     # pr进程里是死循环，无法等待期结束，只能强行终止：
#     pr.terminate()
# def process_student(name):
#     std = Student(name)
#     do_task1(std)
#     do_task2(std)
# def do_task1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)
# def do_task2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)
# import threading
# global_dict = {}
# def std_thread(name):
#     print(threading.current_thread())
#     # std = Student(name)
#     # 吧std放到全局变量global)_dict中“
#     # global_dict[threading.current_thread()] = std
# std_thread('fds')
# print(global_dict)

# import threading
# local_school = threading.local()
# def process_student():
#     # 获取当前线程关联的student
#     std = local_school.Student
#     print('Hello, %s (in %s)' % (std,threading.current_thread().name))
# def process_thread(name):
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target=process_thread,args=('Alice'),name='Thread-A')
# t2 = threading.Thread(target=process_thread,args=('Bob'),name="Thread-B")
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# [
#     {
#         id:'',
#     }
# ]

# let arryList = []
# arr = [2,5,4,8,9]
# arr.forEach((item)=>{
#     arryList.push({
#         'id':item
#     })
# })

# task_master.py

# import time, sys, queue
# from multiprocessing.managers import BaseManager

# # 创建类似的QueueManager:
# class QueueManager(BaseManager):
#     pass

# # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')

# # 连接到服务器，也就是运行task_master.py的机器:
# server_addr = '127.0.0.1'
# print('Connect to server %s...' % server_addr)
# # 端口和验证码注意保持与task_master.py设置的完全一致:
# m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# # 从网络连接:
# m.connect()
# # 获取Queue的对象:
# task = m.get_task_queue()
# result = m.get_result_queue()
# # 从task队列取任务,并把结果写入result队列:
# for i in range(10):
#     try:
#         n = task.get(timeout=1)
#         print('run task %d * %d...' % (n, n))
#         r = '%d * %d = %d' % (n, n, n*n)
#         time.sleep(1)
#         result.put(r)
#     except Queue.Empty:
#         print('task queue is empty.')
# # 处理结束:
# print('worker exit.')

# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。
# 比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。

# import re
# # test = 'a b  c'
# # m = re.match('')
# # # print(test.split(' '))
# # print(re.split(r'\s+',test))

# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(1))



