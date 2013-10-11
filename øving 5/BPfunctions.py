import math

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


def IsPrime(tall):
    prime = True
    for x in range(2, tall):
        if(tall%x==0):
            prime = False
    return prime


def InputCheck(dataType, prompt, errorMsg):
    a = 0
    while True:
        if(dataType == 'int'):
            try:
                    a = int(input(prompt))
                    break
            except ValueError:
                    print(errorMsg)
        elif(dataType == 'string'):
            try:
                a = str(input(prompt))
                break
            except ValueError:
                print(errorMsg)
        elif(dataType == 'float'):
            try:
                a = float(input(prompt))
                break
            except ValueError:
                print(errorMsg)
        elif(dataType == 'bin'):
            a = input(prompt)
            a = str(a)
            invalChar = False
            for x in range(len(a)):
                if(a[x] != '0' and a[x] != '1'):
                    invalChar = True
                    break
            if(invalChar == False):
                break
            else:
                print(errorMsg)
    return a


def ToBin(tall):
    less = True
    i = 0
    rest = tall
    product = ''
    while less:
        if(math.pow(2,i) > tall):
            less = False
            i = i-1
            break
        i+=1
    for x in range(i,-1,-1):
        if(math.pow(2,i) <= rest):
            product += '1'
            rest = rest - math.pow(2,i)
        else:
            product += '0'
        i-=1
    return product
        

def FromBin(tall):
    tall = str(tall)
    tiTall = 0
    for x in range(len(tall)):
        if(int(tall[x])==1):
            tiTall += int(math.pow(2,(len(tall)-1)-x))
    return tiTall


def StringToChar(string):
    chars = []
    for x in range(len(string)):
        chars.append(ord(string[x]))
    return chars

def CharToBin(charList):
    bins = []
    for x in range(len(charList)):
        bins.append(ToBin(charList[x]))
    return bins

def RevKonkat(string, extras):
    zeros = ''
    string = str(string)
    for x in range(extras):
        zeros += '0'
    result = zeros + string
    return result
def GetLargestLenght(strList):
    if(len(strList)>=1):        
        maxLen = len(strList[0])
    else:
        maxLen = 0
    for x in range(1, len(strList)):
        if(len(strList[x]) > (len(strList[x-1]))):
            maxLen = len(strList[x])
    return maxLen


def MakeEvenList(strList):
    maxLen = GetLargestLenght(strList)
    for x in range(len(strList)):
        strList[x] = RevKonkat(strList[x], (maxLen - len(strList[x])))
    return strList

def StringToBin(string):
    binList = MakeEvenList(CharToBin(StringToChar(string)))
    outString = ''
    for x in range(len(binList)):
        outString += binList[x]
    return outString


def Fakultet(tall):
    summen = 1
    for x in range(1,(tall+1)):
        summen = summen * x
    return summen


def FindEndZeros(tall):
    tall = str(tall)
    zero = 0
    for x in range(len(tall)):
        if(tall[x] == '0'):
            zero += 1
        else:
            zero = 0
    return zero


def gcd(tall1, tall2):
    a= tall1
    b= tall2
    holder = 0
    gcd = 0
    done = False
    while not done:
        holder = a
        a = b
        b = holder%b
        if(b==0):
            gcd = a
            done = True
    return gcd


def lcm(tall1, tall2):
    a = 2
    while True:
        if(a*tall1%tall2 ==0):
            break
        a += 1
    a = a*tall1
    return a


def ReduceFraction(tall1, tall2):
    divisor = gcd(tall1, tall2)
    tall1 = tall1 / divisor
    tall2 = tall2 / divisor
    return tall1, tall2



def FibbonacciList(endNumber):
    fibList = []
    if(endNumber == 1):
        fibList = [0]
        
    elif(endNumber ==2):
        fibList = [0,1]
    else:    
        fibList = [0,1]
        
        
        for x in range(2, endNumber+1):
            fibList.append(fibList[x-1] + fibList[x-2])

    return fibList
                       
    





