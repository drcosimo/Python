from operator import truediv
import string
from xmlrpc.client import boolean


stringa:string

stringa = input("inserire stringa")

print(stringa[0:])

isntPalindroma:boolean = False


i:int = 0
while i < len(stringa) / 2 and not isntPalindroma:
    if stringa[i] != stringa[len(stringa)-i-1]:
        isntPalindroma = True
    i += 1

if not isntPalindroma:
    print("è palindroma")
else:
    print("non è palindroma")