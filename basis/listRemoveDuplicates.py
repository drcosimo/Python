from gettext import find
import random as rd

def rmv_sets(l1:int= []):
    return [e for id,e in enumerate(l1) if isFirst(l1,e,id)]


def rmvElement(l,e):
    app:int = l.copy()
    app.remove(e)
    return app

def isFirst(l,e,id):
    return l.index(e) == id

def generateList(n,range):
    a = []
    i=0
    while i < n:
        a.append(rd.randint(1,range))
        i+=1
    return a

dim = int(input("grandezza lista"))
range = int(input("fine range"))
l = generateList(dim,range)
print(l)
print(rmv_sets(l))




