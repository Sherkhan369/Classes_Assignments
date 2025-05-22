#The Date & Time

import time

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# current time

import time
current_time = time.localtime(time.time())
print ("Local current time :", current_time)



#-----------The Calendar
import calendar

cal = calendar.month(2025, 5)
print ("Here is the calendar:")
print (cal)


#-------The Date Time
from datetime import date

date1 = date(2025, 5, 19)
print("Date:", date1)
date2 = date(2025, 5, 21)
print("Date2:", date2)


#--------strftime() Method
import datetime
x = datetime.datetime(2025, 1, 1)

print(x.strftime("%f")) 
print(x.strftime("%A")) 
print(x.strftime("%Y")) 
print(x.strftime("%B")) 