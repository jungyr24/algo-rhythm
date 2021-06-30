n = int(input())
direction = list(input().split())

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dict_d = {
    "L": 0,
    "R": 1,
    "U": 2,
    "D": 3
}
x, y = 1, 1
for i in direction:
    nx = x + dx[dict_d[i]]
    ny = y + dy[dict_d[i]]
    if nx >= 1 and nx < n and ny >= 1 and ny < n:
        x, y = nx, ny
    
print(x, y)