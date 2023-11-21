N = int(input("Entrez un nombre entier supérieur à zéro : "))
if N > 0:
    for i in range(1, N+1):
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}")
else:
    print("Veuillez entrer un nombre entier supérieur à zéro.")
