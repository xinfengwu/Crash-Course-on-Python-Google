#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def check_text(expression,text):
    result=re.search(expression,text)
    return result != None
    
print(check_text(r"A.*a", "Argentina"))# True
print(check_text(r"A.*a", "Azerbaijan"))# True
print(check_text(r"^A.*a$", "Australia"))# True
print(check_text(r"^[a-zA-Z_][a-zA-Z0-9_]*$","_this_is_a_valid_variable_name"))# True
print(check_text(r"^[a-zA-Z_][a-zA-Z0-9_]*$", "this isn't a valid variable"))# False
print(check_text(r"^[a-zA-Z_][a-zA-Z0-9_]*$","my_variable1"))# True
print(check_text(r"^[a-zA-Z_][a-zA-Z0-9_]*$","2my_variable1"))# False

