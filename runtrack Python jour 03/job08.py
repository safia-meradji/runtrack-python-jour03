def display_products(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Combinaison non prise en charge")

# Appels de la fonction avec différents paramètres
display_products("fruits", "hiver")
display_products("fruits", "ete")
display_products("legume", "hiver")
display_products("legume", "ete")
display_products("poisson", "ete")  # Pour tester la combinaison non prise en charge
