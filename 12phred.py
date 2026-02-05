import math

def char_to_prob(c):
    Q = ord(c) - 33
    return 10 ** (-Q / 10)

def prob_to_char(p):
        a = -10*(math.log10(p))+33
        return int(round(a))


print(char_to_prob('A'))
print(chr(prob_to_char(0.001)))
