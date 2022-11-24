# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna


def best(name):
    print(name,"är bäst")
    # TODO Skriv ut att namnet är bäst
    # Ex: "Katherine" in - skriver ut "Katherine är bäst"
    
best("Alex")


def square(number):
    # TODO Returnera talet kvadrerat
    # Ex: 5 in - 25 ut
    return number**2
print(square(10))



def sums(a, b):
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
    return a + b
print(sums(3,8))

# Nu blir det lite svårare


def maximum(a, b, c):
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    if a > b and a > c:
        return a
    elif b>a and b>c:
        return b
    else: return c
print(maximum(7,14,3))


