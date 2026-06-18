"""Exercice 14 — Q1/Q3 (+ Q5/Q6/Q7) : sérialisation Avro.

Crée une liste de personnes (dict), charge le schéma `user.avsc` et écrit le
tout dans `users.avro`. Le schéma inclut, en plus du nom et de l'âge :
- une liste de centres d'intérêt pris dans un enum (Q5/Q6),
- un champ optionnel `entreprise` (Q7).
"""

import os

import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

# Chemins relatifs à ce fichier (indépendants du répertoire courant).
ICI = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(ICI, "user.avsc")
SORTIE = os.path.join(ICI, "users.avro")

# Q1 : liste de dict décrivant des personnes.
personnes = [
    {
        "nom": "Omar",
        "age": 25,
        "interets": ["SPORT", "VOYAGE"],
        "entreprise": {"nom": "Padel SAS", "siret": "12345678900011", "effectifs": 12},
    },
    {
        "nom": "Priscile",
        "age": 23,
        "interets": ["LECTURE", "MUSIQUE", "CINEMA"],
        "entreprise": None,  # champ optionnel : pas d'employeur
    },
    {
        "nom": "Romain",
        "age": 24,
        "interets": ["CUISINE", "VOYAGE", "SPORT"],
        "entreprise": {"nom": "DataCorp", "siret": "98765432100022", "effectifs": 250},
    },
]


def main():
    schema = avro.schema.parse(open(SCHEMA, encoding="utf-8").read())

    with open(SORTIE, "wb") as f:
        writer = DataFileWriter(f, DatumWriter(), schema)
        for personne in personnes:
            writer.append(personne)
        writer.close()

    print(f"{len(personnes)} personnes sérialisées dans {SORTIE}")


if __name__ == "__main__":
    main()
