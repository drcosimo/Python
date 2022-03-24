import string
import random
userGuess: string = ""
numGuesses:int = 0
numberToGuess:int

while True:
    numberToGuess = random.randint(1,9)
    print("hai indovinato: " + str(numGuesses) + " volte")
    userGuess = input("prova a indovinare(exit per uscire)")
    
    if userGuess == "exit":
        print("ciao ciao")
        break
    
    userGuess = int(userGuess)
    guessed:bool = False
    while not guessed:
        if userGuess == numberToGuess:
            print("hai indovinato!")
            numGuesses += 1
            guessed = True
        elif userGuess > numberToGuess:
            userGuess = int(input("un pò piu basso, riprova"))
        elif userGuess < numberToGuess:
            userGuess = int(input("un pò più alto, riprova"))
