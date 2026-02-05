import random

def saving_throw(dc,mode="normal"):
	if mode == "normal": roll = random.choice(range(1, 21))
	elif mode == "advantage": roll = max(random.choice(range(1, 21)), random.choice(range(1, 21)))
	elif mode == "disadvantage": roll = min(random.choice(range(1, 21)) , random.choice(range(1, 21)))
	return roll>=dc

trials = 10000
dc = 5
mode = "normal"
successes = 0

for _ in range(trials):
	if saving_throw(dc, mode):
		successes += 1

print(successes / trials)
