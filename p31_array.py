import numpy as np

coins = [1,2,5,10,20,50,100,200]
total_money = 200

data = np.zeros((len(coins),total_money+1),dtype=np.int32)

for n in range(len(coins)):
    for m in range(total_money+1):
        if n == 0:
            data[n][m] = 1
        else:
            if m - coins[n] < 0:
                data[n][m] = data[n-1][m]
            else:
                data[n][m] = data[n][m-coins[n]] + data[n-1][m]

print(data[len(coins)-1][total_money])