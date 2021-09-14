import math
def check_prime(num):
    for i in range(2, int(math.sqrt(num)) +1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    reversed_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        reversed_base += str(mod)
    base = reversed_base[::-1]  # k진수
    
    for num in base.split("0"):
        if len(num) == 0 or num == '1':
            continue
        
        if check_prime(int(num)):
            answer += 1






    return answer

print(solution(437674, 3))
print(solution(110011, 10))