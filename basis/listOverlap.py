import random

#genero casualmente 2 liste

a:int = []
b:int = []
c:int = []
while len(a) < 10:
    a.append(random.randint(1,30))
    b.append(random.randint(1,30))

print(a)
print(b)
# trovo i duplicati
for n in a:
    if n in b:
        c.append(n)

print(c)

# in una riga di codice
c = [n for n in a if n in b]
print(c)