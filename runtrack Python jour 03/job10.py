def check_pair_or_odd(number):
    if isinstance(number, int) and number > 0:
        if number % 2 == 0:
            print(f"{number} est un nombre pair.")
        else:
            print(f"{number} est un nombre impair.")
    else:
        print("Veuillez entrer un chiffre entier et positif.")

# Demander à l'utilisateur d'entrer un nombre
user_input = input("Entrez un nombre entier positif : ")

# Convertir l'entrée en entier
try:
    user_number = int(user_input)
    # Appeler la fonction avec l'entrée de l'utilisateur
    check_pair_or_odd(user_number)
except ValueError:
    print("Veuillez entrer un nombre entier.")
