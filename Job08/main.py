a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Le triangle est équilatéral.")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        if a == b or b == c or c == a:
            print("Le triangle est rectangle et isocèle.")
        else:
            print("Le triangle est rectangle.")
    elif a == b or b == c or c == a:
        print("Le triangle est isocèle.")
    else:
        print("Le triangle est quelconque.")
else:
    print("Il n'est pas possible de construire un triangle avec ces longueurs.")