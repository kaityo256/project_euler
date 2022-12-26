from collections import defaultdict

memo = defaultdict(int)
coins = [1,2,5,10,20,50,100,200]
total_money = 200

def search(n, money):
    if memo[(n,money)]!=0:
        return memo[(n,money)]
    if money < 0:
        return 0
    if n == 0:
        return 1
    cases = search(n-1, money) + search(n, money-coins[n])
    memo[(n, money)] = cases
    return cases

print(search(len(coins)-1,total_money))
