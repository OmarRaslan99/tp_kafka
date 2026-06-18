"""Exercice 9 — Q2 : producteur de nombres aléatoires.

Génère un nombre aléatoire entre 0 et 10000 toutes les secondes et l'envoie
dans le topic Kafka « nombres ». Arrêt propre avec Ctrl+C.
"""

import random
import time

from kafka import KafkaProducer

TOPIC = "nombres"
BOOTSTRAP = "localhost:9092"


def main():
    # value_serializer : on transmet l'entier sous forme de texte encodé en octets.
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP,
        value_serializer=lambda v: str(v).encode("utf-8"),
    )

    print(f"Producteur démarré → topic '{TOPIC}' (Ctrl+C pour arrêter)")
    try:
        while True:
            nombre = random.randint(0, 10000)
            producer.send(TOPIC, nombre)
            print(f"envoyé : {nombre}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nArrêt du producteur.")
    finally:
        producer.flush()
        producer.close()


if __name__ == "__main__":
    main()
