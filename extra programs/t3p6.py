import datetime
from datetime import timedelta
 
datetimeFormat = '%H:%M:%S'
date1 = '10:01:28'
date2 = '09:56:28'
diff = datetime.datetime.strptime(date1, datetimeFormat)\
    - datetime.datetime.strptime(date2, datetimeFormat)
 
print("Difference:", diff,"hours")
