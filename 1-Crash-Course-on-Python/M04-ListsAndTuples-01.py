#!/usr/bin/env python
# -*- coding: utf-8 -*-

def file_size(file_info):
    name,type,size = file_info
    return ("{:.2f}".format(size / 1024))
print(file_size(('Class Assignment','docx',17875)))
print(file_size(('Notes','txt',496)))
print(file_size(('Program','py',1239)))
