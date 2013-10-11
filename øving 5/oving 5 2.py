from BPfunctions import InputCheck
antall_kvinner = 0
antall_menn = 0
antall_sosmedier = 0
antall_facebook = 0
antall_timer_sosmedier = 0





def main():
    global antall_kvinner, antall_menn, antall_sosmedier, antall_facebook, antall_timer_sosmedier
    
    while True:
        kjonn = input('Hvilket kjønn er du? m/k ')
        if (kjonn == 'hade'):
            break
        if(kjonn == 'm'):
            antall_menn += 1
        else:
            antall_kvinner += 1

            
        age = input('Skriv inn alder: ')
        if (age == 'hade'):
            break
        age = int(age)
        if (age < 16 or age > 25):
            print('Du er utenfor aldersdomenet')
            continue


        
        aktiv_sosmedier = input('er du aktiv på sosiale medier? [ja/nei]: ')
        if(aktiv_sosmedier == 'hade'):
            break
        if(aktiv_sosmedier == 'nei'):
            continue
        antall_sosmedier += 1

        
        
        if(kjonn == 'k'):
            medlem_facebook = input('Mellom 55-60% av facebook sine brukere er kvinner. Er du en av disse? ')
        else:
            medlem_facebook = input('Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse?')
        if (medlem_facebook == 'hade'):
            break
        if(medlem_facebook == 'ja'):
            antall_facebook += 1


            
        timer_sosmedier = input('Hvor mage timer bruker du daglig på sosiale medier? ')
        if(timer_sosmedier == 'hade'):
            break
        antall_timer_sosmedier += int(timer_sosmedier)
    print('\n\nantall menn:', antall_menn, '\nantall kvinner:', antall_kvinner, '\naktive på sosiale medier:', antall_sosmedier, '\nbruker facebook', antall_facebook, '\ntid brukt på sosiale medier:', antall_timer_sosmedier)

main()

#variablene lagres i RAM. Etter selve koden er fullført kan du fortsatt
#se verdien til en variabel hvis du skriver den inn i python shellet
#Lukker du python shellet vil det bli tømt fra RAMen, og dermed borte        
