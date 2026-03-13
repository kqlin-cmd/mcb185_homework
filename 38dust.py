import argparse

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)


#import math
#
#def entropy(s):
#	pa = s.count('A')/len(seq)
#	pc = s.count('C')/len(seq)
#	pg = s.count('G')/len(seq)
#	pt = s.count('T')/len(seq)
#	h = 0
#	if pa != 0: h -= pa * math.log2(pa)
#	if pc != 0: h -= pc * math.log2(pc)
#	if pg != 0: h -= pg * math.log2(pg)
#	if pt != 0: h -= pt * math.log2(pt)
#
#seq = 'AATTCGGCAT'
#seqs = list(seq)
#k = 4
#for i in range(len(seq) - k + 1):
#	win = seq[i:i-k]
#	if entropy(win) < 1.0:
#		for j in range(i,i+k):
#			seqs[j] = 'N'
#
#
#print(''.join(seqs))
