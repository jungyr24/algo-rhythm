"""
1. 현재 위치에서 현재 방향을 기준, 왼쪽 방향(반시계 방향으로 90도 회전)부터 차례대로 갈 곳 정함
2. 바로 왼쪽 방향에 방문하지 않은 칸 존재 -> 왼쪽 회전 후 왼쪽으로 한 칸 전진
                                    존재x -> 왼쪽 회전만 수행 후 1단계로
3. 만약 네 방향 모두 방문한 칸이거나 바다인 경우 바라보는 방향 유지한 채로 뒤로 이동 후 1단계로 돌아감
   뒤쪽 방향이 바다인 경우 움직임 멈춤

이동을 마친 후 방문한 칸의 개수 구하기
"""
n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = []
visited = [] # 방문
for i in range(n):
    graph.append(list(map(int, input().split())))
    visited.append([0 for x in range(m)])
visited[x][y] = 1

# 북 서 남 동
direction = [0, 3, 2, 1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnt = 1
d_cnt = 0
while True:
    # 방향 전환
    d = (d+1) % 4
    
    nx = x + dx[d]
    ny = y + dy[d]

    if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if graph[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            x, y = nx, ny
            d_cnt = 0
            cnt += 1
            continue
        else:
            d_cnt += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if d_cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있으면 뒤로 이동
        if graph[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        d_cnt = 0

print(cnt)
for i in range(n):
    print(visited[i])

"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""