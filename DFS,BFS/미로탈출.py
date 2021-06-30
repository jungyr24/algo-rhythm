"""
N x M 크기의 직사각형에서 
괴물이 있는 부분은 0, 없는 부분은 1
동빈이가 있는 (1, 1)에서 출발하여 괴물을 피해 탈출구가 있는 (N, M)까지의 거리 구하기
* 반드시 탈출할 수 있는 형태로 제시됨
"""
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

# visited 배열 따로 안 만들고 방문함에 따라 1씩 증가시키기
# visited = [[False for i in range(m)] for j in range(n)]
# visited[0][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([(0, 0)])


while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny] == '0':
                continue

            if graph[nx][ny] == '1':
                q.append((nx, ny))
                graph[nx][ny] = str(int(graph[x][y])+1)

                # --------- 출력 -----------
                for i in range(n):
                    print(graph[i])
                print("--------------------")
                # --------------------------

                
print(graph[n-1][m-1])


"""
5 6
101010
111111
000001
111111
111111
"""