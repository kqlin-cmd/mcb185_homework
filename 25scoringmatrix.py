import sys

alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

print('   ',end = '')
for i in range(len(alph)):
	print(alph[i],end = '   ')
print()

for i in range(len(alph)):
	print(alph[i],end = ' ')
	for n in range(len(alph)):
		if n == i: print(mat, end = '  ')
		else:      print(mis, end = '  ')
	print()
