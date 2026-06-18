"""Exercice 10 — Q2 : producteur de logs vers Kafka.

Version Kafka du script fourni `ressources/genlogs.py` : au lieu d'imprimer les
lignes de log sur la sortie standard, on les publie dans le topic « logs ».

Format d'une ligne : "IP<TAB>URL". On met l'URL en **clé** du message pour que
tous les hits d'une même URL aillent sur la même partition (comptage cohérent
quand on parallélise les consommateurs, cf. Exo 6).

Usage : uv run python src/log_producer.py <numusers> <numurls>
"""

import random
import sys
import time

from kafka import KafkaProducer

TOPIC = "logs"
BOOTSTRAP = "localhost:9092"


# --- Helpers repris de genlogs.py (matériel fourni) -------------------------
def randomip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def randomstring(n):
    charset = "abcdefghikjlmnopqrstuvwxyzABCDEFGHIKJLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(charset) for _ in range(n))


def randomurl():
    return "https://localhost/" + randomstring(random.randint(4, 16))


def main():
    if len(sys.argv) != 3:
        print("usage: %s numusers numurls" % sys.argv[0])
        return

    nusers = int(sys.argv[1])
    nurls = int(sys.argv[2])

    users = [randomip() for _ in range(nusers)]
    urls = [randomurl() for _ in range(nurls)]

    # Pondérations : certaines IP / URL sont bien plus populaires que d'autres.
    usersw = [2 ** i / (2 ** (i + 1) - 1) for i in range(nusers)]
    urlsw = [2 ** i / (2 ** (i + 1) - 1) for i in range(nurls)]

    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP,
        key_serializer=lambda k: k.encode("utf-8"),
        value_serializer=lambda v: v.encode("utf-8"),
    )

    print(f"Producteur de logs démarré → topic '{TOPIC}' (Ctrl+C pour arrêter)")
    try:
        while True:
            user = random.choices(users, usersw)[0]
            url = random.choices(urls, urlsw)[0]
            ligne = "%s\t%s" % (user, url)
            # Clé = URL → hits d'une même URL sur la même partition.
            producer.send(TOPIC, key=url, value=ligne)
            print("envoyé :", ligne)
            time.sleep(random.random() * 2)
    except KeyboardInterrupt:
        print("\nArrêt du producteur de logs.")
    finally:
        producer.flush()
        producer.close()


if __name__ == "__main__":
    main()
