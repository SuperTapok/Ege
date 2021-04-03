f = open('24-5.txt')
a = f.read()
max = 0
ans = 0
for i in range(len(a)):
    if a[i] == ')':
        ans += 1
        if ans > max:
            max = ans
    else:
        ans = 0
print(max)
