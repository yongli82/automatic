#!/usr/bin/env python
# -*- coding:utf-8 -*-

from CalendarStore import CalCalendarStore, CalEvent
from Foundation import NSURL, NSDate
import textwrap


def createEvent(title, start_time, stop_time, calendar_name=u"项目", note='', url='', location=''):
    """
    createEvent("Python事件", "2018-10-28 10:00:00 +0800", "2018-10-28 12:00:00 +0800")
    """
    store = CalCalendarStore.defaultCalendarStore()
    for cal in store.calendars():
        if cal._.title == calendar_name:
            event = CalEvent.event()
            event._.calendar = cal
            event._.title = title
            event._.notes = textwrap.dedent(note)
            if url:
                event._.url = NSURL.URLWithString_(url)
            if location:
                event._.location = location
            event._.isAllDay = False
            start = NSDate.dateWithString_(start_time)
            stop = NSDate.dateWithString_(stop_time)
            event._.startDate = start
            event._.endDate = stop
            res, err = store.saveEvent_span_error_(event, 0, None)
            if not res:
                print("添加日历事件失败", err.localizedDescription())
                break
            else:
                print("添加日历事件成功: %s" % res)
                break
    else:
        print("没有找到合适的日历")
        for cal in store.calendars():
            print(cal._.title)
        
        
if __name__ == '__main__':
    createEvent("Python事件", "2018-10-28 10:00:00 +0800", "2018-10-28 12:00:00 +0800")
