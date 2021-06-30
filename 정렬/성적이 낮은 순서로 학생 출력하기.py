# 튜플 이용

n = int(input())
students = []
for i in range(n):
    name, score = input().split()
    students.append((name, int(score)))

students = sorted(students, key=lambda student: student[1])
for student in students:
    print(student[0], end=' ')

"""
2
홍길동 95
이순신 77
"""