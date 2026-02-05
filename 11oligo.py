def tm (A,T,G,C):
	length = A+T+G+C
	if length <= 13: return ( A + T ) * 2 + ( G + C ) * 4
	else :           return 64.9 + 41 * ( G + C -16.4) / length

print (tm(5,3,3,4))
