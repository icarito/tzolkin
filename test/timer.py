import datetime

midnight = datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=999)
#midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
now = datetime.datetime.now()
delta = midnight - now
print delta.seconds
print str(delta)
