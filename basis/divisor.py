
num:int
divisors:int = []

num = int(input("inserire numero"))

i:int = 1

while i < num:
    if num % i == 0:
        divisors.append(i)
    i += 1

print(divisors)

# crea una lista con i valori che vanno da 2 a 10
x : int = range(2,11)

