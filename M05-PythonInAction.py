#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import secrets
import subprocess
from pathlib import Path 

cwd=Path.cwd()
with open(cwd/'users_in.csv','r') as file_input, open(cwd/'users_out.csv','w') as file_out:
    reader = csv.DictReader(file_input)
    writer = csv.DictWriter(file_out,fieldnames=reader.fieldnames)
    writer.writeheader()
    for user in reader:
        user['password']=secrets.token_hex(8)
        useradd_cmd=['/sbin/useradd',
                     '-c',user['real_name'],
                     '-m',
                     '-G',"users",
                     '-p',user['password'],
                     user['username']
                     ]
    #  subprocess.run(useradd_cmd,check=True)
        writer.writerow(user)
