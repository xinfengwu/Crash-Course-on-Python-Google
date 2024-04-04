#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.coursera.org/learn/python-crash-course/supplement/DCZhJ/review-creating-new-strings

def replace_domain(email,old_domain,new_domain):
    if '@'+ old_domain in email:
        index = email.index('@'+old_domain)
        new_email = email[:index]+'@'+new_domain
        return new_email
    return email
str = replace_domain('abcd@google.com','google.com','apple.com')
print(str)
