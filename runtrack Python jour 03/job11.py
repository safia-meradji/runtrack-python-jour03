def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        hours = minutes // 60
        remaining_minutes = minutes % 60

        if hours == 1:
            hours_text = "1 heure"
        else:
            hours_text = f"{hours} heures"

        if remaining_minutes == 1:
            minutes_text = "1 minute"
        else:
            minutes_text = f"{remaining_minutes} minutes"

        print(f"{hours_text} et {minutes_text}")
    else:
        print("Veuillez entrer un nombre entier positif de minutes.")

# Demander à l'utilisateur d'entrer le nombre de minutes
user_input = input("Entrez le nombre de minutes : ")

# Convertir l'entrée en entier
try:
    user_minutes = int(user_input)
    # Appeler la fonction avec l'entrée de l'utilisateur
    time_to_text(user_minutes)
except ValueError:
    print("Veuillez entrer un nombre entier.")

