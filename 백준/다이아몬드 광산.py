r, c = map(int, input().split())
graph = [[0 for _ in range(11)] for _ in range(11)]
for i in range(1, r+1):
    tmp = list(input())
    for j in range(1, c+1):
        graph[i][j] = int(tmp[j-1])

ld = [[0 for _ in range(808)] for _ in range(808)]
rd = [[0 for _ in range(808)] for _ in range(808)]
lu = [[0 for _ in range(808)] for _ in range(808)]
ru = [[0 for _ in range(808)] for _ in range(808)]

for i in range(r, 0, -1):
    for j in range(1, c+1):
        if graph[i][j] == 1:
            ld[i][j] = ld[i+1][j-1]+1
            rd[i][j] = rd[i+1][j+1]+1

for i in range(1, r+1):
    for j in range(1, c+1):
        if graph[i][j] == 1:
            lu[i][j] = lu[i-1][j-1]+1
            ru[i][j] = ru[i-1][j+1]+1

answer = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        for k in range(min(ld[i][j], rd[i][j]), answer, -1):
            if lu[i+2*(k-1)][j] >= k and ru[i+2*(k-1)][j] >= k:
                answer = max(answer, k)
print(answer)
