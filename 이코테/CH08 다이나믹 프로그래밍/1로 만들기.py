# https://www.acmicpc.net/problem/1463
"""
정수 X가 주어질 때 가능한 연산
1. X가 5로 나누어 떨어지면 5로 나눈다.
2. X가 3로 나누어 떨어지면 5로 나눈다.
3. X가 2로 나누어 떨어지면 5로 나눈다.
4. X에서 1 뺀다.

연산 네가지를 적절히 사용하여 X를 1로 만들때 연산 사용 최솟값을 구하여라
"""

# 이코테 code ------------------------------------------------------------
import math

x = int(input())
d = [0] * 30001

# 바텀업 방식
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    
    # 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])


# 로밍맨 code https://www.youtube.com/watch?v=MsU1WeBAf2o ----------------
"""
1 -> 0
2 -> 1
3 -> 1
4 -> 2 ( 1{2로 나눈 것} +f(2))
5 -> 1
6 -> 
"""
# f(n) = 1 + min(f(n/3), f(n/2), f(n/5), f(n-1))

arr = [0, 0, 1, 1, 2] # 앞 부분 bottom-up으로 만들어 둔 것
for i in range(5, x+1):
    # n/3,   n/2,   n/5,    n-1
    d_three, d_two, d_five, m_one = math.inf, math.inf, math.inf, d[i-1]  # 나누는 거는 값이 없을 수도 있으니 무한대로 설정해둬서 뽑히지 않게 함
    
    if i % 3 == 0:
        d_three = arr[i//3]
    if i % 2 == 0:
        d_two = arr[i//2]
    if i % 5 == 0:
        d_five = arr[i//5]
    arr.append(1+ min(d_three, d_two, d_five, m_one))

print(arr[x])
