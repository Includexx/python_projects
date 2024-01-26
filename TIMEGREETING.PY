import time

timestamp = (time.strftime('%H:%M:%S'))
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = (time.strftime('%M'))
print(timestamp)
timestamp = (time.strftime('%S'))
print(timestamp)
if timestamp>=6 and timestamp<12:
  print("GOOD MORING:")
elif timestamp>=12 and timestamp<18:
  print("GOOD AFTERNOON:")
elif timestamp>=18 and timestamp<24:
  print("GOOD EVENING :")
else:
  print("GOOD NIGHT !!!!")
  











