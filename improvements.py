import json
import requests

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
    def __init__(self, phone: str, name: str, company: str):
        """
        Initialise une nouvelle instance de la classe Person.

        @param phone (str): L'âge de la personne.
        @param name (str): Le prénom de la personne.
        @param company (str): Le genre de la personne.
        """
        
        self.phone = phone
        self.name = name
        self.company = company
    
    def to_json(self):
        """
        Méthode permettant de convertir la personne en JSON.

        @return (dict): La personne convertie en dictionnaire.
        """
        return {
            "phone": self.phone,
            "name": self.name,
            "company": self.company
        }

# Création d'un dictionnaire
dictionary = Dictionary()

# Récupération des données depuis l'API
response = requests.get("https://jsonplaceholder.typicode.com/users")

# Ajout des personnes au dictionnaire
for person in response.json():
    dictionary.add_person(Person(person["phone"], person["name"], person["company"]["name"]))

# Affichage du dictionnaire
print("┌" + "─" * 18 + "[ dictionary ]" + "─" * 18 + "┐")
print(" ")
print(dictionary.to_json())
print(" ")
print("└" + "─" * 50 + "┘")
