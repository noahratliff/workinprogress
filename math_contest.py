import numpy as np


def checkPerim(h, l):
    return(2*h+2*l)


def area(h, l):
    return(h*l)


def correct(h1, l1, h2, l2):
    if checkPerim(h1, l1) == 2*(checkPerim(h2, l2)):
        if area(h2, l2) == 2*area(h1, l1):
            return(h1, l1, h2, l2)
        else:
            pass
    else:
        pass


i = 50

h1 = []
l1 = []
h2 = []
l2 = []
combos = []

while i > 0:
    h1.append(i)
    l1.append(i)
    h2.append(i)
    l2.append(i)
    i += -1

for i in h1:
    for o in h2:
        for p in l1:
            for u in l2:
                combos.append([i, p, o, u])

print(combos[0])
for i in reversed(combos):
    h1, l1, h2, l2 = i
    if correct(h1, l1, h2, l2) == None:

        pass
    else:
        print(i)
