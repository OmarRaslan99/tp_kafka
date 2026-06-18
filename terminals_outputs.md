# Q1 — Vérifier kafka-python :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python -c "import kafka; print('version =', kafka.__version__)"
version = 3.0.0
```
---

# Création du topic nombres (1 partition) :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic nombres --partitions 1 --replication-factor 1
Created topic nombres.
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic nombres
Topic: nombres  TopicId: retYJyPUQpm1by66jOU_gg PartitionCount: 1       ReplicationFactor: 1    Configs:
        Topic: nombres  Partition: 0    Leader: 0       Replicas: 0     Isr: 0  Elr: N/A        LastKnownElr: N/A
```

---

# Q2 + Q3 + Q4 + Q5 — Lancer les 3 programmes en même temps :
## Terminal Producteur :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/producer_nombres.py
/mnt/c/tp_kafka/src/producer_nombres.py:38: DeprecationWarning: value_serializer does not implement kafka.serializer.Serializer
  main()
Producteur démarré → topic 'nombres' (Ctrl+C pour arrêter)
envoyé : 9620
envoyé : 6908
envoyé : 7168
envoyé : 15
envoyé : 8568
envoyé : 5870
envoyé : 1293
envoyé : 3857
envoyé : 8142
envoyé : 9348
envoyé : 9618
envoyé : 1408
envoyé : 9834
envoyé : 8648
envoyé : 1665
envoyé : 1123
envoyé : 6374
envoyé : 78
envoyé : 4212
envoyé : 3128
envoyé : 2348
envoyé : 174
envoyé : 8966
envoyé : 9852
envoyé : 7261
envoyé : 9040
envoyé : 983
envoyé : 6618
envoyé : 8517
envoyé : 2439
envoyé : 8069
envoyé : 1198
envoyé : 5298
envoyé : 2275
envoyé : 2170
envoyé : 7905
envoyé : 8640
envoyé : 2283
envoyé : 4321
envoyé : 4145
envoyé : 726
envoyé : 2820
envoyé : 6942
envoyé : 7156
envoyé : 1390
envoyé : 9154
envoyé : 3907
envoyé : 970
envoyé : 4391
envoyé : 1980
envoyé : 5553
envoyé : 1253
envoyé : 7115
envoyé : 8554
envoyé : 2372
envoyé : 1616
envoyé : 3316
envoyé : 9183
envoyé : 1193
envoyé : 9079
envoyé : 4300
envoyé : 8967
envoyé : 8698
envoyé : 7879
envoyé : 2074
envoyé : 7898
envoyé : 8340
envoyé : 7782
envoyé : 3568
envoyé : 5720
envoyé : 7495
envoyé : 567
envoyé : 5689
envoyé : 7488
envoyé : 6538
envoyé : 7535
envoyé : 9362
envoyé : 9451
envoyé : 3836
envoyé : 1884
envoyé : 5910
envoyé : 9123
envoyé : 4926
envoyé : 6298
envoyé : 6142
envoyé : 8354
envoyé : 5522
envoyé : 8783
envoyé : 7963
envoyé : 8070
envoyé : 7178
envoyé : 3064
envoyé : 5250
envoyé : 8995
envoyé : 6358
envoyé : 8493
envoyé : 3694
envoyé : 3441
envoyé : 7290
envoyé : 2040
envoyé : 7339
envoyé : 7573
envoyé : 179
envoyé : 5564
envoyé : 6151
envoyé : 5179
envoyé : 6172
envoyé : 7029
^C
Arrêt du producteur.
```

## Terminal Moyenne :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/consumer_moyenne.py
/mnt/c/tp_kafka/src/consumer_moyenne.py:15: DeprecationWarning: value_deserializer does not implement kafka.serializer.Deserializer
  consumer = KafkaConsumer(
Consommateur 'moyenne' démarré → topic 'nombres' (Ctrl+C pour arrêter)
reçu :  9620  |  moyenne (1 valeurs) = 9620.00
reçu :  6908  |  moyenne (2 valeurs) = 8264.00
reçu :  7168  |  moyenne (3 valeurs) = 7898.67
reçu :    15  |  moyenne (4 valeurs) = 5927.75
reçu :  8568  |  moyenne (5 valeurs) = 6455.80
reçu :  5870  |  moyenne (6 valeurs) = 6358.17
reçu :  1293  |  moyenne (7 valeurs) = 5634.57
reçu :  3857  |  moyenne (8 valeurs) = 5412.38
reçu :  8142  |  moyenne (9 valeurs) = 5715.67
reçu :  9348  |  moyenne (10 valeurs) = 6078.90
reçu :  9618  |  moyenne (11 valeurs) = 6400.64
reçu :  1408  |  moyenne (12 valeurs) = 5984.58
reçu :  9834  |  moyenne (13 valeurs) = 6280.69
reçu :  8648  |  moyenne (14 valeurs) = 6449.79
reçu :  1665  |  moyenne (15 valeurs) = 6130.80
reçu :  1123  |  moyenne (16 valeurs) = 5817.81
reçu :  6374  |  moyenne (17 valeurs) = 5850.53
reçu :    78  |  moyenne (18 valeurs) = 5529.83
reçu :  4212  |  moyenne (19 valeurs) = 5460.47
reçu :  3128  |  moyenne (20 valeurs) = 5343.85
reçu :  2348  |  moyenne (21 valeurs) = 5201.19
reçu :   174  |  moyenne (22 valeurs) = 4972.68
reçu :  8966  |  moyenne (23 valeurs) = 5146.30
reçu :  9852  |  moyenne (24 valeurs) = 5342.38
reçu :  7261  |  moyenne (25 valeurs) = 5419.12
reçu :  9040  |  moyenne (26 valeurs) = 5558.38
reçu :   983  |  moyenne (27 valeurs) = 5388.93
reçu :  6618  |  moyenne (28 valeurs) = 5432.82
reçu :  8517  |  moyenne (29 valeurs) = 5539.17
reçu :  2439  |  moyenne (30 valeurs) = 5435.83
reçu :  8069  |  moyenne (31 valeurs) = 5520.77
reçu :  1198  |  moyenne (32 valeurs) = 5385.69
reçu :  5298  |  moyenne (33 valeurs) = 5383.03
reçu :  2275  |  moyenne (34 valeurs) = 5291.62
reçu :  2170  |  moyenne (35 valeurs) = 5202.43
reçu :  7905  |  moyenne (36 valeurs) = 5277.50
reçu :  8640  |  moyenne (37 valeurs) = 5368.38
reçu :  2283  |  moyenne (38 valeurs) = 5287.18
reçu :  4321  |  moyenne (39 valeurs) = 5262.41
reçu :  4145  |  moyenne (40 valeurs) = 5234.48
reçu :   726  |  moyenne (41 valeurs) = 5124.51
reçu :  2820  |  moyenne (42 valeurs) = 5069.64
reçu :  6942  |  moyenne (43 valeurs) = 5113.19
reçu :  7156  |  moyenne (44 valeurs) = 5159.61
reçu :  1390  |  moyenne (45 valeurs) = 5075.84
reçu :  9154  |  moyenne (46 valeurs) = 5164.50
reçu :  3907  |  moyenne (47 valeurs) = 5137.74
reçu :   970  |  moyenne (48 valeurs) = 5050.92
reçu :  4391  |  moyenne (49 valeurs) = 5037.45
reçu :  1980  |  moyenne (50 valeurs) = 4976.30
reçu :  5553  |  moyenne (51 valeurs) = 4987.61
reçu :  1253  |  moyenne (52 valeurs) = 4915.79
reçu :  7115  |  moyenne (53 valeurs) = 4957.28
reçu :  8554  |  moyenne (54 valeurs) = 5023.89
reçu :  2372  |  moyenne (55 valeurs) = 4975.67
reçu :  1616  |  moyenne (56 valeurs) = 4915.68
reçu :  3316  |  moyenne (57 valeurs) = 4887.61
reçu :  9183  |  moyenne (58 valeurs) = 4961.67
reçu :  1193  |  moyenne (59 valeurs) = 4897.80
reçu :  9079  |  moyenne (60 valeurs) = 4967.48
reçu :  4300  |  moyenne (61 valeurs) = 4956.54
reçu :  8967  |  moyenne (62 valeurs) = 5021.23
reçu :  8698  |  moyenne (63 valeurs) = 5079.59
reçu :  7879  |  moyenne (64 valeurs) = 5123.33
reçu :  2074  |  moyenne (65 valeurs) = 5076.42
reçu :  7898  |  moyenne (66 valeurs) = 5119.17
reçu :  8340  |  moyenne (67 valeurs) = 5167.24
reçu :  7782  |  moyenne (68 valeurs) = 5205.69
reçu :  3568  |  moyenne (69 valeurs) = 5181.96
reçu :  5720  |  moyenne (70 valeurs) = 5189.64
reçu :  7495  |  moyenne (71 valeurs) = 5222.11
reçu :   567  |  moyenne (72 valeurs) = 5157.46
reçu :  5689  |  moyenne (73 valeurs) = 5164.74
reçu :  7488  |  moyenne (74 valeurs) = 5196.14
reçu :  6538  |  moyenne (75 valeurs) = 5214.03
reçu :  7535  |  moyenne (76 valeurs) = 5244.57
reçu :  9362  |  moyenne (77 valeurs) = 5298.04
reçu :  9451  |  moyenne (78 valeurs) = 5351.28
reçu :  3836  |  moyenne (79 valeurs) = 5332.10
reçu :  1884  |  moyenne (80 valeurs) = 5289.00
reçu :  5910  |  moyenne (81 valeurs) = 5296.67
reçu :  9123  |  moyenne (82 valeurs) = 5343.33
reçu :  4926  |  moyenne (83 valeurs) = 5338.30
reçu :  6298  |  moyenne (84 valeurs) = 5349.73
reçu :  6142  |  moyenne (85 valeurs) = 5359.05
reçu :  8354  |  moyenne (86 valeurs) = 5393.87
reçu :  5522  |  moyenne (87 valeurs) = 5395.34
reçu :  8783  |  moyenne (88 valeurs) = 5433.84
reçu :  7963  |  moyenne (89 valeurs) = 5462.26
reçu :  8070  |  moyenne (90 valeurs) = 5491.23
reçu :  7178  |  moyenne (91 valeurs) = 5509.77
reçu :  3064  |  moyenne (92 valeurs) = 5483.18
reçu :  5250  |  moyenne (93 valeurs) = 5480.68
reçu :  8995  |  moyenne (94 valeurs) = 5518.06
reçu :  6358  |  moyenne (95 valeurs) = 5526.91
reçu :  8493  |  moyenne (96 valeurs) = 5557.80
reçu :  3694  |  moyenne (97 valeurs) = 5538.59
reçu :  3441  |  moyenne (98 valeurs) = 5517.18
reçu :  7290  |  moyenne (99 valeurs) = 5535.09
reçu :  2040  |  moyenne (100 valeurs) = 5500.14
reçu :  7339  |  moyenne (101 valeurs) = 5518.35
reçu :  7573  |  moyenne (102 valeurs) = 5538.49
reçu :   179  |  moyenne (103 valeurs) = 5486.46
reçu :  5564  |  moyenne (104 valeurs) = 5487.20
reçu :  6151  |  moyenne (105 valeurs) = 5493.52
reçu :  5179  |  moyenne (106 valeurs) = 5490.56
reçu :  6172  |  moyenne (107 valeurs) = 5496.93
reçu :  7029  |  moyenne (108 valeurs) = 5511.11
^C
Arrêt du consommateur 'moyenne'.
```

