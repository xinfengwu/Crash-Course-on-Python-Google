#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.coursera.org/learn/python-crash-course/supplement/GwQPr/review-iterating-over-lists-and-tuples

winners =['Ashley','Dylan','Reese']
for index, person in enumerate(winners):
    print('{} - {}'.format(index +1, person))
