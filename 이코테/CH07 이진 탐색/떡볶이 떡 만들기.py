# 갖고 있는 떡 들에서 기준 길이만큼 자르고 남은 자투리 떡들을 모아서 손님한테 판매
# 손님이 요청한 총 떡의 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

def binary(rice, target, start, end):
    global m_target
    if start > end:
        return m_target
    
    mid = (start+end) // 2
    
    # 떡 자르기
    total = 0
    for r in rice:
        if mid > r:
            continue
        total += (r-mid)
    
    # ------ 내 코드 --- 오답
    # if total == target:
    #     return mid

    # if total > target:
    #     m_target = mid
    #     return binary(rice, target, mid+1, end)
    # else:
    #     return binary(rice, target, start, mid-1)
    # ------------------

    if total < target: # 떡의 양이 부족하면 더 자르기
        return binary(rice, target, start, mid-1)
    else: # 떡의 양이 충분한 경우 덜자르기
        m_target = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기서 기록
        return binary(rice, target, mid+1, end)

n, m = map(int, input().split())
rice = list(map(int, input().split()))
m_target = 0
# rice.sort() 정렬 필요없음
result = binary(rice, m, 0, rice[-1])
print(result)


"""
4 6
19 15 10 17
"""