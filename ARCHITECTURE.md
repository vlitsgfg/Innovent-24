

number of days = len(current_attendance)

hashmap = {}
days_absent

for each day in current_attendance:
	for empID in day:
		if empID in hashmap:
			hashmap[empID] += 1
		else:
			hashmap[empID] = 1

input := empID

hashmap[empID] * 100 / number of days

