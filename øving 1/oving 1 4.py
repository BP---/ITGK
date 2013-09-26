a = "y"
antallMsg = 1
def logg(navn, tid, melding, nrmsg):
    #print('Msg',nrmsg, 'Klokken', tid, 'sendte', navn, 'foelgende melding: "',melding,'"')
    utTekst = 'Msg ' + str(nrmsg) + ': Klokken ' + tid + ' sendte ' + navn + ' foelgende melding: "' + melding + '"'
    return utTekst
def main():
    global antallMsg
    global a
    navn = input('Navn: ')
    tid = input('Naar?: ')
    msg = input('Melding: ')
    print('\n')
    print(logg(navn, tid, msg, antallMsg),'\n\n')
    antallMsg += 1
    a = input('skriv "x" for aa avslutte ')
while( a != "x"):
    main()

