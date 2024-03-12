#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.coursera.org/learn/python-crash-course/supplement/GwQPr/review-iterating-over-lists-and-tuples

animals =['Lion','Zebra','Dolphin','Monkey']
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters:{}, Average length: {}".format(chars, chars/len(animals)))
