import math
def OverflateKule(radius):
    overflate = 4 * math.pi * math.pow(radius, 2)
    overflate = format(overflate,'.2f')
    return overflate

def Volum(radius):
    volum = (4 * math.pi * math.pow(radius, 3))/3 
    #volum = format(volum,'.2f')
    volum = round(volum, 2)
    return volum


radius = float(input('Skriv inn en radius: '))
print('Overflaten på en kule med radius', radius, 'er', OverflateKule(radius))
print('Volumet er', Volum(radius))


