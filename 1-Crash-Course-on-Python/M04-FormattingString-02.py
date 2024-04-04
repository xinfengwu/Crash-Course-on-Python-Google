#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.coursera.org/learn/python-crash-course/supplement/566hN/review-formatting-strings

price =7.5
with_tax =price*1.09
print(price,with_tax)
print('Base price: ${:.2f}. With Tax: ${:.2f}'.format(price,with_tax))
