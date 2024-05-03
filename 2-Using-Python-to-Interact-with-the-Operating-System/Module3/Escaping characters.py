#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def check_text(expression, text):
    result = re.search(expression, text)
    return result != None


print(check_text(r".com", "welcome"))  # True
print(check_text(r"\.com", "welcome"))  # False
print(check_text(r"\.com", "mydomain.com"))  # True
print(check_text(r"\w*", "This is an example"))  # True
print(check_text(r"\w*", "And_this_is_another"))  # True
