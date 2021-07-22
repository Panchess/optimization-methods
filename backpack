n = int(input())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
k = int(input())
table = [[0] * (k + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= weights[i - 1]:
            table[i][j] = max(table[i - 1][j], values[i - 1] + table[i - 1][j - weights[i - 1]])
        else:
            table[i][j] = table[i - 1][j]
i = n
j = k
weight_best = 0
while (i > 0):
    if table[i][j] > table[i - 1][j]:
        weight_best += weights[i - 1]
        j = j - weights[i - 1]
        i = i - 1
    else:
        i = i - 1
print(weight_best, table[n][k])
