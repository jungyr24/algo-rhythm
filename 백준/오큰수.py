# http://boj.kr/17298
"""
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
"""
# 시간 초과
# n = int(input())
# array = list(map(int, input().split()))

# stack = []
# o_big = [-1] * n

# for i in range(n):
#     while stack and (array[i] > stack[-1][0]):
#         num, idx = stack.pop()
#         o_big[idx] = array[i]
#     stack.append((array[i], i))

# print(*o_big)



# 스택 이용
n = int(input())
array = list(map(int, input().split()))
result = [-1] * n
stack = []
for i in range(n):
    while stack and array[i] > stack[-1][0]:
        num, idx = stack.pop()
        result[idx] = array[i]
    stack.append((array[i], i))

print(*result)
        

"""
4
3 5 2 7

4
9 5 4 8
"""