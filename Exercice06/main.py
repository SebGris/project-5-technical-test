# Fonction calculate_average
def calculate_average(numbers):
    if not numbers:  # Vérifie si la liste est vide
        return 0
    total = sum(numbers)  # Calcule la somme des nombres
    count = len(numbers)  # Compte le nombre de nombres
    average = total / count  # Calcule la moyenne
    return average


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
