# 반복되는 수열 파악
# [ 제일 큰수 * k + 그 다음으로 큰 수 ]
# ex) [6 6 6 5][6 6 6 5]

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
first, second = arr[0], arr[1]
result = 0
count = int(m / (k+1)) * k

result = count * first
result += (m-count) * second

print(result)