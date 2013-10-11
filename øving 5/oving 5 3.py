from BPfunctions import gcd, ReduceFraction, InputCheck

go = 'y'
while go != 'n':
    a = InputCheck('int', 'Skriv inn et tall', 'Ikke et heltall, prøv igjen')
    b = InputCheck('int', 'Skriv inn et tall', 'Ikke et heltall, prøv igjen')
    print(gcd(a,b))
    a, b = ReduceFraction(a,b)
    print(int(a),'/',int(b), sep='')
    go = input('skriv n for å avslutte')


    
