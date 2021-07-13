# 조건을 만족하는 최장 수열 구하기
# LIS

t = int(input())

for _ in range(t):
    n = int(input())
    diamonds = []

    for i in range(n):
        w, c = map(float, input().split())
        diamonds.append((w, c))
    dp = [0 for _ in range(300)]
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if diamonds[j][0] < diamonds[i][0] and diamonds[j][1] > diamonds[i][1]:
                dp[i] = max(dp[j]+1, dp[i])
    res = max(dp)
    print(">>>>>>>>>>>>>>>>>>", res)