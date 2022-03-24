
num1:int
num2:int

num1 = int(input("inserire numero"))

if num1 % 2 == 0:
    if num1 % 4 == 0:
        print("è anche multiplo di 4")
    else:
        print("è pari")
else:
    print("è dispari")


num2 = int(input("inserire altro numero"))

if num1 % num2 == 0:
    print("è un divisore di num1")
else:
    print("non è un divisore di num1")