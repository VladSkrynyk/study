
# Місце для Вашого коду
from itertools import combinations, product, combinations_with_replacement

# якщо елементи в А повинні бути унікальними
#A = list(range(1, 21))
#comb = list(combinations(A, 10))

#count = set()
#for i in comb:
#    list_sum = []
#    for k in range(0, len(i)):
#        for l in range(0, len(i)):
#            if k != l:
#                list_sum.append(i[k] + i[l])
#    list_sum = set(list_sum)
#    count.add(len(list_sum))


#print(count)

# якщо елементи в А можуть повторюватись
A = list(range(1, 21))
comb = list(combinations_with_replacement(A, 10))

count = set()
print(comb)
for i in comb:
    list_sum = []
    for k in range(0, len(i)):
        for l in range(0, len(i)):
            if k != l:
                list_sum.append(i[k] + i[l])
    if len(set(list_sum)) == 3:
        print(f"tyt -> {i}")
    list_sum = set(list_sum)

    count.add(len(list_sum))


print(count)

