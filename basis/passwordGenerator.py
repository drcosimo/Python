import random as rd


sicurezza:int = int(input("quanto forte la password? [1,5]"))

def generatePasswd(forza):
    pwd = ""

    i=0
    while i < forza*5:
        ch = chr(rd.randint(20,84))
        if(ch != " "):
            pwd += ch
            i += 1
    return pwd

print(generatePasswd(sicurezza))    