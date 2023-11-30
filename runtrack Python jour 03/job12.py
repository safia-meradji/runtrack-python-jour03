def reverse_string(input_string):
    return input_string[::-1]

# Demander à l'utilisateur d'entrer une chaîne de caractères
user_input = input("Entrez une chaîne de caractères : ")

# Appeler la fonction avec l'entrée de l'utilisateur
reversed_user_input = reverse_string(user_input)

# Afficher le résultat
print(f"Chaîne originale : {user_input}")
print(f"Chaîne inversée : {reversed_user_input}")

