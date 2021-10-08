p = input()
cnt = 0

x, y = int(ord(p[0])) - int(ord('a')) + 1, int(p[1])
dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > 0 and nx < 8 and ny > 0 and ny < 8:
        cnt += 1
print(cnt)
