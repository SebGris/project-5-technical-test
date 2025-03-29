students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
    'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

name = input("“Entrez le nom de l’étudiant : ")
if name in students:
    print(f"Notes de {name} :")
    for subject, grade in students[name].items():
        print(f"{subject}: {grade}")
    average = sum(students[name].values()) / len(students[name])
    print(f"Moyenne de {name} : {average:.2f}")
else:
    print(f"L'étudiant {name} n'existe pas dans la liste.")
