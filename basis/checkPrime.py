

num:int


def checkPrime(n:int): 
    isPrime:bool = True

    i:int = 2
    while i <= num/2 and isPrime:
        if num % i == 0:
            isPrime = False
        i += 1
    return isPrime

num = int(input("inserire numero\n"))

if(checkPrime(num)):
    print("è primo")
else:
    print("non è primo")
