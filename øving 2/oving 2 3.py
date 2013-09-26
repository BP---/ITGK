cont = 'y'
def Celcius(far):
    cel = (5/9)*(far-32)
    return cel
def main():
    global cont
    grader = input('skriv inn en temperatur i farenheit ')
    print(grader, 'grader farenheit er', format(Celcius(int(grader)),'.2f'), 'grader celcius')
    cont = input('skriv x for å avslutte ')
while (cont!='x'):
    main()
