#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def rearrange_name(name):

    result = re.search(r"^([\w]*), ([\w\. ]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Lovelace, Ada F.")
print(name)
