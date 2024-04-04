#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.coursera.org/learn/python-crash-course/supplement/GwQPr/review-iterating-over-lists-and-tuples

def full_emails(people):
    result=[]
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result
print(full_emails([('alex@example.com','Alex Diego'),('shay@example.com','Shay Brandt')]))
