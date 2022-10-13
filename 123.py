z = [int(i) for i in input().split()]
count = 0

for i in range(len(z) - 1):
    if z[i] < z[i + 1]:
        count += 1

print(count)