## Terminal Min/Max :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/consumer_minmax.py
/mnt/c/tp_kafka/src/consumer_minmax.py:15: DeprecationWarning: value_deserializer does not implement kafka.serializer.Deserializer
  consumer = KafkaConsumer(
Consommateur 'minmax' démarré → topic 'nombres' (Ctrl+C pour arrêter)
reçu :  9620  |  min =  9620  max =  9620
reçu :  6908  |  min =  6908  max =  9620
reçu :  7168  |  min =  6908  max =  9620
reçu :    15  |  min =    15  max =  9620
reçu :  8568  |  min =    15  max =  9620
reçu :  5870  |  min =    15  max =  9620
reçu :  1293  |  min =    15  max =  9620
reçu :  3857  |  min =    15  max =  9620
reçu :  8142  |  min =    15  max =  9620
reçu :  9348  |  min =    15  max =  9620
reçu :  9618  |  min =    15  max =  9620
reçu :  1408  |  min =    15  max =  9620
reçu :  9834  |  min =    15  max =  9834
reçu :  8648  |  min =    15  max =  9834
reçu :  1665  |  min =    15  max =  9834
reçu :  1123  |  min =    15  max =  9834
reçu :  6374  |  min =    15  max =  9834
reçu :    78  |  min =    15  max =  9834
reçu :  4212  |  min =    15  max =  9834
reçu :  3128  |  min =    15  max =  9834
reçu :  2348  |  min =    15  max =  9834
reçu :   174  |  min =    15  max =  9834
reçu :  8966  |  min =    15  max =  9834
reçu :  9852  |  min =    15  max =  9852
reçu :  7261  |  min =    15  max =  9852
reçu :  9040  |  min =    15  max =  9852
reçu :   983  |  min =    15  max =  9852
reçu :  6618  |  min =    15  max =  9852
reçu :  8517  |  min =    15  max =  9852
reçu :  2439  |  min =    15  max =  9852
reçu :  8069  |  min =    15  max =  9852
reçu :  1198  |  min =    15  max =  9852
reçu :  5298  |  min =    15  max =  9852
reçu :  2275  |  min =    15  max =  9852
reçu :  2170  |  min =    15  max =  9852
reçu :  7905  |  min =    15  max =  9852
reçu :  8640  |  min =    15  max =  9852
reçu :  2283  |  min =    15  max =  9852
reçu :  4321  |  min =    15  max =  9852
reçu :  4145  |  min =    15  max =  9852
reçu :   726  |  min =    15  max =  9852
reçu :  2820  |  min =    15  max =  9852
reçu :  6942  |  min =    15  max =  9852
reçu :  7156  |  min =    15  max =  9852
reçu :  1390  |  min =    15  max =  9852
reçu :  9154  |  min =    15  max =  9852
reçu :  3907  |  min =    15  max =  9852
reçu :   970  |  min =    15  max =  9852
reçu :  4391  |  min =    15  max =  9852
reçu :  1980  |  min =    15  max =  9852
reçu :  5553  |  min =    15  max =  9852
reçu :  1253  |  min =    15  max =  9852
reçu :  7115  |  min =    15  max =  9852
reçu :  8554  |  min =    15  max =  9852
reçu :  2372  |  min =    15  max =  9852
reçu :  1616  |  min =    15  max =  9852
reçu :  3316  |  min =    15  max =  9852
reçu :  9183  |  min =    15  max =  9852
reçu :  1193  |  min =    15  max =  9852
reçu :  9079  |  min =    15  max =  9852
reçu :  4300  |  min =    15  max =  9852
reçu :  8967  |  min =    15  max =  9852
reçu :  8698  |  min =    15  max =  9852
reçu :  7879  |  min =    15  max =  9852
reçu :  2074  |  min =    15  max =  9852
reçu :  7898  |  min =    15  max =  9852
reçu :  8340  |  min =    15  max =  9852
reçu :  7782  |  min =    15  max =  9852
reçu :  3568  |  min =    15  max =  9852
reçu :  5720  |  min =    15  max =  9852
reçu :  7495  |  min =    15  max =  9852
reçu :   567  |  min =    15  max =  9852
reçu :  5689  |  min =    15  max =  9852
reçu :  7488  |  min =    15  max =  9852
reçu :  6538  |  min =    15  max =  9852
reçu :  7535  |  min =    15  max =  9852
reçu :  9362  |  min =    15  max =  9852
reçu :  9451  |  min =    15  max =  9852
reçu :  3836  |  min =    15  max =  9852
reçu :  1884  |  min =    15  max =  9852
reçu :  5910  |  min =    15  max =  9852
reçu :  9123  |  min =    15  max =  9852
reçu :  4926  |  min =    15  max =  9852
reçu :  6298  |  min =    15  max =  9852
reçu :  6142  |  min =    15  max =  9852
reçu :  8354  |  min =    15  max =  9852
reçu :  5522  |  min =    15  max =  9852
reçu :  8783  |  min =    15  max =  9852
reçu :  7963  |  min =    15  max =  9852
reçu :  8070  |  min =    15  max =  9852
reçu :  7178  |  min =    15  max =  9852
reçu :  3064  |  min =    15  max =  9852
reçu :  5250  |  min =    15  max =  9852
reçu :  8995  |  min =    15  max =  9852
reçu :  6358  |  min =    15  max =  9852
reçu :  8493  |  min =    15  max =  9852
reçu :  3694  |  min =    15  max =  9852
reçu :  3441  |  min =    15  max =  9852
reçu :  7290  |  min =    15  max =  9852
reçu :  2040  |  min =    15  max =  9852
reçu :  7339  |  min =    15  max =  9852
reçu :  7573  |  min =    15  max =  9852
reçu :   179  |  min =    15  max =  9852
reçu :  5564  |  min =    15  max =  9852
reçu :  6151  |  min =    15  max =  9852
reçu :  5179  |  min =    15  max =  9852
reçu :  6172  |  min =    15  max =  9852
reçu :  7029  |  min =    15  max =  9852
^C
Arrêt du consommateur 'minmax'.
```
---