f = open('24-s1.txt')
a = f.readlines()
ans = 0
x = 0
for i in range(len(a)):
    b = a[i]
    for j in range(len(b)-2):
        if b[j] == 'A' and b[j+2] == 'R':
            x += 1
    if x != 0:
        ans += 1
        x = 0
print(ans)
