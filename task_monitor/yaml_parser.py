#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import yaml

f = open('data/2018-10/2018-10-26.yml')
content = yaml.load(f)
print(content)
