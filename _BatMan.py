# BatMan - Battery Manager for your Linux System
# @author Vivek Shah

import psutil
import time
import os

logfilepath = os.path.dirname(os.path.realpath(__file__)) + "/battery_log.csv"

with open(logfilepath,"a") as logfile:
    try:
        battery_status = psutil.sensors_battery()
        percentage = battery_status.percent
        secondsleft = battery_status.secsleft
        power_plugged = battery_status.power_plugged
        timestamp = time.localtime()
        s = time.strftime("%D %H:%M:%S",timestamp) + "," + str(percentage) + "," + str(secondsleft) + "," + str(power_plugged) + "\n"
        logfile.write(s)
    except Exception as exp:
        print(exp)
        exit()

## This code takes less than 0.1 second to run.
## So it will take less than 0.1 second of CPU time in One minute(3600 seconds)
## Stores the battery logs in battery_log.log file
