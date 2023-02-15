i = 0
n = 7
k = 0
while i < n:
    j = 0
    while j < i * i:
        k += 1
        j += 1
    i += 1

print(k)

sum1 = 0
for i in range(0, 7):
    sum1 += i**2
print(sum1)

