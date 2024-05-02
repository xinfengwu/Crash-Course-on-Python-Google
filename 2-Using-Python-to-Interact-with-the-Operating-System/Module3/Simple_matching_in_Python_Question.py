# Fill in the code to check if the text passed contains the vowels a, e, and i and meet the following criteria: 

# the vowels appear in the order a, e, and i 
# the vowels have exactly one occurrence of any other character between them.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True
