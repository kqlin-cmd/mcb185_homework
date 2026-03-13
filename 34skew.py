import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10

g = 0
c = 0
for j in seq[:w]:
	if j == 'G': g += 1
	if j == 'C': c += 1

for i in range(len(seq) - w +1):
	s = seq[i:i+w]
	print(i,sequence.gc_comp(s),sequence.gc_skew(s))
