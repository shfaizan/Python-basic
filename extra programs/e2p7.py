from datetime import datetime

print("17103455")
print("Faizan Shaikh", end='\n\n')

now = datetime.now()
now1 = now.strftime("%a %d %b %y")
now2 = now.strftime("%A %d %B %Y")
print(now, now1, now2, sep = "\n")
