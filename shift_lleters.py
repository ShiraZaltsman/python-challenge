# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:21:22 2019

@author: User
"""
import string


def shiftByTwo(str_):
    strList = list(str_)
    abc = list(string.ascii_lowercase)
    new_str = []
    for l in strList:
        if l in abc:
            index = (abc.index(l) + 2) % len(abc)
            new_str.append(abc[index])
        else:
            new_str.append(l)
    print(''.join(new_str))


if __name__ == '__main__':
    shiftByTwo("map")
