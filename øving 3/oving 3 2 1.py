import math
def Omkrets(r):
    omkrets = format(math.pi * 2 * r, '.2f')
    return omkrets

def Areal(r):
    areal = format(math.pi * math.pow(r, 2),'.2f')
    return areal

def main():
    radius = input('skriv inn en radius ')
    print('Areal: ', Areal(float(radius)), '\nOmkrets: ', Omkrets(float(radius)))

main()
