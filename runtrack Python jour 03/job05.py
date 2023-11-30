def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Gérer la division par zéro
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == "%":
        # Gérer la division par zéro
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Division par zéro"
    else:
        return "Opérateur non pris en charge"

# Exemples d'appels de la fonction
result_addition = calcule(5, "+", 3)
result_subtraction = calcule(10, "-", 4)
result_multiplication = calcule(6, "*", 7)
result_division = calcule(8, "/", 2)
result_modulo = calcule(11, "%", 3)

# Affichage des résultats
print("Addition:", result_addition)
print("Soustraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)
print("Modulo:", result_modulo)
