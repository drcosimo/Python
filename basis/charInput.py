
import string

from datetime import date as dt

name:string
age:int

# ottengo l'anno attuale
year:int = dt.today().year

# chiedo nome e anno
name = input("inserisci il nome")
age = int(input("inserisci età"))

if age < 100 :
    # calcolo quando ha 100 anni
    vecchio:int = year + (100-age)

    # chiedo quante volte
    n:int = int(input("quante volte te lo devo di?"))

    # stampo n volte
    i:int = 0

    while i<n:
        print(name + " farai 100 anni nel " + str(vecchio))
        i+=1
else :
    print("gia li hai fatti 100 anni")
# occhio ai tipi nelle concatenazioni