debug = False
def Adder(nr1, nr2):
    global debug
    if(debug == True):
        print('tallene som legges sammen er', nr1, 'og', nr2)
    ans = int(nr1)+int(nr2)
    return ans
def main():
    global debug
    global cont
    reqDebug = input('vil du debugge? (y/n)')
    if (reqDebug == 'y'):
        debug = True
    elif(reqDebug == 'n'):
        debug = False
    else:
         debug = False
    tall1 = input('skriv inn et tall: ')
    tall2 = input('Skriv inn et nytt tall: ')
    print(str(Adder(int(tall1), int(tall2))))
    cont = input('skriv x for å avslutte ')

cont = 'y'
while cont != 'x':
    main()
    
         
         
    
