t = int(input())

arr = list(map(int, input().split()))
for number in arr:
    total = 1
    for i in range(2, number):
        if number % i == 0:
            m1, m2 = i, number//i
            if m1 == m2:
                total + m1
            elif m1 < m2:
                total += (m1+m2)
            else:
                break 
    
    if total == number:
        if number == 1:
            print("Deficient")
        else:
            print("Perfect")
    elif total > number:
        print("Abendant")
    else:
        print("Deficient")