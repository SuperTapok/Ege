max_qua_of_del = 2
min_int_with_max_dels = 586431
max_int_with_max_dels = 586132
list_of_minimals = []
for i in range(586132, 586431):
    qua_of_del = 2
    max_del = 0
    for j in range(2, i//2+1):
        if i % j == 0:
            qua_of_del += 1
            max_del = j
    if qua_of_del >= max_qua_of_del:
        max_qua_of_del = qua_of_del
        if i > max_int_with_max_dels:
            max_int_with_max_dels = i
            ans_max = max_del
if i < min_int_with_max_dels:
    list_of_minimals.append(i)
    ans_min = max_del

print(max_qua_of_del, ans_min)
print(max_qua_of_del, ans_max)
