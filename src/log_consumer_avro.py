"""Exercice 17 — consommateur de logs Avro, compatible plusieurs versions.

Lit le topic « logs-avro », décode la clé et la valeur en Avro. Pour la valeur,
on lit le header Kafka `schema_version` afin de choisir le **schéma d'écriture**,
puis on décode en **résolvant** vers le schéma le plus récent (v3) : les champs
absents des anciennes versions sont comblés par leurs valeurs par défaut.
Un même consommateur gère ainsi les v1, v2 et v3 (Q4).
"""

import os

from kafka import KafkaConsumer

from avro_utils import deserialize, load_schema

TOPIC = "logs-avro"
BOOTSTRAP = "localhost:9092"
ICI = os.path.dirname(os.path.abspath(__file__))

KEY_SCHEMA = load_schema(os.path.join(ICI, "log_key.avsc"))
VALUE_SCHEMAS = {
    1: load_schema(os.path.join(ICI, "log_value_v1.avsc")),
    2: load_schema(os.path.join(ICI, "log_value_v2.avsc")),
    3: load_schema(os.path.join(ICI, "log_value_v3.avsc")),
}
READER_SCHEMA = VALUE_SCHEMAS[3]  # schéma le plus récent (lecture uniforme)


def version_from_headers(headers):
    """Récupère le numéro de version dans les headers Kafka (défaut 1)."""
    entetes = dict(headers or [])
    return int(entetes.get("schema_version", b"1").decode("utf-8"))


def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        group_id="log-avro-counter",
        auto_offset_reset="earliest",
    )

    print(f"Consommateur Avro démarré → topic '{TOPIC}' (Ctrl+C pour arrêter)")
    try:
        for message in consumer:
            version = version_from_headers(message.headers)
            cle = deserialize(KEY_SCHEMA, KEY_SCHEMA, message.key)
            valeur = deserialize(VALUE_SCHEMAS[version], READER_SCHEMA, message.value)
            print(f"[v{version}] cle={cle['url']}  valeur={valeur}")
    except KeyboardInterrupt:
        print("\nArrêt du consommateur Avro.")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
