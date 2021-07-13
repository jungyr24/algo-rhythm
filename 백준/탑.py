n = int(input())
building = list(map(int, input().split()))
result = [0] * n

stack = []
for i in range(n-1, -1, -1):
    # print("---")
    # print("탑:", building[i])
    while stack and stack[-1][0] < building[i]:
        height, idx = stack.pop()
        result[idx] = i+1
    stack.append((building[i], i))
    # print("stack:", stack)


print(*result)