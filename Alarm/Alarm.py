from datetime import datetime
import time
import winsound


timeOpt = input("Chose one of this two -> AM, PM :")
userHrs = int(input("Chose hour(s) :"))
userMin = int(input("Chose minute(s) :"))
userSec = int(input("Chose secende(s) :"))

if not (0 <= userHrs <= 12):
    raise ValueError("Hours must be between 0 and 12 for AM/PM.")
if not (0 <= userMin < 60):
    raise ValueError("Minutes must be between 0 and 59.")
if not (0 <= userSec < 60):
    raise ValueError("Seconds must be between 0 and 59.")


realTime = datetime.now()
realTime = [realTime.hour, realTime.minute, realTime.second]

if timeOpt == "AM":
    pass
elif timeOpt == "PM" :
    if userHrs != 12:  # 12 AM -> 0 hours
        userHrs += 12
else :
    pass

cond = [userHrs, userMin, userSec]
while realTime != cond :
    print(f"{str(realTime[0]).zfill(2)}:{str(realTime[1]).zfill(2)}:{str(realTime[2]).zfill(2)}")
    time.sleep(1)
    realTime = datetime.now()
    realTime = [realTime.hour, realTime.minute, realTime.second]

for i in range(0,3):
    winsound.Beep(440, 1000)


