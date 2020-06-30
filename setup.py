from crontab import CronTab
import os
import getpass

try:
    username = getpass.getuser()
    cron = CronTab(user=username)

    previousCron = cron.remove_all(command="_BatMan.py")
    if previousCron > 0:
        print("Previous CronJobs related to BatMan deleted.")

    python = "python3"
    path = os.path.dirname(os.path.realpath(__file__)).replace(" ","\ ")
    command = "{} {}/_BatMan.py".format(python, path)
    batmancronjob = cron.new(command=command, comment="BatMan @ github.com/vivekshah1801.")
    cron.write()
except Exception as e:
    print("""
    Some Error Occured while setting BatMan.
    Report this issue at https://github.com/vivekshah1801/BatMan/issues/new
    Error: """, e)
    print()
    exit(1)

print("BatMan set up")