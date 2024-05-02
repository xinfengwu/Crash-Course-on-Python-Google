#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def check_text(expression,text):
    result=re.search(expression,text)
    return result != None
    
def check_All_text(expression,text):
    result=re.findall(expression,text)
    return result != None
    
print(check_text(r"[Pp]ython", "Python"))
print(check_text(r"[a-z]way", "The end of the highway"))
print(check_text(r"[a-z]way", "What a way to go"))
print(check_text("cloud[a-zA-Z0-9]", "cloudy"))
print(check_text("cloud[a-zA-Z0-9]", "cloud9"))
print(check_text(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(check_text(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(check_text(r"cat|dog", "I like cats."))
print(check_text(r"cat|dog", "I love dogs!"))
print(check_text(r"cat|dog", "I like both dogs and cats."))

print(check_text(r"cat|dog", "I like cats."))
print(check_text(r"cat|dog", "I love dogs!"))
print(check_text(r"cat|dog", "I like both dogs and cats."))
print(check_All_text(r"cat|dog", "I like both dogs and cats."))
