#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-

import json
import os
import sys
os.system("openstack image list > image.txt")

f = open("image.txt","r",encoding='utf-8')
for line in f.readlines():
    location = line.find(sys.argv[1])
    if  location != -1:
        print(line[0:location].replace("|", "").strip())

f.close()
