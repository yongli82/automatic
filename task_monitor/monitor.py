#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from datetime import datetime
from datetime import timedelta
import time
import yaml

import os
import os.path

def notify(title, subtitle, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" subtitle "{}"'
              """.format(text, title, subtitle))

print("-" * 80)
# 当天
now = datetime.now()
print(now)
month = now.strftime("%Y-%m")
today = now.strftime("%Y-%m-%d")

yml_file = os.path.join(os.path.dirname(__file__), "data/%s/%s.yml" % (month, today))

print("yml_file=%s" % yml_file)
if not os.path.exists(yml_file):
    print("任务文件%s不存在" % yml_file)
    exit(0)

tasks = []
with open(yml_file) as f:
    tasks = yaml.load(f)

todo_tasks = []
for task in tasks:
    print(task)
    # {'Yaml解析': {'begin': '10:00', 'end': '11:00', 'status': None, 'memo': None}}
    task_name = [*task][0]
    print(task_name)
    task_info = task[task_name]
    status = task_info["status"]
    if status not in [None, "todo"]:
        continue
    begin = today + " " + task_info["begin"]
    end = today + " " + task_info["end"]
    begin_time = datetime.strptime(begin, "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(end, "%Y-%m-%d %H:%M")
    if now < begin_time:
        continue
    if now - begin_time < timedelta(minutes=2):
        todo_tasks.append({"task_name": task_name, "begin_time": task_info["begin"], "end_time": task_info["end"], "type": "开始"})
        continue
    if now > end_time:
        todo_tasks.append({"task_name": task_name, "begin_time": task_info["begin"], "end_time": task_info["end"], "type": "超时"})
        continue

print("=" * 80)
print("Todo Tasks:")
for todo_task in todo_tasks:
    print(todo_task)
    task_name = todo_task["task_name"]
    begin_time = todo_task["begin_time"]
    end_time = todo_task["end_time"]
    todo_type = todo_task["type"]
    content = "【%(type)s】 %(begin_time)s ~ %(end_time)s" % todo_task
    subtitle = "%(task_name)s " % todo_task
    notify("待办任务", subtitle, content)
    time.sleep(2)
