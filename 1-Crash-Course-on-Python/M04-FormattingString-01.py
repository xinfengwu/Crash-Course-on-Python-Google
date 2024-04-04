#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.coursera.org/learn/python-crash-course/supplement/566hN/review-formatting-strings

name = 'Manny'
print('{}, your lucky number is {}.'.format(name,len(name)))
print('{name}, your lucky number is {number}. Congrats! {name}. Congrats! {name}.'.format(name='Manny',number=len('Manny')))
