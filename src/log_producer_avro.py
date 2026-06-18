"""Exercice 17 — producteur de logs encodés en Avro.

Reprend le générateur de logs de l'Exo 10, mais encode **clé et valeur en Avro**
et publie dans le topic « logs-avro ». La version du schéma de valeur utilisée
est transmise dans un **header Kafka** `schema_version`, ce qui permet au
consommateur de gérer plusieurs versions (Q4).

Usage : uv run python src/log_producer_avro.py <numusers> <numurls> [version]
  version = 1 (ip,url) | 2 (+datetime,taille) | 3 (+headers HTTP), défaut 1
"""

import os
import random
import sys
import time
from datetime import datetime

from kafka import KafkaProducer

from avro_utils import load_schema, serialize

TOPIC = "logs-avro"
BOOTSTRAP = "localhost:9092"
ICI = os.path.dirname(os.path.abspath(__file__))

KEY_SCHEMA = load_schema(os.path.join(ICI, "log_key.avsc"))
VALUE_SCHEMAS = {
    1: load_schema(os.path.join(ICI, "log_value_v1.avsc")),
    2: load_schema(os.path.join(ICI, "log_value_v2.avsc")),
    3: load_schema(os.path.join(ICI, "log_value_v3.avsc")),
}

# Valeurs aléatoires pour les headers HTTP (v3) — non exploitées.
REFERERS = ["https://www.google.com", "https://www.bing.com", "https://t.co", "-"]
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "curl/8.4.0",
]


def randomip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def randomstring(n):
    charset = "abcdefghikjlmnopqrstuvwxyzABCDEFGHIKJLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(charset) for _ in range(n))


def randomurl():
    return "https://localhost/" + randomstring(random.randint(4, 16))


def build_value(version, ip, url):
    """Construit l'enregistrement valeur selon la version demandée."""
    valeur = {"ip": ip, "url": url}
    if version >= 2:
        valeur["datetime"] = datetime.now().isoformat(timespec="seconds")
        valeur["taille"] = random.randint(0, 10_000_000)
    if version >= 3:
        valeur["headers"] = {
            "referer": random.choice(REFERERS),
            "user_agent": random.choice(USER_AGENTS),
        }
    return valeur


def main():
    if len(sys.argv) not in (3, 4):
        print("usage: %s numusers numurls [version]" % sys.argv[0])
        return

    nusers = int(sys.argv[1])
    nurls = int(sys.argv[2])
    version = int(sys.argv[3]) if len(sys.argv) == 4 else 1

    users = [randomip() for _ in range(nusers)]
    urls = [randomurl() for _ in range(nurls)]
    usersw = [2 ** i / (2 ** (i + 1) - 1) for i in range(nusers)]
    urlsw = [2 ** i / (2 ** (i + 1) - 1) for i in range(nurls)]

    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP)  # clé/valeur déjà en bytes

    print(f"Producteur Avro démarré → topic '{TOPIC}' (version={version}, Ctrl+C pour arrêter)")
    try:
        while True:
            user = random.choices(users, usersw)[0]
            url = random.choices(urls, urlsw)[0]
            cle = serialize(KEY_SCHEMA, {"url": url})
            valeur = serialize(VALUE_SCHEMAS[version], build_value(version, user, url))
            producer.send(
                TOPIC,
                key=cle,
                value=valeur,
                headers=[("schema_version", str(version).encode("utf-8"))],
            )
            print(f"envoyé (v{version}) : {user}\t{url}")
            time.sleep(random.random() * 2)
    except KeyboardInterrupt:
        print("\nArrêt du producteur Avro.")
    finally:
        producer.flush()
        producer.close()


if __name__ == "__main__":
    main()
