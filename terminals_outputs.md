# Q1 — Créer le topic logs (3 partitions) :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic logs --partitions 3 --replication-factor 1
Created topic logs.
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic logs
Topic: logs     TopicId: L72xK9fLQfqICQT7FcuouA PartitionCount: 3       ReplicationFactor: 1    Configs:
        Topic: logs     Partition: 0    Leader: 0       Replicas: 0     Isr: 0  Elr: N/A        LastKnownElr: N/A
        Topic: logs     Partition: 1    Leader: 0       Replicas: 0     Isr: 0  Elr: N/A        LastKnownElr: N/A
        Topic: logs     Partition: 2    Leader: 0       Replicas: 0     Isr: 0  Elr: N/A        LastKnownElr: N/A
```

---

# Q2 + Q3 — Producteur + 1 consommateur compteur :
## Terminal Producteur :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/log_producer.py 5 5
/mnt/c/tp_kafka/src/log_producer.py:76: DeprecationWarning: key_serializer does not implement kafka.serializer.Serializer
  main()
/mnt/c/tp_kafka/src/log_producer.py:76: DeprecationWarning: value_serializer does not implement kafka.serializer.Serializer
  main()
Producteur de logs démarré → topic 'logs' (Ctrl+C pour arrêter)
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 217.86.94.239  https://localhost/jo9eHEPImuFF
envoyé : 217.86.94.239  https://localhost/jo9eHEPImuFF
envoyé : 24.94.250.86   https://localhost/sMMxbhksBF1AIS
envoyé : 217.86.94.239  https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/jo9eHEPImuFF
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/jo9eHEPImuFF
envoyé : 221.186.7.194  https://localhost/jo9eHEPImuFF
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/jo9eHEPImuFF
envoyé : 217.86.94.239  https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 144.32.110.7   https://localhost/jo9eHEPImuFF
envoyé : 221.186.7.194  https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/H0Ajd
envoyé : 217.86.94.239  https://localhost/h1PI
envoyé : 65.90.207.212  https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/dvKIjIxoauxu
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 217.86.94.239  https://localhost/H0Ajd
envoyé : 144.32.110.7   https://localhost/sMMxbhksBF1AIS
envoyé : 144.32.110.7   https://localhost/H0Ajd
envoyé : 221.186.7.194  https://localhost/dvKIjIxoauxu
envoyé : 65.90.207.212  https://localhost/dvKIjIxoauxu
envoyé : 24.94.250.86   https://localhost/sMMxbhksBF1AIS
envoyé : 144.32.110.7   https://localhost/dvKIjIxoauxu
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 217.86.94.239  https://localhost/dvKIjIxoauxu
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 217.86.94.239  https://localhost/dvKIjIxoauxu
envoyé : 144.32.110.7   https://localhost/dvKIjIxoauxu
envoyé : 144.32.110.7   https://localhost/jo9eHEPImuFF
envoyé : 217.86.94.239  https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/H0Ajd
envoyé : 144.32.110.7   https://localhost/jo9eHEPImuFF
envoyé : 221.186.7.194  https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/H0Ajd
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/jo9eHEPImuFF
envoyé : 65.90.207.212  https://localhost/sMMxbhksBF1AIS
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/h1PI
envoyé : 144.32.110.7   https://localhost/h1PI
envoyé : 144.32.110.7   https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/jo9eHEPImuFF
envoyé : 144.32.110.7   https://localhost/dvKIjIxoauxu
envoyé : 217.86.94.239  https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/dvKIjIxoauxu
envoyé : 24.94.250.86   https://localhost/jo9eHEPImuFF
envoyé : 144.32.110.7   https://localhost/h1PI
envoyé : 144.32.110.7   https://localhost/jo9eHEPImuFF
envoyé : 221.186.7.194  https://localhost/dvKIjIxoauxu
envoyé : 217.86.94.239  https://localhost/jo9eHEPImuFF
envoyé : 24.94.250.86   https://localhost/dvKIjIxoauxu
envoyé : 217.86.94.239  https://localhost/jo9eHEPImuFF
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/H0Ajd
envoyé : 217.86.94.239  https://localhost/sMMxbhksBF1AIS
envoyé : 221.186.7.194  https://localhost/dvKIjIxoauxu
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 144.32.110.7   https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/dvKIjIxoauxu
envoyé : 221.186.7.194  https://localhost/sMMxbhksBF1AIS
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/dvKIjIxoauxu
envoyé : 221.186.7.194  https://localhost/sMMxbhksBF1AIS
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/dvKIjIxoauxu
envoyé : 24.94.250.86   https://localhost/dvKIjIxoauxu
envoyé : 65.90.207.212  https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/H0Ajd
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 144.32.110.7   https://localhost/H0Ajd
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 65.90.207.212  https://localhost/dvKIjIxoauxu
envoyé : 24.94.250.86   https://localhost/sMMxbhksBF1AIS
envoyé : 65.90.207.212  https://localhost/sMMxbhksBF1AIS
envoyé : 65.90.207.212  https://localhost/H0Ajd
envoyé : 24.94.250.86   https://localhost/sMMxbhksBF1AIS
envoyé : 144.32.110.7   https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/H0Ajd
envoyé : 144.32.110.7   https://localhost/h1PI
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/dvKIjIxoauxu
envoyé : 221.186.7.194  https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/H0Ajd
envoyé : 144.32.110.7   https://localhost/jo9eHEPImuFF
envoyé : 144.32.110.7   https://localhost/dvKIjIxoauxu
envoyé : 217.86.94.239  https://localhost/jo9eHEPImuFF
envoyé : 221.186.7.194  https://localhost/H0Ajd
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/h1PI
envoyé : 144.32.110.7   https://localhost/jo9eHEPImuFF
envoyé : 144.32.110.7   https://localhost/dvKIjIxoauxu
envoyé : 221.186.7.194  https://localhost/sMMxbhksBF1AIS
envoyé : 65.90.207.212  https://localhost/H0Ajd
envoyé : 65.90.207.212  https://localhost/sMMxbhksBF1AIS
envoyé : 24.94.250.86   https://localhost/jo9eHEPImuFF
envoyé : 221.186.7.194  https://localhost/H0Ajd
envoyé : 144.32.110.7   https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/dvKIjIxoauxu
envoyé : 65.90.207.212  https://localhost/dvKIjIxoauxu
envoyé : 24.94.250.86   https://localhost/dvKIjIxoauxu
envoyé : 24.94.250.86   https://localhost/h1PI
envoyé : 221.186.7.194  https://localhost/sMMxbhksBF1AIS
^C
Arrêt du producteur de logs.
```
## Terminal Consommateur 1 :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/log_consumer.py
/mnt/c/tp_kafka/src/log_consumer.py:22: DeprecationWarning: value_deserializer does not implement kafka.serializer.Deserializer
  consumer = KafkaConsumer(
Consommateur de logs démarré → topic 'logs' (Ctrl+C pour arrêter)
[p1] [2026-06-18 09:20] https://localhost/h1PI -> 1
[p1] [2026-06-18 09:20] https://localhost/h1PI -> 2
[p1] [2026-06-18 09:20] https://localhost/h1PI -> 3
[p0] [2026-06-18 09:20] https://localhost/dvKIjIxoauxu -> 1
[p1] [2026-06-18 09:20] https://localhost/h1PI -> 4
[p2] [2026-06-18 09:20] https://localhost/H0Ajd -> 1
[p1] [2026-06-18 09:20] https://localhost/sMMxbhksBF1AIS -> 1
[p2] [2026-06-18 09:20] https://localhost/H0Ajd -> 2
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 1
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 2
[p1] [2026-06-18 09:21] https://localhost/sMMxbhksBF1AIS -> 1
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 3
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 1
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 4
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 2
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 5
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 6
[p0] [2026-06-18 09:21] https://localhost/jo9eHEPImuFF -> 1
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 1
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 2
[p0] [2026-06-18 09:21] https://localhost/jo9eHEPImuFF -> 2
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 3
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 4
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 3
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 5
[p0] [2026-06-18 09:21] https://localhost/jo9eHEPImuFF -> 3
[p1] [2026-06-18 09:21] https://localhost/sMMxbhksBF1AIS -> 2
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 6
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 4
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 5
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 6
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 7
[p0] [2026-06-18 09:21] https://localhost/jo9eHEPImuFF -> 4
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 7
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 8
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 8
[p0] [2026-06-18 09:21] https://localhost/jo9eHEPImuFF -> 5
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 9
[p0] [2026-06-18 09:21] https://localhost/jo9eHEPImuFF -> 6
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 9
[p0] [2026-06-18 09:21] https://localhost/jo9eHEPImuFF -> 7
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 10
[p0] [2026-06-18 09:21] https://localhost/jo9eHEPImuFF -> 8
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 7
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 10
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 8
[p1] [2026-06-18 09:21] https://localhost/sMMxbhksBF1AIS -> 3
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 11
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 11
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 12
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 9
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 12
[p1] [2026-06-18 09:21] https://localhost/sMMxbhksBF1AIS -> 4
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 13
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 13
[p1] [2026-06-18 09:21] https://localhost/sMMxbhksBF1AIS -> 5
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 14
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 15
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 14
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 15
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 16
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 17
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 18
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 10
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 19
[p2] [2026-06-18 09:21] https://localhost/H0Ajd -> 11
[p1] [2026-06-18 09:21] https://localhost/h1PI -> 20
[p0] [2026-06-18 09:21] https://localhost/dvKIjIxoauxu -> 16
[p1] [2026-06-18 09:21] https://localhost/sMMxbhksBF1AIS -> 6
[p1] [2026-06-18 09:21] https://localhost/sMMxbhksBF1AIS -> 7
[p2] [2026-06-18 09:22] https://localhost/H0Ajd -> 1
[p1] [2026-06-18 09:22] https://localhost/sMMxbhksBF1AIS -> 1
[p1] [2026-06-18 09:22] https://localhost/h1PI -> 1
[p2] [2026-06-18 09:22] https://localhost/H0Ajd -> 2
[p1] [2026-06-18 09:22] https://localhost/h1PI -> 2
[p1] [2026-06-18 09:22] https://localhost/h1PI -> 3
[p0] [2026-06-18 09:22] https://localhost/dvKIjIxoauxu -> 1
[p1] [2026-06-18 09:22] https://localhost/h1PI -> 4
[p2] [2026-06-18 09:22] https://localhost/H0Ajd -> 3
[p0] [2026-06-18 09:22] https://localhost/jo9eHEPImuFF -> 1
[p0] [2026-06-18 09:22] https://localhost/dvKIjIxoauxu -> 2
[p0] [2026-06-18 09:22] https://localhost/jo9eHEPImuFF -> 2
[p2] [2026-06-18 09:22] https://localhost/H0Ajd -> 4
[p1] [2026-06-18 09:22] https://localhost/h1PI -> 5
[p2] [2026-06-18 09:22] https://localhost/H0Ajd -> 5
[p1] [2026-06-18 09:22] https://localhost/h1PI -> 6
[p0] [2026-06-18 09:22] https://localhost/jo9eHEPImuFF -> 3
[p0] [2026-06-18 09:22] https://localhost/dvKIjIxoauxu -> 3
[p1] [2026-06-18 09:22] https://localhost/sMMxbhksBF1AIS -> 2
[p2] [2026-06-18 09:22] https://localhost/H0Ajd -> 6
[p1] [2026-06-18 09:22] https://localhost/sMMxbhksBF1AIS -> 3
[p0] [2026-06-18 09:22] https://localhost/jo9eHEPImuFF -> 4
[p2] [2026-06-18 09:22] https://localhost/H0Ajd -> 7
[p1] [2026-06-18 09:22] https://localhost/h1PI -> 7
[p0] [2026-06-18 09:22] https://localhost/dvKIjIxoauxu -> 4
[p0] [2026-06-18 09:22] https://localhost/dvKIjIxoauxu -> 5
^C
--- Récapitulatif des hits par URL et par minute ---
2026-06-18 09:20 :
       4  https://localhost/h1PI
       2  https://localhost/H0Ajd
       1  https://localhost/dvKIjIxoauxu
       1  https://localhost/sMMxbhksBF1AIS
2026-06-18 09:21 :
      20  https://localhost/h1PI
      16  https://localhost/dvKIjIxoauxu
      11  https://localhost/H0Ajd
       8  https://localhost/jo9eHEPImuFF
       7  https://localhost/sMMxbhksBF1AIS
2026-06-18 09:22 :
       7  https://localhost/H0Ajd
       7  https://localhost/h1PI
       5  https://localhost/dvKIjIxoauxu
       4  https://localhost/jo9eHEPImuFF
       3  https://localhost/sMMxbhksBF1AIS
```

---

# Q5 — Parallélisation : 2ᵉ consommateur même groupe :
## Terminal Consommateur 1 :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/log_consumer.py
/mnt/c/tp_kafka/src/log_consumer.py:22: DeprecationWarning: value_deserializer does not implement kafka.serializer.Deserializer
  consumer = KafkaConsumer(
Consommateur de logs démarré → topic 'logs' (Ctrl+C pour arrêter)
[p2] [2026-06-18 09:26] https://localhost/E7KMnbtLEfiIe8 -> 1
[p2] [2026-06-18 09:26] https://localhost/PYdlCZxxIsjU -> 1
[p2] [2026-06-18 09:26] https://localhost/PYdlCZxxIsjU -> 2
[p2] [2026-06-18 09:26] https://localhost/E7KMnbtLEfiIe8 -> 2
[p2] [2026-06-18 09:26] https://localhost/E7KMnbtLEfiIe8 -> 3
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 1
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 2
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 3
[p1] [2026-06-18 09:26] https://localhost/ES4gvkEb -> 1
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 4
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 5
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 6
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 7
[p1] [2026-06-18 09:26] https://localhost/ES4gvkEb -> 2
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 8
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 9
[p1] [2026-06-18 09:26] https://localhost/ES4gvkEb -> 3
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 10
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 11
[p1] [2026-06-18 09:26] https://localhost/ES4gvkEb -> 4
[p0] [2026-06-18 09:26] https://localhost/nj31DLUcyXGg -> 1
[p0] [2026-06-18 09:26] https://localhost/nj31DLUcyXGg -> 2
[p0] [2026-06-18 09:26] https://localhost/nj31DLUcyXGg -> 3
[p0] [2026-06-18 09:26] https://localhost/nj31DLUcyXGg -> 4
[p0] [2026-06-18 09:26] https://localhost/nj31DLUcyXGg -> 5
[p0] [2026-06-18 09:26] https://localhost/nj31DLUcyXGg -> 6
[p0] [2026-06-18 09:26] https://localhost/nj31DLUcyXGg -> 7
[p2] [2026-06-18 09:26] https://localhost/E7KMnbtLEfiIe8 -> 4
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 12
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 13
[p0] [2026-06-18 09:26] https://localhost/nj31DLUcyXGg -> 8
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 14
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 15
[p1] [2026-06-18 09:26] https://localhost/ES4gvkEb -> 5
[p2] [2026-06-18 09:26] https://localhost/PYdlCZxxIsjU -> 3
[p1] [2026-06-18 09:26] https://localhost/ES4gvkEb -> 6
[p2] [2026-06-18 09:26] https://localhost/E7KMnbtLEfiIe8 -> 5
[p1] [2026-06-18 09:26] https://localhost/femPZhtW1hYL9Ra -> 16
[p0] [2026-06-18 09:26] https://localhost/nj31DLUcyXGg -> 9
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 1
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 1
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 2
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 2
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 1
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 3
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 4
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 3
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 2
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 3
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 5
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 6
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 7
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 4
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 8
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 9
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 4
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 10
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 5
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 11
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 5
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 6
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 6
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 7
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 7
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 8
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 9
[p1] [2026-06-18 09:27] https://localhost/ES4gvkEb -> 12
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 8
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 9
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 10
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 11
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 12
[p1] [2026-06-18 09:27] https://localhost/femPZhtW1hYL9Ra -> 13
[p0] [2026-06-18 09:27] https://localhost/nj31DLUcyXGg -> 10
^C
--- Récapitulatif des hits par URL et par minute ---
2026-06-18 09:26 :
      16  https://localhost/femPZhtW1hYL9Ra
       9  https://localhost/nj31DLUcyXGg
       6  https://localhost/ES4gvkEb
       5  https://localhost/E7KMnbtLEfiIe8
       3  https://localhost/PYdlCZxxIsjU
2026-06-18 09:27 :
      13  https://localhost/femPZhtW1hYL9Ra
      12  https://localhost/ES4gvkEb
      10  https://localhost/nj31DLUcyXGg
```
## Terminal Consommateur 2 :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/log_consumer.py
/mnt/c/tp_kafka/src/log_consumer.py:22: DeprecationWarning: value_deserializer does not implement kafka.serializer.Deserializer
  consumer = KafkaConsumer(
Consommateur de logs démarré → topic 'logs' (Ctrl+C pour arrêter)
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 1
[p2] [2026-06-18 09:27] https://localhost/PYdlCZxxIsjU -> 1
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 2
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 3
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 4
[p2] [2026-06-18 09:27] https://localhost/PYdlCZxxIsjU -> 2
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 5
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 6
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 7
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 8
[p2] [2026-06-18 09:27] https://localhost/PYdlCZxxIsjU -> 3
[p2] [2026-06-18 09:27] https://localhost/PYdlCZxxIsjU -> 4
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 9
[p2] [2026-06-18 09:27] https://localhost/PYdlCZxxIsjU -> 5
[p2] [2026-06-18 09:27] https://localhost/E7KMnbtLEfiIe8 -> 10
[p2] [2026-06-18 09:27] https://localhost/PYdlCZxxIsjU -> 6
[p2] [2026-06-18 09:28] https://localhost/E7KMnbtLEfiIe8 -> 1
[p1] [2026-06-18 09:28] https://localhost/femPZhtW1hYL9Ra -> 1
[p1] [2026-06-18 09:28] https://localhost/femPZhtW1hYL9Ra -> 2
^C
--- Récapitulatif des hits par URL et par minute ---
2026-06-18 09:27 :
      10  https://localhost/E7KMnbtLEfiIe8
       6  https://localhost/PYdlCZxxIsjU
2026-06-18 09:28 :
       2  https://localhost/femPZhtW1hYL9Ra
       1  https://localhost/E7KMnbtLEfiIe8
```
## la sortie du --describe :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group log-counter

GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                             HOST            CLIENT-ID
log-counter     logs            0          61              61              0               kafka-python-3.0.0-8e869e9b-50ca-43ef-a05d-9f5a175d85dd /127.0.0.1      kafka-python-3.0.0
log-counter     logs            1          97              99              2               kafka-python-3.0.0-8e869e9b-50ca-43ef-a05d-9f5a175d85dd /127.0.0.1      kafka-python-3.0.0
log-counter     logs            2          151             152             1               kafka-python-3.0.0-b290248e-6956-4661-82cb-bfb2c1c41d55 /127.0.0.1      kafka-python-3.0.0
```