import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if 'DKTGT' in seq: print(defline)