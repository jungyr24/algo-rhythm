def solution(lottos, win_nums):
    answer = []

    zero_cnt = 0
    right_cnt = 0
    for num in lottos:
        if num == 0:
            zero_cnt += 1
        elif num in win_nums:
            right_cnt += 1

    high = 6 if right_cnt + zero_cnt == 0 else 7 - (right_cnt + zero_cnt)
    low = 6 if right_cnt == 0 else 7-right_cnt
    answer.append(high)
    answer.append(low)

    return answer

def a_solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)
    ans = 0
    for num in lottos:
        if num in win_nums:
            ans += 1
    
    return rank[cnt_0+ans], rank[ans]


print(a_solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(a_solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(a_solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))