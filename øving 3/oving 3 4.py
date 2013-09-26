def Pricing(age):
    price = 0
    if (age < 5):
        price = 0
    elif(age >= 5 and age <=15):
        price = 10
    elif(age >=16 and age <= 20):
        price = 20
    elif(age >=21 and age <= 25):
        price = 30
    elif(age >= 25 and age <= 60):
        price = 40
    else:
        price = 0
    return price
def main():
    global cont
    alder = input('alder: ')
    print('Du må betale', str(Pricing(int(alder))), 'kr')
    cont = input('\nskriv x for å avslutte ')
cont = 'y'
while(cont != 'x'):
    main()    
