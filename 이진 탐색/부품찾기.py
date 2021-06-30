# 손님이 찾는 부품이 있는지 확인 있으면 yes 없으면 no 출력

n = int(input()) # 동빈이가 갖고 있는 부품
equipment = list(map(int, input().split()))
m = int(input()) # 손님이 찾는 부품
customer = list(map(int, input().split()))

equipment.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for e in customer:
    result = binary_search(equipment, e, 0, n-1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=' ')



# --------------
# 집합 자료형 이용해서 풀 수도 있음 
# --------------

"""
5
8 3 7 9 2
3
5 7 9
"""