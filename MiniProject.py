import random
target=random.randint(1,100)

while True:

    userChoice= (input("Gusee the target or Quit (Q):"))
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)

    if(userChoice == target):
         print("Sucess: Correct Guess")
         break
    elif (userChoice < target):
         print("Your number was too small.Take a large number")
    else:
          print("Your number was too big.Take a small number")

print("----Game Over----")
