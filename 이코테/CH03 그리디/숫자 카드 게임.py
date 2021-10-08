n, m = map(int, input().split())
card_max = []
for i in range(n):
    tmp = list(map(int, input().split()))
    card_max.append(min(tmp))
print(max(card_max))

"""
result = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    result = max(result, min(tmp))
print(result)
"""
