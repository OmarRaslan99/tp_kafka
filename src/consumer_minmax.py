"""Exercice 9 — Q4 : consommateur qui calcule le minimum et le maximum.

Lit les nombres du topic « nombres » et affiche le min et le max courants à
chaque message reçu. Groupe dédié « minmax » (distinct de « moyenne ») : il
reçoit donc lui aussi tous les messages.
"""

from kafka import KafkaConsumer

TOPIC = "nombres"
BOOTSTRAP = "localhost:9092"


def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        group_id="minmax",
        auto_offset_reset="earliest",
        value_deserializer=lambda b: int(b.decode("utf-8")),
    )

    minimum = None
    maximum = None

    print(f"Consommateur 'minmax' démarré → topic '{TOPIC}' (Ctrl+C pour arrêter)")
    try:
        for message in consumer:
            valeur = message.value
            minimum = valeur if minimum is None else min(minimum, valeur)
            maximum = valeur if maximum is None else max(maximum, valeur)
            print(f"reçu : {valeur:5d}  |  min = {minimum:5d}  max = {maximum:5d}")
    except KeyboardInterrupt:
        print("\nArrêt du consommateur 'minmax'.")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
