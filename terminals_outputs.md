# Création du topic logs-avro (3 partitions) :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic logs-avro --partitions 3 --replication-factor 1
Created topic logs-avro.
```

---

# Produire un mélange de versions (Q2 + Q3 + Q5) :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/log_producer_avro.py 5 5 1
msProducteur Avro démarré → topic 'logs-avro' (version=1, Ctrl+C pour arrêter)
envoyé (v1) : 113.126.252.160   https://localhost/oBUutH
envoyé (v1) : 80.81.217.126     https://localhost/Xp2g
envoyé (v1) : 113.126.252.160   https://localhost/fbT3Ty8iU
envoyé (v1) : 186.223.175.92    https://localhost/X01pSTr
envoyé (v1) : 80.81.217.126     https://localhost/Xp2g
envoyé (v1) : 233.1.50.93       https://localhost/Hkru4TTb5JCRCYh
envoyé (v1) : 113.126.252.160   https://localhost/oBUutH
envoyé (v1) : 113.126.252.160   https://localhost/X01pSTr
envoyé (v1) : 233.1.50.93       https://localhost/Xp2g
envoyé (v1) : 216.165.110.152   https://localhost/oBUutH
envoyé (v1) : 216.165.110.152   https://localhost/oBUutH
envoyé (v1) : 80.81.217.126     https://localhost/fbT3Ty8iU
envoyé (v1) : 113.126.252.160   https://localhost/Hkru4TTb5JCRCYh
envoyé (v1) : 186.223.175.92    https://localhost/fbT3Ty8iU
^C
Arrêt du producteur Avro.
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/log_producer_avro.py 5 5 2
Producteur Avro démarré → topic 'logs-avro' (version=2, Ctrl+C pour arrêter)
envoyé (v2) : 101.148.109.140   https://localhost/7Wyr39SATHgLf6UP
envoyé (v2) : 101.148.109.140   https://localhost/2uBv7xAZn2
envoyé (v2) : 146.186.43.111    https://localhost/7Wyr39SATHgLf6UP
envoyé (v2) : 146.186.43.111    https://localhost/7Wyr39SATHgLf6UP
envoyé (v2) : 155.139.9.229     https://localhost/7Wyr39SATHgLf6UP
envoyé (v2) : 101.148.109.140   https://localhost/pzUG7Y
envoyé (v2) : 119.34.94.65      https://localhost/7Wyr39SATHgLf6UP
envoyé (v2) : 146.186.43.111    https://localhost/7Wyr39SATHgLf6UP
envoyé (v2) : 101.148.109.140   https://localhost/7Wyr39SATHgLf6UP
envoyé (v2) : 119.34.94.65      https://localhost/BhiooX
envoyé (v2) : 101.148.109.140   https://localhost/2uBv7xAZn2
envoyé (v2) : 101.148.109.140   https://localhost/2uBv7xAZn2
envoyé (v2) : 101.148.109.140   https://localhost/BhiooX
^C
Arrêt du producteur Avro.
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/log_producer_avro.py 5 5 3
Producteur Avro démarré → topic 'logs-avro' (version=3, Ctrl+C pour arrêter)
envoyé (v3) : 244.127.214.158   https://localhost/1eKetz
envoyé (v3) : 73.164.46.205     https://localhost/wR0wIGoNPx
envoyé (v3) : 244.127.214.158   https://localhost/dntHPajUdh5V5E
envoyé (v3) : 147.128.118.58    https://localhost/dntHPajUdh5V5E
envoyé (v3) : 234.211.168.51    https://localhost/6fFVjgxurd9GAuv
envoyé (v3) : 255.210.194.254   https://localhost/1eKetz
envoyé (v3) : 73.164.46.205     https://localhost/wR0wIGoNPx
envoyé (v3) : 73.164.46.205     https://localhost/1eKetz
envoyé (v3) : 255.210.194.254   https://localhost/dntHPajUdh5V5E
envoyé (v3) : 147.128.118.58    https://localhost/6fFVjgxurd9GAuv
envoyé (v3) : 244.127.214.158   https://localhost/6fFVjgxurd9GAuv
envoyé (v3) : 234.211.168.51    https://localhost/ZX4m65x1Fg5V
envoyé (v3) : 244.127.214.158   https://localhost/wR0wIGoNPx
envoyé (v3) : 244.127.214.158   https://localhost/dntHPajUdh5V5E
envoyé (v3) : 244.127.214.158   https://localhost/6fFVjgxurd9GAuv
^C
Arrêt du producteur Avro.
```

---

