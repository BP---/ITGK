import math
def VektorList(a, b, c):
    vektor = [a,b,c]
    return vektor

def SkalarMultiply(vektor, skalar):
    for x in range(len(vektor)):
        vektor[x] = vektor[x] * skalar
    return vektor
        
def VectorLength(vektor):
    length = 0
    for x in range(len(vektor)):
        length += vektor[x]**2
    length = math.sqrt(length)
    return length
def VektorProdukt(vektor1, vektor2):
    produkt = 0
    for x in range(len(vektor1)):
        produkt += vektor1[x] * vektor2[x]
    return produkt

a = VektorList(int(input('tall1 ')), int(input('tall2 ')), int(input('tall3 ')))
print(a)
b = VectorLength(a)
print(format(b,'.2f'))
a = SkalarMultiply(a,int(input('tall ')))
c = VectorLength(a)
print(a, format(c,'.2f'), ',', format((c-b),'.2f'))
d = VektorList(int(input('tall1 ')), int(input('tall2 ')), int(input('tall3 ')))
print(VektorProdukt(a,d))

