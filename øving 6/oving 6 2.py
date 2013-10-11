li = [1,2,3,4,5,6]


def NegPartall(liste):
    for x in range(len(liste)):
        if(liste[x]%2==0):
            liste[x] = liste[x] * -1
    return liste

print(NegPartall(li))
li.reverse()
print(li)
