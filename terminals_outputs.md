# Exercice 13 — Installer & vérifier Avro :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv add avro
Resolved 3 packages in 229ms
Prepared 1 package in 76ms
░░░░░░░░░░░░░░░░░░░░ [0/1] Installing wheels...                                                                                                                                                                    warning: Failed to hardlink files; falling back to full copy. This may lead to degraded performance.
         If the cache and target directories are on different filesystems, hardlinking may not be supported.
         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
Installed 1 package in 1.39s
 + avro==1.12.1
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python -c "import avro; import avro.schema; print('avro version =', avro.__version__)"
avro version = 1.12.1
```

---

# Exercice 14 — Sérialiser puis relire :
```
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/avro_serialize.py
3 personnes sérialisées dans /mnt/c/tp_kafka/src/users.avro
raslan@DESKTOP-L584EQM:/mnt/c/tp_kafka$ uv run python src/avro_read.py
{'nom': 'Omar', 'age': 25, 'interets': ['SPORT', 'VOYAGE'], 'entreprise': {'nom': 'Padel SAS', 'siret': '12345678900011', 'effectifs': 12}}
{'nom': 'Priscile', 'age': 23, 'interets': ['LECTURE', 'MUSIQUE', 'CINEMA'], 'entreprise': None}
{'nom': 'Romain', 'age': 24, 'interets': ['CUISINE', 'VOYAGE', 'SPORT'], 'entreprise': {'nom': 'DataCorp', 'siret': '98765432100022', 'effectifs': 250}}
```