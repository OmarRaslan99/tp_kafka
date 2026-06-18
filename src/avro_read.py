"""Exercice 14 — Q4 : lecture d'un fichier Avro.

Relit `users.avro` et affiche chaque personne. Le schéma est embarqué dans le
fichier Avro : il n'est donc pas nécessaire de le fournir pour relire.
"""

import os

from avro.datafile import DataFileReader
from avro.io import DatumReader

ICI = os.path.dirname(os.path.abspath(__file__))
FICHIER = os.path.join(ICI, "users.avro")


def main():
    with open(FICHIER, "rb") as f:
        reader = DataFileReader(f, DatumReader())
        for personne in reader:
            print(personne)
        reader.close()


if __name__ == "__main__":
    main()
