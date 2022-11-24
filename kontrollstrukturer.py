import random

slumptal = random.randint(1,100)

while True:
    svar = int(input("Gissa på ett tal"))
    if svar == slumptal:
        print("Rätt svar")
        break
    elif svar < slumptal:
        print("Talet är större")
    elif svar > slumptal:
        print("Talet är mindre")
        



