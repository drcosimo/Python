
def fibonacci(n:int):
    numbers:int = []

    i:int=0
    prec:int=1
    cur:int=1
    app:int
    while i < n:
        app = cur
        cur += prec
        prec = app
        numbers.append(prec)
        i += 1
    return numbers

times:int

times = int(input("quanti numeri di fibonacci?"))

print(fibonacci(times))
