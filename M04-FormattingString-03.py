#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.coursera.org/learn/python-crash-course/supplement/566hN/review-formatting-strings

def to_celsius(x):
    return(x-32)*5/9

for x in range(0,101,10):
    print('{:>3.0f} F | {:>6.2f} C'.format(x,to_celsius(x)))
