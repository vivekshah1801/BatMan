# BatMan - Battery Manager for Linux System
It logs your battery status and analyses your battery behaviour using those logs.

# Setup Guide
> 1. pip3 install -r requirements.txt
> 2. "crontab -e"
  Add following line to your cronjob list
  */2 * * * *  python3 /home/path/to/BatMan.py &
> 3. The script will automatically run every 2 minutes and logs your battery status to battery_log.log file.
> 4. The log file will be used for deriving data about your battery behaviour.
