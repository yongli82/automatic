#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
在10:00~20:00, 整点的时候弹出提醒

https://pyobjc.readthedocs.io/en/latest/apinotes/NotificationCenter.html



display notification "All graphics have been converted." with title "My Graphic Processing Script" subtitle "Processing is complete." sound name "Frog"

"""


# https://pypi.org/project/pync/
#import pync

#pync.notify("hello world")


# 

# import os
# 
# def notify(title, text):
#     os.system("""
#               osascript -e 'display notification "{}" with title "{}"'
#               """.format(text, title))
# 
# notify("Title", "Heres an alert")


from Foundation import NSUserNotification
from Foundation import NSUserNotificationCenter
from Foundation import NSUserNotificationDefaultSoundName


class Notification():
    def notify(self, _title, _message, _sound = False):
        self._title = _title
        self._message = _message
        self._sound = _sound

        self.notification = NSUserNotification.alloc().init()
        self.notification.setTitle_(self._title)
        self.notification.setInformativeText_(self._message)
        if self._sound == True:
            self.notification.setSoundName_(NSUserNotificationDefaultSoundName)

        center = NSUserNotificationCenter.defaultUserNotificationCenter()
        center.deliverNotification_(self.notification)

N = Notification()
N.notify(_title="SOME", _message="Something", _sound=True)




