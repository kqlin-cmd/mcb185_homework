import sys
import math

vals = []
for s in sys.argv[1:]:
	vals.append(float(s))

# max, min, range
vals.sort()
total = 0
for val in vals: total += val
mean = total / len(vals)

# median
m = len(vals) // 2
if len(vals) % 2 == 1: median = vals[m]
else: median = ( vals[m] + vals[m-1] ) / 2

# standard deviation
if len(vals) == 1
	stdv = 0
sums = 0
for summ in vals: sums += ( summ - mean )**2
stdv = math.sqrt(sums / (len(vals) - 1))


print(vals)
print('minimum:', vals[0])
print('maximum:', vals[-1])
print('range:', vals[-1] - vals[0])
print('average:', mean)
print('median:', median)
print('standard deviation:',stdv)
