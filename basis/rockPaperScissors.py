import string
import random
choices :string = ["sasso","carta","forbice"]

userChoice: string = ""
computerChoice: string = ""

while True:
    userChoice = input("sasso carta o forbice?(quit per uscire)")
    if userChoice == "quit":
        break
    if userChoice in choices:
        #input valido
        computerChoice = choices[random.randint(0,2)]
        print("il computer butta... " + computerChoice)
        if (computerChoice == "sasso" and userChoice == "forbice") or (computerChoice == "forbice" and userChoice == "carta") or (computerChoice == "carta" and userChoice == "sasso"):
            print("hai perso") 
        elif computerChoice == userChoice:
                print("pareggio")
        else:
            print("hai vinto!")   
    else:
        print("non conosco questa opzione")