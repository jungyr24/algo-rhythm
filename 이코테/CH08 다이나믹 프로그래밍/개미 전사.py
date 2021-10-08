"""
메뚜기 식략 창고 터는데 인접한 창고는 털 수 없음
털어올 수 있는 최대 식량 구하기
"""
n = int(input())
storage = list(map(int, input().split()))

d = [0] * 100

d[0] = storage[0]
d[1] = max(d[0], storage[1])

for i in range(2, n):
    d[i] = max(d[i-1], storage[i]+d[i-2])   # 인접한 창고 식량과 현재 창고+2칸 앞 창고 식량의 합 중 큰 값 dp 테이블에 넣기
print(d[n-1])

"""
4
1 3 1 5
"""