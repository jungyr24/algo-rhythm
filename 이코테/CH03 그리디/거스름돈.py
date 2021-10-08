# 가장 큰 화폐단위부터 거슬러주기
n = 1260
count = 0

coin_type = [500, 100, 50, 10]
for coin in coin_type:
    count += n // coin
    n %= coin

print(count)