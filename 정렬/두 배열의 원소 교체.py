"""
동빈이가 가진 첫 번째 배열의 작은 수들을 두 번째 배열의 큰 수들과 바꿀 수 있다 k번
바꾸고 나서 동빈나가 가진 배열의 합을 구하여라
"""
n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)

for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i] = arr2[i] # 굳이 안 바꿔도 됨

print(sum(arr1))

"""
5 3
1 2 5 4 3
5 5 6 6 5
"""