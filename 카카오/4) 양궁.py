max_diff = 0
max_info = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def check(count, index, info, apeach_info):
    global max_diff, max_info
    if count < 0:
        return

    if index == len(apeach_info)-1:
        if count > 0:
            info[index] = count
            count = 0

    if count == 0:
        ryan_total, apeach_total = 0, 0
        for i in range(len(info)):
            if info[i] == 0 and apeach_info[i] == 0:
                continue
            if info[i] > apeach_info[i]:
                ryan_total += (10-i)
            else:
                apeach_total += (10-i)

        if ryan_total <= apeach_total:
            return
        total = ryan_total-apeach_total

        
        if total == max_diff:
            for j in range(10, -1, -1):
                if info[j] > max_info[j]:
                    max_info = info
                    break
                elif info[j] < max_info[j]:
                    break
        elif total > max_diff:
            max_diff = total
            
            max_info = info
        return

    value = apeach_info[index]+1
    tmp = []
    for i in range(len(info)):
        if i == index:
            tmp.append(value)
        else:
            tmp.append(info[i])
    
    check(count-value, index+1, tmp,  apeach_info)
    check(count,       index+1, info, apeach_info)

def solution(n, info):
    global max_diff
    ryan_info = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    check(n, 0, ryan_info, info)

    if max_diff == 0:
        return [-1]
    else:
        return max_info