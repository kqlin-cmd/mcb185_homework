import sys
import mcb185

kd = {
	'A': 1.8,  'C': 2.5,  'D': -3.5, 'E': -3.5,
	'F': 2.8,  'G': -0.4, 'H': -3.2, 'I': 4.5,
	'K': -3.9, 'L': 3.8,  'M': 1.9,  'N': -3.5,
	'P': -1.6, 'Q': -3.5, 'R': -4.5, 'S': -0.8,
	'T': -0.7, 'V': 4.2,  'W': -0.9, 'Y': -1.3
}

def hydropathy(seq):
	total = 0
	for aa in seq:
		total += kd[aa]
	return total / len(seq)

def has_signal_peptide(seq):
	end = min(30, len(seq))
	for i in range(0, end - 8 + 1):
		window = seq[i:i+8]
		if 'P' in window:
			continue
		if hydropathy(window) >= 2.5:
			return True
	return False

def has_transmembrane_region(seq):
	for i in range(30, len(seq) - 11 + 1):
		window = seq[i:i+11]
		if 'P' in window:
			continue
		if hydropathy(window) >= 2.0:
			return True
	return False

for name, seq in mcb185.read_fasta(sys.argv[1]):
	if has_signal_peptide(seq) and has_transmembrane_region(seq):
		print(name)
