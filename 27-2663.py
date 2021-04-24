f = open('27-2663-B.txt', "r")
minr1 = 10000
minr2 = 100000
minr3 = 1000000
s = 0
for line in f:
    a, b = map(int, line.split())
    s += min(a, b)
    k = abs(a-b)
    if k < minr1:
        minr1 = k
    elif minr1 < k < minr2:
        minr2 = k
    elif minr2 < k:
        minr3 = k
if s % 3 == 0:
    print(s)
elif (s+minr1) % 3 == 0:
    print(s+minr1)
elif (s+minr2) % 3 == 0:
    print(s+minr2)
elif (s+minr3) % 3 == 0:
    print(s+minr3)
elif (s+minr1+minr2) % 3 == 0:
    print(s+minr1+minr2)
elif (s+minr1+minr2+minr3) % 3 == 0:
    print(s+minr1+minr2+minr3)
# answer is 66228 (right) and 203412732 (right)
