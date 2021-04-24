f = open('27-A.txt')
minr = 10000
s1 = 0
s2 = 0
s3 = 0
for line in f:
    a, b, c = map(int, line.split())
    if (a >= b) and (a >= c):
        s3 += a
        if b >= c:
            s2 += b
            s1 += c
        else:
            s2 += c
            s1 += b
    elif (b >= a) and (b >= c):
        s3 += b
        if a >= c:
            s2 += a
            s1 += c
        else:
            s2 += c
            s1 += a
    elif (c >= a) and (c >= b):
        s3 += c
        if a >= b:
            s2 += a
            s1 += b
        else:
            s2 += b
            s1 += a
    if abs(a - b) % 2 != 0 and abs(a - b) < minr:
        minr = abs(a - b)
    elif abs(a - c) % 2 != 0 and abs(a - c) < minr:
        minr = abs(a - c)
if (s1 + s2) % 2 != 0:
    print(s3)
else:
    print(s3-minr)
