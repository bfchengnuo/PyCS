import time
from datetime import datetime

time.sleep(2)

print(datetime.now())
print(datetime.strptime("2020-04-27 23:33:25", "%Y-%m-%d %H:%M:%S"))
print(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))