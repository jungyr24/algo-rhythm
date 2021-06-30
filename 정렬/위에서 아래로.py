# 수열을 내림차순으로 정렬하는 프로그램 만들기

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
print(arr)
