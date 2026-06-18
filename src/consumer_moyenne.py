"""Exercice 9 — Q3 : consommateur qui calcule la moyenne.

Lit les nombres du topic « nombres » et affiche la moyenne courante à chaque
message reçu. Groupe dédié « moyenne » : il reçoit donc tous les messages,
indépendamment du consommateur min/max (modèle publish/subscribe, cf. Exo 7).
"""

from kafka import KafkaConsumer

TOPIC = "nombres"
BOOTSTRAP = "localhost:9092"


def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        group_id="moyenne",
        auto_offset_reset="earliest",
        value_deserializer=lambda b: int(b.decode("utf-8")),
    )

    somme = 0
    compte = 0

    print(f"Consommateur 'moyenne' démarré → topic '{TOPIC}' (Ctrl+C pour arrêter)")
    try:
        for message in consumer:
            valeur = message.value
            somme += valeur
            compte += 1
            moyenne = somme / compte
            print(f"reçu : {valeur:5d}  |  moyenne ({compte} valeurs) = {moyenne:.2f}")
    except KeyboardInterrupt:
        print("\nArrêt du consommateur 'moyenne'.")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
