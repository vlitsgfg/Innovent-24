import random
from datetime import datetime
import json

l = json.load(open("emp-list.json"))
print(len(l))

d = {}

s = ""
for i in range(1, 15):
	d[datetime(2023, 9, i).strftime("%d-%m-%Y")] = random.sample(l, random.randint(400, 500))

f = open("emp-attendance.json", "w+")
f.write(json.dumps(d, indent=4))
f.close()
