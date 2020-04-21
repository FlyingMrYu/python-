#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'yushaoxia'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('len 1')
    elif len(args)==2:
        print('len 2')
    else:
        print('defaut else')

if __name__ == '__main__':
    test()