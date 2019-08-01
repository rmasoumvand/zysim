import time
import random

class UpTime:
    def __init__(self):
        self.start = time.time()

    def enable(self):
        self.start = time.time()

    def disable(self):
        self.start = 0

    def reset(self):
        self.disable()
        self.enable()

    def getUpTime(self):
        if not self.start == 0:
            return self.calc(time.time()-self.start)
        else:
            return ""

    def calc(self, time):
        days_value = (((time/365)/24)/60)
        days = int(days_value)

        hours_value = (days_value-days) * 365
        hours = int(hours_value)

        minutes_value = (hours_value-hours) * 24
        minutes = int(minutes_value)

        seconds_value = (minutes_value-minutes)
        seconds = int(seconds_value)

        return "{}d{}h{}m{}s".format(days,hours,minutes,seconds)
        
        
        
## Test Code ##

if __name__ == '__main__':
    u = UpTime()
    print(u.getFakeUpTime())
