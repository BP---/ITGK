def GraadigeAlgoritmen(number, denominatorList):
    split = denominatorList
    res = []
    rest = number
    for x in range(len(split)):
        res.append(0)
    current = 0
    toomuch = False
    count = 1
    for x in range(len(split)):
        count = 1
        toomuch = False
        while not toomuch:
            current = count * split[x]
            if(current > rest):
                toomuch = True
                rest = rest - ((count -1)*split[x])
            else:
                res[x] = count
                count +=1
    return res

teeth = [95 , 103 , 71 , 99 , 114 , 64 , 95 , 53 , 97 , 114 , 109 , 11 , 2 , 21 , 45 , 2 , 26 , 81 , 54 , 14 , 118 , 108 , 117 , 27 , 115 , 43 , 70 , 58 , 107]
money = []
denoms = [20,10,5,1,0.5]
for x in range(len(teeth)):
    money.append(teeth[x] /2)

coinPurse = [0,0,0,0,0]

for x in range(len(money)):
    coins = GraadigeAlgoritmen(money[x], denoms)
    for y in range(len(coinPurse)):
        coinPurse[y] += coins[y]
    print(teeth[x], '=>', money[x], '=>', coins)

for x in range(len(coinPurse)):
    print(coinPurse[x],' ', denoms[x], '-kroninger, ', end='', sep='')
    
          



