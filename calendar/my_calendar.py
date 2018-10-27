#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
添加日历事件
https://pyobjc.readthedocs.io/en/latest/examples/CalendarStore/Scripts/add_wwdc_to_calendar/index.html
"""

from __future__ import print_function
from CalendarStore import CalCalendarStore, CalEvent
from Foundation import NSURL, NSDate
import textwrap

store = CalCalendarStore.defaultCalendarStore()
for cal in store.calendars():
    if cal._.title == "项目":
        event = CalEvent.event()
        event._.calendar = cal
        event._.title = "Python添加日历事件"
        event._.notes = textwrap.dedent('''
                这个是用Python添加的日历事件
                ''')
        event._.url = NSURL.URLWithString_('http://www.google.com.hk')
        event._.location = "中国上海市安化路492号"
        event._.isAllDay = False
        start = NSDate.dateWithString_("2018-10-27 10:00:00 +0800")
        stop = NSDate.dateWithString_("2018-10-27 12:00:00 +0800")
        event._.startDate = start
        event._.endDate = stop
        res, err = store.saveEvent_span_error_(event, 0, None)
        if not res:
            print("添加日历事件失败", err.localizedDescription())
        break

else:
    print("没有找到合适的日历")
