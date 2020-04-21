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

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.name,self.score)
        
bart = Student('Bart Simpson', 59)
bart.print_score()
        
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print(self.name, self.score)

# bart = Student('Bart Simpson', 59)
# bart.print_score()
print('master')
