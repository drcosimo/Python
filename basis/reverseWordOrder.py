

import string

def reversePhrase(str:string):
    l = str.split(" ")
    l.reverse()
    str = ""
    for e in l:
        str += e + " " 
    return str

multiLineString:string = input("scrivi una frase")

print(reversePhrase(multiLineString))
