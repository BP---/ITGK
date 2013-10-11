from BPfunctions import FromBin, ToBin
print('A = ',ord('A'), 'i titalssystemet og ', ToBin(ord('A')), 'i binæræ')
converters = ['01001100','01101001','01110011','01110000']
for x in range(len(converters)):
    print(converters[x], '=', FromBin(converters[x]),'=',chr(FromBin(converters[x])))

#metadata er data om data, en beskrivelse av hva slags data som finnes. 
