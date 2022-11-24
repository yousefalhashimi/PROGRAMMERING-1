username = input("Name:").capitalize()
score = 0
svar = input("Hur gammal är Dante?")
if svar == '69':
    print("Rätt svar")
    score = score + 1
else: 
    print("Fel svar! Rätt svar 69")
svar = input("Vilken linje går Dante i?").capitalize()
if svar == 'Teknik' :
        print("Rätt svar")
        score = score + 1
else:
    print("Fel svar! Rätt svar Teknik")
svar = input("Vem är Dantes bästa vän?").capitalize()
if svar == 'Steroids' :
    print("Rätt svar")
    score = score + 1
else:
    print("Fel svar! Rätt svar Steroids")
svar = input("Vad är Dantes hobby?").capitalize()
if svar == 'Gym':
    print("Rätt svar")
    score = score + 1
else:
    print("Fel svar! Rätt svar Gym")
print("Bra jobbat "+str(username)+" du fick "+str(score)+" av 4!")