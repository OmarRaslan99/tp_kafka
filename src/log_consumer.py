"""Exercice 10 — Q3 : consommateur qui compte les hits par URL et par minute.

Lit le topic « logs », et pour chaque ligne "IP<TAB>URL" incrémente un compteur
`compteurs[minute][url]`. La minute est la minute courante au format
"AAAA-MM-JJ HH:MM" (dans la vraie vie on compterait plutôt par jour, et on
stockerait dans une base distribuée ; ici un simple dict Python suffit).

Le `group_id` permet de lancer plusieurs instances en parallèle (Q5) : Kafka
répartit alors les partitions entre les consommateurs du même groupe.
"""

from collections import defaultdict
from datetime import datetime

from kafka import KafkaConsumer

TOPIC = "logs"
BOOTSTRAP = "localhost:9092"


def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        group_id="log-counter",
        auto_offset_reset="latest",
        value_deserializer=lambda b: b.decode("utf-8"),
    )

    # compteurs[minute][url] = nombre de hits
    compteurs = defaultdict(lambda: defaultdict(int))

    print(f"Consommateur de logs démarré → topic '{TOPIC}' (Ctrl+C pour arrêter)")
    try:
        for message in consumer:
            # message.value = "IP<TAB>URL"
            _ip, _, url = message.value.partition("\t")
            minute = datetime.now().strftime("%Y-%m-%d %H:%M")
            compteurs[minute][url] += 1
            print(f"[p{message.partition}] [{minute}] {url} -> {compteurs[minute][url]}")
    except KeyboardInterrupt:
        print("\n--- Récapitulatif des hits par URL et par minute ---")
        for minute in sorted(compteurs):
            print(f"{minute} :")
            for url, nb in sorted(compteurs[minute].items(), key=lambda x: -x[1]):
                print(f"    {nb:4d}  {url}")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
