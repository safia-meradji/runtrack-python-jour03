def check_positivity(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("Le nombre est nul")

# Appels de la fonction avec différents paramètres
check_positivity(5)
check_positivity(-3)
check_positivity(0)
