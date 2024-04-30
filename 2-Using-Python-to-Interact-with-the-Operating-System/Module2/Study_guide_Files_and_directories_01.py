#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
#  os.chdir(os.path.join(os.getcwd(),'2-Using-Python-to-Interact-with-the-Operating-System/Module2'))
dest_dir = os.path.join(os.getcwd(),"test1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

# Construct source and destination paths:
src_file = os.path.join(os.getcwd(),'sample_data',"README.md")
dest_file = os.path.join(os.getcwd(),"test1","README.md")

# Move the file from its original location to the destination:
os.rename(src_file,dest_file)
