# uptime
Simple python script to check connection status over time.  
Run it on a Raspberry Pi to keep track of network issues.  

Run every minute with crontab:
```
crontab -e
*/1 * * * * python /home/pi/uptime.py
```
Error logs will be written to /home/pi/uptime.log with a timestamp.
