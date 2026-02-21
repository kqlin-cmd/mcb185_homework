import sys
import random

people = int(sys.argv[1])
calendar = int(sys.argv[2])
iterations = int(sys.argv[3])

sames = 0
for _ in range(iterations):
	classroom = []
	for i in range(people):
		birthday = random.randint(0,calendar-1)
		classroom.append(birthday)

	same_birthday = False
	for i in range(0, len(classroom)):
		for j in range(i+1,len(classroom)):
			if classroom[i] == classroom[j]:
				same_birthday = True
				break
			classroom.append(birthday)
		if same_birthday: sames +=1

print (sames/iterations)


# 23 365 10000
