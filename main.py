import json

class Dictionary:
    """
    Classe représentant un dictionnaire qui contient une liste de personnes.
    """
    def __init__(self):
        """
        Initialise une nouvelle instance de la classe Dictionary.
        """
        self.persons = []
    
    def add_person(self, person):
        """
        Méthode permettant d'ajouter une nouvelle personne à la liste des personnes.

        @param person: La personne à ajouter.
        @type person: Person
        """
        self.persons.append(person)

    def get_persons(self):
        """
        Méthode permettant de récupérer la liste des personnes.

        @return (list): La liste des personnes.
        """
        return self.persons
    
    def to_json(self):
        """
        Méthode permettant de convertir le dictionnaire en JSON.

        @return (str): Le dictionnaire converti en JSON.
        """
        return json.dumps([person.to_json() for person in self.persons], indent=2)

class Person:
    """
    Classe représentant une personne.
    """
    def __init__(self, age: int, first_name: str, gender: str):
        """
        Initialise une nouvelle instance de la classe Person.

        @param age (int): L'âge de la personne.
        @param first_name (str): Le prénom de la personne.
        @param gender (str): Le genre de la personne.
        """
        
        self.age = age
        self.first_name = first_name
        self.gender = gender
    
    def to_json(self):
        """
        Méthode permettant de convertir la personne en objet JSON.

        @return (dict): La personne convertie en dictionnaire.
        """
        return {
            "age": self.age,
            "first_name": self.first_name,
            "gender": self.gender
        }

# Création d'un dictionnaire
dictionary = Dictionary()

# Création de deux personnes
person1 = Person(25, "Alice", "female")
person2 = Person(30, "Bob", "male")

# Ajout des personnes au dictionnaire
dictionary.add_person(person1)
dictionary.add_person(person2)

# Affichage du dictionnaire
print("┌" + "─" * 18 + "[ dictionary ]" + "─" * 18 + "┐")
print(" ")
print(dictionary.to_json())
print(" ")
print("└" + "─" * 50 + "┘")
