def sign_of(tall):
    backText = ''
    if(tall<0):
        backText = 'Tallet er negativt'
    elif(tall==0):
        backText = 'Tallet er null'
    else:
        backText = 'Tallet er positivt'
    return backText
number = int(input('skriv inn et heltall '))
print(sign_of(number))
                   
