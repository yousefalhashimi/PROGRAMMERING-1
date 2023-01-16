# Den här koden visar alla bollar som är i spel och vilken spelare som är börjar.
bollar =['o','o','o','o','o','o','o','o','o','o']
active_player = "player 1"
# Den här koden ger spelare val att välja 1 eller 2 bollar och tar bort antal bollar valt samt vem som vinner och man vill starta om spelet.
while True:
    valid =True
    print(*bollar)
    choice = int(input(active_player + " Pick 1 or 2 balls"))
    # om man väjer 1 så tas det bort 1 boll och går över till andra spelaren
    if choice == 1:
        bollar.pop()
    # om man väljer 2 så tas bort 2 bollar och går över till andra spelaren
    elif choice == 2 and len(bollar) > 1:
        bollar.pop()
        bollar.pop()
    # om man väljer nåt annat än 1 eller 2 så kommer det stå invalid för att det går ej att ta nåt annat
    else: 
        print("Invalid")
        valid = False
    # Den här koden är om den som tog sista bollen vinner och sen kan man starta om eller stänga av spelet
    if len(bollar) == 0:
        restart = input(active_player + " You Win! type yes to restart, type no to end game.").capitalize()
        if restart == "Yes":
            bollar =['o','o','o','o','o','o','o','o','o','o']
        else:
            break
# Den här koden gör så att spelarna turas om.
    if active_player == "player 1" and valid:
        active_player = "player 2"
    elif active_player == "player 2" and valid: 
        active_player = "player 1"
