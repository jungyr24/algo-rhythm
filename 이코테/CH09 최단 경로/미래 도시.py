# 플로이드 워셜 알고리즘
"""
1번 회사에서 출발하여 k번 회사를 방문한 뒤에 x번회사로 가는 것
이때 최소 시간을 계산하시오

n, m입력 받은 후 회사 간 간성정보, 마지막 줄에 x, k입력받기
"""
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]
if distance == INF:
    print("-1")
else:
    print(distance)