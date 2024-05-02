#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def check_text(expression,text):
    result=re.search(expression,text)
    return result != None
    
def check_All_text(expression,text):
    result=re.findall(expression,text)
    return result != None
    
print(check_text(r"Py.*n", "Pygmalion"))
print(check_text(r"Py.*n", "Python Programming"))
print(check_text(r"Py[a-z]*n", "Python Programming"))
print(check_text(r"Py[a-z]*n", "Pyn"))
print(check_text(r"o+l+", "goldfish"))
print(check_text(r"o+l+", "woolly"))
print(check_text(r"o+l+", "boil"))

print(check_text(r"p?each", "To each their own"))
print(check_text(r"p?each", "I like peaches"))

