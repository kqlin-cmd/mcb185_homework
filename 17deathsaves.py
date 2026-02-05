import random

def death_save():
	successes = 0
	failures = 0

	while True:
		roll = random.choice(range(1, 21))

		if roll == 1:
			failures += 2
		elif roll == 20:
			return "revived"
		elif roll < 10:
			failures += 1
		else:
			successes += 1

		if failures >= 3:
			return "died"
		if successes >= 3:
			return "stabilized"

trials = 10000
results = {"died": 0, "stabilized": 0, "revived": 0}

for _ in range(trials):
	outcome = death_save()
	results[outcome] += 1

for outcome in results:
	print(outcome, results[outcome] / trials)
