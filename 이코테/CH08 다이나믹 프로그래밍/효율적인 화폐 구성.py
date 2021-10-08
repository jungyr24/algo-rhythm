# n개의 화폐를 가지고 최소 개수로 m원을 만들기
# 화폐 단위는 입력받는다 

n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))


d = [10001] * (m+1)

d[0] = 0

for i in range(n): # 화폐 개수
    for j in range(coin[i], m+1): # 현재 화폐에서 만들고자 하는 단위까지
       d[j] = min(d[j], d[j-coin[i]]+1) # 현재 화폐로 만들수 있는지 

if d[m] != 10001:
    print(d[m])
else:
    print(-1)

"""
2 15
3
4

3 4
3
5
7
"""