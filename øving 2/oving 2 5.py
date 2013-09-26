done = 'y'
def TimeLonn(hours, rate):
    lonn = float(hours) * float(rate)
    return lonn
def Provisjon(grunnblp, rate, sale):
    lonn = float(grunnblp) + (float(rate)/100) * float(sale)
    return lonn
def main():
    global done
    print('Velkommen til ReNew!')
    typeLonn = input('er den ansatte på [t]imelonn, eller [p]rovisjon?: ')
    sats = 0
    if(typeLonn == 't'):
        timeTall = input('Skriv inn antall timer: ')
        sats = input('skriv inn timesatsen: ')
        print('Den ansatte har tjent ', TimeLonn(timeTall, sats), 'kr')
    elif(typeLonn == 'p'):
        grunnbelop = input('Skriv inn et grunnbelop: ')
        sats= input('skriv inn prosentsatsen: ')
        salg = input('skriv inn totalt salg: ')
        print('Den ansatte har tjent ', Provisjon(grunnbelop, sats, salg), 'kr')
    else:
        print('Feil type input')
    done = input('Skriv x for aa avslutte ')

while(done !='x'):    
    main()
    