# Consommer et décoder toutes les versions (Q2 + Q4) :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/log_consumer_avro.py
Consommateur Avro démarré → topic 'logs-avro' (Ctrl+C pour arrêter)
[v1] cle=https://localhost/Xp2g  valeur={'ip': '80.81.217.126', 'url': 'https://localhost/Xp2g', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/fbT3Ty8iU  valeur={'ip': '113.126.252.160', 'url': 'https://localhost/fbT3Ty8iU', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/X01pSTr  valeur={'ip': '186.223.175.92', 'url': 'https://localhost/X01pSTr', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/Xp2g  valeur={'ip': '80.81.217.126', 'url': 'https://localhost/Xp2g', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/Hkru4TTb5JCRCYh  valeur={'ip': '233.1.50.93', 'url': 'https://localhost/Hkru4TTb5JCRCYh', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/X01pSTr  valeur={'ip': '113.126.252.160', 'url': 'https://localhost/X01pSTr', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/Xp2g  valeur={'ip': '233.1.50.93', 'url': 'https://localhost/Xp2g', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/fbT3Ty8iU  valeur={'ip': '80.81.217.126', 'url': 'https://localhost/fbT3Ty8iU', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/Hkru4TTb5JCRCYh  valeur={'ip': '113.126.252.160', 'url': 'https://localhost/Hkru4TTb5JCRCYh', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/fbT3Ty8iU  valeur={'ip': '186.223.175.92', 'url': 'https://localhost/fbT3Ty8iU', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/7Wyr39SATHgLf6UP  valeur={'ip': '101.148.109.140', 'url': 'https://localhost/7Wyr39SATHgLf6UP', 'datetime': '2026-06-18T10:42:01', 'taille': 6004481, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/2uBv7xAZn2  valeur={'ip': '101.148.109.140', 'url': 'https://localhost/2uBv7xAZn2', 'datetime': '2026-06-18T10:42:02', 'taille': 9237, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/7Wyr39SATHgLf6UP  valeur={'ip': '146.186.43.111', 'url': 'https://localhost/7Wyr39SATHgLf6UP', 'datetime': '2026-06-18T10:42:02', 'taille': 1728907, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/7Wyr39SATHgLf6UP  valeur={'ip': '146.186.43.111', 'url': 'https://localhost/7Wyr39SATHgLf6UP', 'datetime': '2026-06-18T10:42:03', 'taille': 7045447, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/7Wyr39SATHgLf6UP  valeur={'ip': '155.139.9.229', 'url': 'https://localhost/7Wyr39SATHgLf6UP', 'datetime': '2026-06-18T10:42:03', 'taille': 5200523, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/pzUG7Y  valeur={'ip': '101.148.109.140', 'url': 'https://localhost/pzUG7Y', 'datetime': '2026-06-18T10:42:05', 'taille': 5028279, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/7Wyr39SATHgLf6UP  valeur={'ip': '119.34.94.65', 'url': 'https://localhost/7Wyr39SATHgLf6UP', 'datetime': '2026-06-18T10:42:06', 'taille': 6725707, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/7Wyr39SATHgLf6UP  valeur={'ip': '146.186.43.111', 'url': 'https://localhost/7Wyr39SATHgLf6UP', 'datetime': '2026-06-18T10:42:06', 'taille': 1169143, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/7Wyr39SATHgLf6UP  valeur={'ip': '101.148.109.140', 'url': 'https://localhost/7Wyr39SATHgLf6UP', 'datetime': '2026-06-18T10:42:08', 'taille': 4196266, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/2uBv7xAZn2  valeur={'ip': '101.148.109.140', 'url': 'https://localhost/2uBv7xAZn2', 'datetime': '2026-06-18T10:42:11', 'taille': 2288294, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/2uBv7xAZn2  valeur={'ip': '101.148.109.140', 'url': 'https://localhost/2uBv7xAZn2', 'datetime': '2026-06-18T10:42:13', 'taille': 2618873, 'headers': {'referer': '-', 'user_agent': '-'}}
[v3] cle=https://localhost/ZX4m65x1Fg5V  valeur={'ip': '234.211.168.51', 'url': 'https://localhost/ZX4m65x1Fg5V', 'datetime': '2026-06-18T10:42:31', 'taille': 9698266, 'headers': {'referer': 'https://t.co', 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'}}
[v3] cle=https://localhost/dntHPajUdh5V5E  valeur={'ip': '244.127.214.158', 'url': 'https://localhost/dntHPajUdh5V5E', 'datetime': '2026-06-18T10:42:22', 'taille': 4371684, 'headers': {'referer': 'https://t.co', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}}
[v3] cle=https://localhost/dntHPajUdh5V5E  valeur={'ip': '147.128.118.58', 'url': 'https://localhost/dntHPajUdh5V5E', 'datetime': '2026-06-18T10:42:23', 'taille': 5340104, 'headers': {'referer': 'https://www.bing.com', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}}
[v3] cle=https://localhost/dntHPajUdh5V5E  valeur={'ip': '255.210.194.254', 'url': 'https://localhost/dntHPajUdh5V5E', 'datetime': '2026-06-18T10:42:30', 'taille': 5068180, 'headers': {'referer': '-', 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'}}
[v3] cle=https://localhost/dntHPajUdh5V5E  valeur={'ip': '244.127.214.158', 'url': 'https://localhost/dntHPajUdh5V5E', 'datetime': '2026-06-18T10:42:33', 'taille': 1667674, 'headers': {'referer': 'https://t.co', 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'}}
[v1] cle=https://localhost/oBUutH  valeur={'ip': '113.126.252.160', 'url': 'https://localhost/oBUutH', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/oBUutH  valeur={'ip': '113.126.252.160', 'url': 'https://localhost/oBUutH', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/oBUutH  valeur={'ip': '216.165.110.152', 'url': 'https://localhost/oBUutH', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v1] cle=https://localhost/oBUutH  valeur={'ip': '216.165.110.152', 'url': 'https://localhost/oBUutH', 'datetime': '', 'taille': 0, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/BhiooX  valeur={'ip': '119.34.94.65', 'url': 'https://localhost/BhiooX', 'datetime': '2026-06-18T10:42:10', 'taille': 6772051, 'headers': {'referer': '-', 'user_agent': '-'}}
[v2] cle=https://localhost/BhiooX  valeur={'ip': '101.148.109.140', 'url': 'https://localhost/BhiooX', 'datetime': '2026-06-18T10:42:14', 'taille': 808800, 'headers': {'referer': '-', 'user_agent': '-'}}
[v3] cle=https://localhost/1eKetz  valeur={'ip': '244.127.214.158', 'url': 'https://localhost/1eKetz', 'datetime': '2026-06-18T10:42:20', 'taille': 5778375, 'headers': {'referer': 'https://www.google.com', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}}
[v3] cle=https://localhost/wR0wIGoNPx  valeur={'ip': '73.164.46.205', 'url': 'https://localhost/wR0wIGoNPx', 'datetime': '2026-06-18T10:42:20', 'taille': 999741, 'headers': {'referer': '-', 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'}}
[v3] cle=https://localhost/6fFVjgxurd9GAuv  valeur={'ip': '234.211.168.51', 'url': 'https://localhost/6fFVjgxurd9GAuv', 'datetime': '2026-06-18T10:42:24', 'taille': 6425899, 'headers': {'referer': 'https://t.co', 'user_agent': 'curl/8.4.0'}}
[v3] cle=https://localhost/1eKetz  valeur={'ip': '255.210.194.254', 'url': 'https://localhost/1eKetz', 'datetime': '2026-06-18T10:42:26', 'taille': 7812907, 'headers': {'referer': 'https://www.bing.com', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}}
[v3] cle=https://localhost/wR0wIGoNPx  valeur={'ip': '73.164.46.205', 'url': 'https://localhost/wR0wIGoNPx', 'datetime': '2026-06-18T10:42:27', 'taille': 1555319, 'headers': {'referer': 'https://www.google.com', 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'}}
[v3] cle=https://localhost/1eKetz  valeur={'ip': '73.164.46.205', 'url': 'https://localhost/1eKetz', 'datetime': '2026-06-18T10:42:29', 'taille': 9612453, 'headers': {'referer': 'https://www.google.com', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}}
[v3] cle=https://localhost/6fFVjgxurd9GAuv  valeur={'ip': '147.128.118.58', 'url': 'https://localhost/6fFVjgxurd9GAuv', 'datetime': '2026-06-18T10:42:30', 'taille': 436389, 'headers': {'referer': 'https://t.co', 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'}}
[v3] cle=https://localhost/6fFVjgxurd9GAuv  valeur={'ip': '244.127.214.158', 'url': 'https://localhost/6fFVjgxurd9GAuv', 'datetime': '2026-06-18T10:42:30', 'taille': 841345, 'headers': {'referer': 'https://www.google.com', 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'}}
[v3] cle=https://localhost/wR0wIGoNPx  valeur={'ip': '244.127.214.158', 'url': 'https://localhost/wR0wIGoNPx', 'datetime': '2026-06-18T10:42:32', 'taille': 5494551, 'headers': {'referer': 'https://www.bing.com', 'user_agent': 'curl/8.4.0'}}
[v3] cle=https://localhost/6fFVjgxurd9GAuv  valeur={'ip': '244.127.214.158', 'url': 'https://localhost/6fFVjgxurd9GAuv', 'datetime': '2026-06-18T10:42:35', 'taille': 9785095, 'headers': {'referer': 'https://www.bing.com', 'user_agent': 'curl/8.4.0'}}
^C
Arrêt du consommateur Avro.
```