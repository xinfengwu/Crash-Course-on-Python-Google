#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.coursera.org/learn/python-crash-course/supplement/0uq4H/review-modifying-the-contents-of-a-list

fruits =['Pineapple','Banana','Apple','Melon']
fruits.insert(0,'Orange')
fruits.insert(24,'Peach')
fruits.remove('Melon')
print(fruits)
fruits.pop(0)
print(fruits)
