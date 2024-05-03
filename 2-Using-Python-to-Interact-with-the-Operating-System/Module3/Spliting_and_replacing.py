#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(result)
result = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(result)
result = re.sub(r"([\w.%+-]+@[\w.-]+)", "[REDACTED]",
                "Recieved an email for go_nuts95@my.example.com")
print(result)
lastname = "last name"
result = re.sub(r"^([\w .-]*), ([\w .-]*)$",
                r"\2 is first name,and \1 is " + lastname, "Lovecace, Ada")
print(result)
