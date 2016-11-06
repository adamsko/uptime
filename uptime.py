import urllib2, urllib, datetime

request = urllib2.Request('https://www.google.com')
try: response = urllib2.urlopen(request)
except urllib2.URLError as e:
    t = datetime.datetime.now()
    f = open('/home/pi/uptime.log', 'a')
    f.write(str(t))
    f.write(str(e.reason))
    f.write('\n')
    f.close

