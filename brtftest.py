import random

password = str(input("Store a 4-digit Pass: "))
guess = ""

while guess != password:
    guess = str(random.randint(0,9999))
    print("==>", guess)
    
    if guess == password:
        print("Password Found")
        print("==>", guess)
        break

