
import random as rd

# matrix holder
matrix:int = [[[]]]

def generateMatrix(matrix,n):
    i=0
    j=0
    #inizializzo la matrice
    matrix = [[[0 for k in range(1)] for j in range(n)] for i in range(n)]
    # popolo randomicamente
    while i < n:
        j=0
        while j < n:
            matrix[i][j][0] = rd.randint(0,3)
            j += 1
        i += 1

    return matrix

def calculateDeterminant(matrix,det):
    i = 0
    j = 0
    l = len(matrix)
    if l == 2:
        # det = ac - bd
        return sum(multiply(matrix[0][0],matrix[1][1]),multiply(matrix[0][1],matrix[1][0]),-1) 

    # per ogni elemento della prima colonna
    while i < l:
        # trovo la sottomatrice di cui calcolare il determinante
        subMat = findMat(matrix,i,l)
        # accumulo il determinante
        multiplier:int = [(-1)**i*matrix[i][0][j] for j in range(len(matrix[i][0]))]
        det = sum(multiply(calculateDeterminant(subMat,det),multiplier),det,1)
        i+=1

    return det

# trovo la sotto matrice per il calcolo del determinante in base alla posizione attuale
def findMat(matrix,pos,l):
    subMatrix = [[0 for i in range(l-1)] for j in range(l-1)]
    k = 0
    h = 0

    # trovo la sottomatrice lungo la prima colonna
    for i in range(l):
        for j in range(1,l):
            # abilitazione alla scrittura
            if i != pos :
                # salvo il valore
                subMatrix[k][h] = matrix[i][j]
                # scelta dell incremento
                if h == l-2:
                    k += 1
                    h = 0
                else:
                    h += 1
    return subMatrix

#somma tra due equazioni
def sum(e1,e2,sign):
    l1 = len(e1)
    l2 = len(e2)
    mx = e1 if max(l1,l2) == l1 else e2
    start = min(l1,l2)
    #inizializzo il risultato
    res = [0 for i in range(max(l1,l2))]

    for i in range(len(mx)):
        # ultimo caso
        if l1 != l2 and i == start:
            # nel caso in cui una delle 2 equazioni abbia piu termini dell'altra
            for j in range(i,i+abs(l1-l2)): 
                res[j] = mx[j]
            break
        else:
            # altri termini
            if sign > 0:
                res[i] = e1[i] + e2[i]
            else:
                res[i] = e1[i] - e2[i]

    return res


# moltiplicazione tra due equazioni
def multiply(e1,e2):
    l1 = len(e1)
    l2 = len(e2)
    mx = max(len(e1),len(e2))
    #inizializzo il risultato
    res = [0 for i in range(mx+1)]

    for i in range(l1):
        for j in range(l2):
            # altri gradi
            if not (i == 0 and j == 0): 
                res[i+j] += e1[i]*e2[j]
            else:
                # primo grado 
                res[0] += e1[i]*e2[j]
    return res

def stampa(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(str(m[i][j]), end="")
        print()

def clean(m):
    for i in range(len(m)-1,0):
        if m[i] != 0:
            break
        m.remove(i)
    return m

matrix = generateMatrix(matrix,3)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            matrix[i][j].append(-1)



stampa(matrix)
print("\n")


print(calculateDeterminant(matrix,[0 for i in range(1)]))

# FUNZIONANTE => calcolo polinomio caratteristico
# DA FARE => risoluzione equazione