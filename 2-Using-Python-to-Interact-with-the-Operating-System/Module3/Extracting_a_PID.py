#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def extract_pid(log_line):
    regex = r"\[(\d)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]


log = "99 elephants in a [cage]"
print(extract_pid(log))
