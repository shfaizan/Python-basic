from datetime import datetime, timedelta
from pytz import timezone, utc

print("17103455")
print("Faizan Shaikh", end='\n\n')

t1 = 'Sun 15 Mar 2019 11:44:36 -0700'
t2 = 'Sun 15 Mar 2019 11:44:36 -0030'

fmt = '%a %d %b %Y %H:%M:%S %z'

t1_obj = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
t2_obj = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

t1_utc = t1_obj.astimezone(timezone('UTC'))
t2_utc = t2_obj.astimezone(timezone('UTC'))

delay = t1_utc - t2_utc
delay_in_s = delay.total_seconds()

days = divmod(delay_in_s, 86400)
hours = divmod(days[1], 3600)
minutes = divmod(hours[1], 60)
seconds = divmod(minutes[1],1)

print("Delay is of %d hours, %d minutes and %d seconds" %(hours[0], minutes[0], seconds[0]) )
