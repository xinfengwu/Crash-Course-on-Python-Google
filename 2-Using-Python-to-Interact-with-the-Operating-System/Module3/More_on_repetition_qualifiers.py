#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.findall(r"s\w{,20}", "I really like strawberries"))
