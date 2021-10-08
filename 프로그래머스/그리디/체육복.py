# 전체학생 수 n, 체육복 없는 애들 lost배열, 여벌체육복 애들 reserve
# 체육수업 들을 수 잇는 학생의 최댓값

def solution(n, lost, reserve):
    answer = 0
    for s in lost[:]:
        if s in reserve:
            lost.remove(s)
            reserve.remove(s)

    for student in lost[:]:
        if student == 1:
            if student+1 in reserve:
                lost.remove(student)
                reserve.remove(student+1)
        elif student == n:
            if student-1 in reserve:
                lost.remove(student)
                reserve.remove(student-1)
        else:
            before = student-1
            next = student+1
            if before in reserve:
                lost.remove(student)
                reserve.remove(before)
                continue
            elif next in reserve:
                lost.remove(student)
                reserve.remove(next)
    answer = n - len(lost)
    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(2, [2], [2]))