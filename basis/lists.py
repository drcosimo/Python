a:int = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b:int = []

for n in a:
    if n < 5:
        b.append(n)

print(b)

c:int = []

num:int = int(input("inserire un numero"))

for n in a:
    if n < num: 
        c.append(n)

print(c)
