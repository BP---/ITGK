def Solve(number):
    numbersUsed = 0
    total = 0
    a = 1
    while total < number:
        
        total += a**2
        a +=1
                
        print((a-1), total)
    
    a -= 2
    return a
print(Solve(int(input('skriv tall '))))
