import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(board, c):

    n, m = len(board), len(board[0])
    robot = [(i,j) for i in range(n) for j in range(m) if board[i][j]==2]

    distance = [[INF] * m for _ in range(n)]

    x, y = robot[0][0], robot[0][1]
    q = [(0, x, y)]
    distance[x][y] = 0
    d_x, d_y = [(i,j) for i in range(n) for j in range(m) if board[i][j]==3][0]
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0 or board[nx][ny] == 3:
                cost = dist + 1
            if board[nx][ny] == 1:
                cost = dist + 1 + c
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
 
    return distance[d_x][d_y]

print(solution([[0,0,0,0,2,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0,1,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,3,0,0,0,1,0]], 1))
print(solution([[0,0,0,0,2,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0,1,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,3,0,0,0,1,0]], 2))