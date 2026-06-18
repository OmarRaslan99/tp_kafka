# TP Kafka — Stream Processing

**Module :** Traitement temps-réel avec Kafka (Sylvain Gault)

**Groupe :** Omar · Priscile · Romain

> Ce document sert de **rapport** rendu avec le TP. Les questions sont numérotées par
> exercice ; pour chaque exercice on indique **qui a fait quoi** (code / tests / rapport).

---

## Environnement & reproduction

| Composant | Choix |
|---|---|
| OS hôte | Windows 10 |
| Runtime | **WSL2 — Ubuntu 22.04** (Kafka, ZooKeeper et Python y tournent) |
| Java | **Temurin OpenJDK 17.0.19** (installé dans `~/jdk-17`) |
| Kafka | **Apache Kafka 3.9.1** (Scala 2.13), **mode ZooKeeper** (installé dans `~/kafka`) |
| Code projet | `C:\tp_kafka` (Windows), vu depuis WSL comme `/mnt/c/tp_kafka` |
| Outillage Python | **uv** (`pyproject.toml` / `uv.lock`), **Python 3.11**, venv `.venv/` (ignoré) |
| Lib Python | **kafka-python 3.0.0** |

**Note d'installation.** Sur cette machine, la connectivité Internet sortante de WSL2
était cassée (NAT/HNS), tandis que Windows avait accès au réseau. Java et Kafka ont donc
été **téléchargés côté Windows puis installés dans WSL** via `/mnt/c`. Cela ne change rien
au fonctionnement : tout s'exécute ensuite localement dans WSL. Le réseau WSL a ensuite été
réparé (`Restart-Service hns` en PowerShell admin), ce qui a permis d'installer `uv` et
`kafka-python`.

### Mise en place de l'outillage Python (reproduction)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # installe uv
cd /mnt/c/tp_kafka
uv init --name tp-kafka --python 3.11
uv add kafka-python
uv run python -c "import kafka; print(kafka.__version__)"   # vérif
```

L'environnement (`JAVA_HOME`, `PATH` vers `kafka/bin`) est défini dans
[`scripts/env.sh`](scripts/env.sh) — **à sourcer dans chaque terminal WSL** (on ne modifie
pas `~/.bashrc`).

### Lancer l'environnement (rappel commandes)
```bash
# Dans CHAQUE terminal WSL, d'abord :
source /mnt/c/tp_kafka/scripts/env.sh

# Terminal 1 — ZooKeeper
zookeeper-server-start.sh ~/kafka/config/zookeeper.properties
# Terminal 2 — Broker Kafka
kafka-server-start.sh ~/kafka/config/server.properties
```

---

## Réponses par exercice

### Partie Kafka

#### Exercice 1 — Installation de Kafka
*Statut : fait (phase Set up).*
- Kafka 3.9 (Scala 2.13) téléchargé et décompressé, installé dans `~/kafka` (WSL).
- Programmes Linux dans `bin/` ; programmes Windows dans `bin/windows/`. On utilise `bin/` (.sh).
- **Qui a fait quoi :** _à compléter_.

#### Exercice 2 — Déploiement local (ZooKeeper + Kafka)
*Statut : fait.*

**Configuration.** On a modifié les répertoires de données pour les sortir de `/tmp`
(purgé à chaque redémarrage de WSL, donc on perdrait topics et messages) :
- `config/zookeeper.properties` → `dataDir=/home/raslan/kafka-data/zookeeper`
- `config/server.properties` → `log.dirs=/home/raslan/kafka-data/kafka-logs`

Lancement (deux terminaux, après `source scripts/env.sh`) :
```bash
zookeeper-server-start.sh ~/kafka/config/zookeeper.properties   # « binding to port ...:2181 »
kafka-server-start.sh     ~/kafka/config/server.properties      # « [KafkaServer id=0] started »
```

**Q3 — rôle des paramètres de `server.properties` :**
- `broker.id` (=0) : identifiant **unique** du broker au sein du cluster. Deux brokers ne
  peuvent pas partager le même id.
- `num.partitions` (=1) : nombre de partitions **par défaut** d'un topic créé sans préciser
  ce nombre (plus de partitions ⇒ plus de parallélisme de consommation).
- `log.retention.hours` (=168, soit 7 jours) : durée de **conservation** des messages sur
  disque avant suppression automatique.

**Q5 — relancer un 2ᵉ broker avec la MÊME config.** Le démarrage échoue immédiatement,
**avant même** le bind du port 9092, sur le verrou du répertoire de logs :
```
org.apache.kafka.common.KafkaException: Failed to acquire lock on file .lock in
/home/raslan/kafka-data/kafka-logs. A Kafka instance in another process or thread is
using this directory.
```
Pour lancer un **2ᵉ broker** sur la même machine, il faut donc lui donner :
- un `broker.id` (et `node.id`) **distinct**,
- un `log.dirs` **distinct** (verrou `.lock` exclusif par répertoire),
- un port `listeners` **distinct** (sinon conflit sur 9092).
*(C'est ce qu'on fera à l'Exercice 11 — déploiement pseudo-distribué.)*

- **Qui a fait quoi :** _à compléter_.

#### Exercice 3 — Gestion de topic
*Statut : fait.* (commandes via `kafka-topics.sh`, broker sur `localhost:9092`)

```bash
# 1) lister les topics (vide au départ)
kafka-topics.sh --bootstrap-server localhost:9092 --list
# (aucune sortie)

# 2) créer un topic
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic premier-topic
# -> Created topic premier-topic.

# 3) lister à nouveau
kafka-topics.sh --bootstrap-server localhost:9092 --list
# -> premier-topic

# 4) détails du topic
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic premier-topic
```
Sortie du `--describe` :
```
Topic: premier-topic   TopicId: WV18z8nWQ8yekl_6282UEQ   PartitionCount: 1   ReplicationFactor: 1   Configs:
    Topic: premier-topic   Partition: 0   Leader: 0   Replicas: 0   Isr: 0   Elr: N/A   LastKnownElr: N/A
```
**Lecture du `--describe`** (déploiement à 1 seul broker) :
- `PartitionCount: 1`, `ReplicationFactor: 1` : 1 partition, aucune réplique supplémentaire.
- `Partition: 0` : l'unique partition ; `Leader: 0` : le broker `0` en est le leader.
- `Replicas: 0` : la partition n'est stockée que sur le broker `0`.
- `Isr: 0` : *In-Sync Replicas* — répliques à jour (ici seulement le broker `0`).
- `Elr` / `LastKnownElr` : *Eligible Leader Replicas* (notion Kafka 3.9), `N/A` ici.

**Remarque (énoncé).** Le **renommage** d'un topic n'est pas supporté ; relancer `--create`
sur un topic existant renvoie `TopicExistsException` (les noms de topics sont uniques).

- **Qui a fait quoi :** _à compléter_.

#### Exercice 4 — Production / consommation de messages
*Statut : fait.* (programmes `kafka-console-producer.sh` / `kafka-console-consumer.sh`)

**Q1 — Producteur.** On lance un producteur sur le topic puis on tape quelques lignes
(chaque ligne = un message). *Sortie réelle (terminal 3) :*
```
$ kafka-console-producer.sh --bootstrap-server localhost:9092 --topic premier-topic
>Hello Romain
>Romain est tro nul au Padel et tous les sports combines
>Hello from T3
>Hello from T3 (2)
...
>Hello from T3 (6)
```

**Q2 — Consommateur « nu » (`--bootstrap-server` + `--topic` seulement).**
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic
# (rien ne s'affiche au démarrage)
```
*Réponse :* il **n'affiche rien** au lancement. Par défaut le consommateur ne lit que les
messages **arrivés après son lancement** (lecture « live » depuis la fin du topic), pas
l'historique déjà présent.

**Q3 — Les deux ouverts en même temps.** En tapant des messages dans le producteur, ils
apparaissent **en temps réel** dans le consommateur. *Sortie réelle (terminal 4) :*
```
$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic
Hello Romain
Romain est tro nul au Padel et tous les sports combines
^CProcessed a total of 3 messages
```

**Q4 — Option `--from-beginning`.** *Sortie réelle (terminal 4) :*
```
$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --from-beginning
Hello Romain
Romain est tro nul au Padel et tous les sports combines
^CProcessed a total of 3 messages
```
*Réponse :* elle fait lire **tous les messages depuis le plus ancien offset** conservé dans
la partition (et pas seulement les nouveaux). Utile pour rejouer tout l'historique.

**Q5 — Panne simulée + reprise avec `--offset`.** On arrête le consommateur (Ctrl-C)
pendant que le producteur envoie, puis on relance en ciblant une position précise. `--offset`
exige de préciser la partition (`--partition`). *Sortie réelle (terminal 4) :*
```
$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --partition 0 --offset earliest
Hello Romain
Romain est tro nul au Padel et tous les sports combines
^CProcessed a total of 3 messages
```
On peut aussi tester `--offset latest` (que les nouveaux) ou `--offset <entier>` (position
exacte).
*Réponse :* `--offset N --partition 0` fait reprendre la lecture **à partir de la position N**
de la partition. Pour ne traiter **que les messages non-lus**, il faudrait reprendre au
**dernier offset déjà consommé** ; or le consommateur console seul ne mémorise pas cette
position. C'est exactement ce que résolvent les **groupes de consommateurs** (Exo 5), qui
sauvegardent l'offset côté Kafka.

- **Qui a fait quoi :** _à compléter_.

#### Exercice 5 — Groupes et offsets
*Statut : fait.* (commande `kafka-consumer-groups.sh`)

**Q1 — Assigner un groupe (`--group`).**
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --group mon-groupe --from-beginning
```
*Réponse :* avec un `--group`, Kafka **sauvegarde les offsets** consommés dans le topic
interne `__consumer_offsets`. Si on arrête puis relance un consommateur du **même groupe**,
il **reprend après le dernier offset validé** (il ne re-lit pas l'historique) — contrairement
au consommateur sans groupe de l'Exo 4.

**Q2 — Lister les groupes.** *Sortie réelle (terminal 5) :*
```
$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
console-consumer-29451
console-consumer-92888
mon-groupe
```
*(les `console-consumer-XXXXX` sont les groupes éphémères créés automatiquement par les
consommateurs sans `--group` des exercices précédents ; `mon-groupe` est le nôtre.)*

**Q3 — Détails d'un groupe.** *Sortie réelle (terminal 5) :*
```
$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group mon-groupe
GROUP        TOPIC          PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG  CONSUMER-ID                  HOST        CLIENT-ID
mon-groupe   premier-topic  0          3               3               0    console-consumer-1bd3cf36... /127.0.0.1  console-consumer
```
- `CURRENT-OFFSET` : dernier offset commité par le groupe.
- `LOG-END-OFFSET` : offset de fin (dernier message + 1) dans la partition.
- `LAG` = `LOG-END-OFFSET − CURRENT-OFFSET` : nombre de messages **non encore traités** (ici 0).

**Q4 — Réinitialiser l'offset au plus ancien.** Le consommateur du groupe doit être
**arrêté**, sinon Kafka refuse le reset — erreur réellement rencontrée tant que le
consommateur tournait encore :
```
$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group mon-groupe --reset-offsets --to-earliest --topic premier-topic --execute
Error: Assignments can only be reset if the group 'mon-groupe' is inactive, but the current state is Stable.
```
Une fois le consommateur arrêté, le reset réussit :
```
$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group mon-groupe --reset-offsets --to-earliest --topic premier-topic --execute
GROUP        TOPIC          PARTITION  NEW-OFFSET
mon-groupe   premier-topic  0          0
```
En relançant le consommateur du groupe, il **re-lit tous les messages depuis le début**
(`NEW-OFFSET = 0`) : le reset a bien été pris en compte.

- **Qui a fait quoi :** _à compléter_.

#### Exercice 6 — Parallélisation du traitement
*Statut : fait.*

**Q1 — 2ᵉ consommateur dans le même groupe (topic à 1 partition).** On lance deux
consommateurs avec `--group mon-groupe` et on produit des messages.
*Réponse :* **un seul** des deux consommateurs reçoit les messages ; l'autre reste
**inactif**. Règle : au sein d'un groupe, **une partition est assignée à un seul
consommateur** — avec 1 partition, le 2ᵉ consommateur n'a rien à traiter.

**Q2 — Passer le topic à 2 partitions.** *Sortie réelle (terminal 5) :*
```
$ kafka-topics.sh --bootstrap-server localhost:9092 --alter --topic premier-topic --partitions 2
$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic premier-topic
Topic: premier-topic   TopicId: WV18z8nWQ8yekl_6282UEQ   PartitionCount: 2   ReplicationFactor: 1   Configs:
    Topic: premier-topic   Partition: 0   Leader: 0   Replicas: 0   Isr: 0   Elr: N/A   LastKnownElr: N/A
    Topic: premier-topic   Partition: 1   Leader: 0   Replicas: 0   Isr: 0   Elr: N/A   LastKnownElr: N/A
```
On voit bien désormais **Partition: 0** *et* **Partition: 1**.
*Note :* on peut seulement **augmenter** le nombre de partitions, jamais le réduire.

**Q3 — Vérifier la répartition sur deux consommateurs.** Avec 2 partitions et 2
consommateurs du même groupe, chacun se voit assigner **une partition** ; les messages
produits se répartissent alors entre les deux consommateurs (chaque message va à un seul des
deux).

*Piège rencontré :* en envoyant des messages **sans clé**, ils sont tous arrivés sur la même
partition (donc un seul consommateur). En effet, le partitionneur par défaut de Kafka (≥ 2.4)
est **« sticky »** : il regroupe les messages sans clé sur **une même partition** pour
optimiser les lots, ce n'est pas un round-robin message par message. Pour forcer la
répartition, on produit **avec des clés** (la partition vaut `hash(clé) % nb_partitions`) :
```bash
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic premier-topic \
  --property parse.key=true --property key.separator=:
> a:msg1
> b:msg2
> c:msg3
```
Avec 2 consommateurs du même groupe `mon-groupe`, les 6 messages clés se sont bien
**répartis sur les deux** : *(sorties réelles)*
```
# Terminal 4 (assigné à la partition 0)        # Terminal 6 (assigné à la partition 1)
msg1                                           msg4
msg2                                           msg6
msg3
msg5
```
Chaque message n'est traité que par **un seul** consommateur du groupe : c'est la
parallélisation recherchée (le traitement est réparti sur les 2 partitions).

- **Qui a fait quoi :** _à compléter_.

#### Exercice 7 — Plusieurs traitements par message (groupes distincts)
*Statut : fait.*

**Q1 — Deux consommateurs, deux groupes différents**, sur le même topic :
```bash
# Terminal A
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --group groupe-A
# Terminal B
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic premier-topic --group groupe-B
```

**Q2 — Comportement.** Chaque message envoyé dans le topic est reçu **par les deux groupes**
(un, et un seul, consommateur de **chaque** groupe le traite). Le même message
(`g: test groupe A et B`, produit en terminal 3) est bien apparu **dans les deux** :
```
# Terminal 4 (--group groupe-A)        # Terminal 6 (--group groupe-B)
 test groupe A et B                     test groupe A et B
```
C'est le modèle **publish/subscribe** : des groupes distincts représentent des **traitements
indépendants** du même flux (à l'inverse de l'Exo 6 où les consommateurs d'un *même* groupe se
*partagent* les messages).

*Remarque (piège `parse.key`).* Quand le producteur tourne avec `--property parse.key=true`,
**chaque** ligne doit contenir le séparateur ; sinon il s'arrête sur une exception :
```
org.apache.kafka.common.KafkaException: No key separator found on line number 7: 'test groupe A et B'
```
→ il faut écrire `clé:valeur` (ex. `g: test groupe A et B`).

- **Qui a fait quoi :** _à compléter_.

#### Exercice 8 — Explorer ZooKeeper
*Statut : fait.*

**Q1 — Le répertoire `dataDir` de ZooKeeper.** On relève le `dataDir` dans la config, puis on
liste son contenu : *(sorties réelles)*
```
$ grep -E '^dataDir' ~/kafka/config/zookeeper.properties
dataDir=/home/raslan/kafka-data/zookeeper
$ ls -R ~/kafka-data/zookeeper
/home/raslan/kafka-data/zookeeper:
version-2

/home/raslan/kafka-data/zookeeper/version-2:
log.1  log.43  log.c2  snapshot.0  snapshot.42  snapshot.c1
```
*Réponse :* ZooKeeper persiste son état sur disque dans `version-2/`, sous deux formes :
les **snapshots** (`snapshot.*`, image de l'arborescence à un instant T) et les **journaux de
transactions** (`log.*`, suite des modifications). C'est ce qui permet à ZooKeeper de
reconstruire son état au redémarrage.

**Q2 — Lancer le shell ZooKeeper.**
```bash
zookeeper-shell.sh localhost:2181
```
*Réponse :* on obtient un shell rudimentaire (`JLine support is disabled`) : **aucun prompt**
n'est affiché et **aucune édition de ligne** n'est possible — on tape les commandes « à
l'aveugle » puis Entrée, comme l'annonce l'énoncé.

**Q3 — Commande inconnue → liste des commandes.** En tapant `help` (commande non reconnue), le
shell affiche la liste des commandes disponibles : *(extrait de la sortie réelle)*
```
addWatch ...      create [-s] [-e] ...   get [-s] [-w] path     ls [-s] [-w] [-R] path
addauth ...       delete [-v version]    getAcl [-s] path       quit
close             deleteall path         getAllChildrenNumber   set [-s] [-v] path data
config            delquota               getEphemerals path     stat [-w] path
connect host:port history                listquota              version / whoami
...
Command not found: Command not found help
```
Les commandes utiles pour explorer sont surtout `ls` (lister les enfants d'un znode) et
`get` (lire le contenu d'un znode).

**Q4 — Trouver au moins deux znodes liés à Kafka.** On part de la racine puis on descend :
*(sorties réelles)*
```
ls /
[admin, brokers, cluster, config, consumers, controller, controller_epoch, feature,
 isr_change_notification, latest_producer_id_block, log_dir_event_notification, zookeeper]

ls /brokers/ids
[0]
get /brokers/ids/0
{"features":{},"listener_security_protocol_map":{"PLAINTEXT":"PLAINTEXT"},
 "endpoints":["PLAINTEXT://DESKTOP-L584EQM.localdomain:9092"],"jmx_port":-1,
 "port":9092,"host":"DESKTOP-L584EQM.localdomain","version":5,"timestamp":"1781706151709"}

get /brokers/topics/premier-topic
{"partitions":{"0":[0],"1":[0]},"topic_id":"WV18z8nWQ8yekl_6282UEQ", ... ,"version":3}

get /controller
{"version":2,"brokerid":0,"timestamp":"1781706151854","kraftControllerEpoch":-1}
```
*Réponse — deux znodes liés à Kafka (parmi d'autres) :*
- **`/brokers/ids/0`** : l'enregistrement du broker `0` — son hôte, son port (`9092`) et ses
  *endpoints*. C'est ainsi que Kafka sait quels brokers sont vivants (ce znode est **éphémère** :
  il disparaît si le broker s'arrête).
- **`/brokers/topics/premier-topic`** : les métadonnées du topic, dont la carte
  **partition → réplicas**. On y voit bien `"partitions":{"0":[0],"1":[0]}`, soit les **2
  partitions** (sur le broker `0`) créées à l'Exercice 6.
- *(bonus)* **`/controller`** indique quel broker joue le rôle de contrôleur (`brokerid:0`).

**Q5 — Observer un changement côté Kafka reflété dans ZooKeeper.** Le shell ZK ouvert, on liste
les topics, on **crée** un topic dans un autre terminal, puis on re-liste : *(sorties réelles)*
```
# avant (dans le shell ZK)
ls /brokers/topics
[__consumer_offsets, premier-topic]

# dans un autre terminal Kafka
$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic zk-demo --partitions 1 --replication-factor 1
Created topic zk-demo.

# après (de retour dans le shell ZK)
ls /brokers/topics
[__consumer_offsets, premier-topic, zk-demo]
get /brokers/topics/zk-demo
{"partitions":{"0":[0]},"topic_id":"i5lmFi0tS0GZAAA0trfk7g", ... ,"version":3}
```
*Réponse :* dès la création du topic côté Kafka, un nouveau znode **`/brokers/topics/zk-demo`**
apparaît **en direct** dans ZooKeeper, avec sa structure de partitions. ZooKeeper est donc bien
le **dépôt des métadonnées** du cluster (brokers, topics, partitions, contrôleur), mis à jour à
chaque changement.
*Nuance importante :* les **offsets des groupes de consommateurs** ne sont **pas** stockés dans
ZooKeeper mais dans le topic interne **`__consumer_offsets`** (cf. Exercice 5) — on le voit
d'ailleurs listé parmi les topics ci-dessus.
*(Le topic de test a ensuite été supprimé : `kafka-topics.sh ... --delete --topic zk-demo`.)*

- **Qui a fait quoi :** _à compléter_.

#### Exercice 9 — Premiers programmes Python (producteur / moyenne / min-max)
*Statut : fait.*

Première phase **en Python** avec la bibliothèque `kafka-python`, lancée via `uv`. Trois
programmes dans `src/` : un producteur de nombres aléatoires et deux consommateurs d'analyse.
On utilise un **topic dédié `nombres`** (1 partition).

**Q1 — Installer et vérifier `kafka-python`.** La dépendance `kafka-python>=3.0.0` est déclarée
dans `pyproject.toml` (gérée par `uv`). Vérification : *(sortie réelle)*
```
$ uv run python -c "import kafka; print('version =', kafka.__version__)"
version = 3.0.0
```
La bibliothèque s'importe correctement (l'énoncé demande aussi `help(kafka)`, qui ouvre la
documentation intégrée). *Documentation : https://kafka-python.readthedocs.io/*

**Création du topic.** *(sortie réelle)*
```
$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic nombres --partitions 1 --replication-factor 1
Created topic nombres.
$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic nombres
Topic: nombres  TopicId: retYJyPUQpm1by66jOU_gg  PartitionCount: 1  ReplicationFactor: 1  Configs:
    Topic: nombres  Partition: 0  Leader: 0  Replicas: 0  Isr: 0  Elr: N/A  LastKnownElr: N/A
```

**Q2 — Producteur de nombres aléatoires** (`src/producer_nombres.py`). Un message par seconde,
nombre entre 0 et 10000 :
```python
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: str(v).encode("utf-8"),
)
while True:
    nombre = random.randint(0, 10000)
    producer.send("nombres", nombre)
    time.sleep(1)
```
*Sortie réelle (extrait) :*
```
Producteur démarré → topic 'nombres' (Ctrl+C pour arrêter)
envoyé : 9620
envoyé : 6908
envoyé : 7168
envoyé : 15
...
^C
Arrêt du producteur.
```

**Q3 — Consommateur « moyenne »** (`src/consumer_moyenne.py`). Groupe dédié `moyenne` ; il
maintient une somme et un compteur, et affiche la moyenne courante. *Sortie réelle (extraits) :*
```
Consommateur 'moyenne' démarré → topic 'nombres' (Ctrl+C pour arrêter)
reçu :  9620  |  moyenne (1 valeurs) = 9620.00
reçu :  6908  |  moyenne (2 valeurs) = 8264.00
reçu :    15  |  moyenne (4 valeurs) = 5927.75
...
reçu :  7029  |  moyenne (108 valeurs) = 5511.11
```
On voit la moyenne **converger vers ~5000** (≈ espérance d'un tirage uniforme sur [0, 10000]) à
mesure que les valeurs s'accumulent.

**Q4 — Consommateur « min / max »** (`src/consumer_minmax.py`). Groupe **distinct** `minmax`.
*Sortie réelle (extraits) :*
```
Consommateur 'minmax' démarré → topic 'nombres' (Ctrl+C pour arrêter)
reçu :  9620  |  min =  9620  max =  9620
reçu :    15  |  min =    15  max =  9620
reçu :  9834  |  min =    15  max =  9834
reçu :  9852  |  min =    15  max =  9852
...
reçu :  7029  |  min =    15  max =  9852
```
Le **min** descend à `15` et le **max** monte à `9852`, puis se stabilisent (ils ne peuvent que
s'élargir).

**Q5 — Les faire tourner en même temps.** Les trois programmes ont tourné simultanément
(3 terminaux). Comme `moyenne` et `minmax` sont dans des **groupes différents**, ils reçoivent
**chacun tous** les nombres produits (modèle publish/subscribe, cf. Exo 7) : les 108 valeurs
émises par le producteur apparaissent bien dans les deux consommateurs, qui calculent leurs
statistiques en parallèle et en temps réel.

**Q6 — Distribuer le calcul si le débit devient trop important.** On réutilise le mécanisme de
l'**Exercice 6** : **augmenter le nombre de partitions** du topic `nombres`, puis lancer
**plusieurs instances d'un même consommateur dans le même groupe** (ex. plusieurs `moyenne`
avec `group_id="moyenne"`). Kafka répartit alors les partitions entre ces instances, qui
peuvent tourner sur **plusieurs machines** — le traitement est parallélisé. Limite à garder en
tête : chaque instance ne voit qu'**une partie** des données, donc pour une statistique globale
(moyenne, min, max) il faut une **étape d'agrégation finale** combinant les résultats partiels
de chaque consommateur (par exemple : sommes + compteurs partiels additionnés pour la moyenne ;
min des min et max des max). *(Réponse théorique — la parallélisation effective relève des
exercices bonus.)*

*Remarque technique.* `kafka-python` émet un `DeprecationWarning` (« value_serializer /
value_deserializer does not implement kafka.serializer.Serializer ») car on passe une simple
`lambda` au lieu d'une classe `Serializer` dédiée. C'est **sans conséquence** sur le
fonctionnement ; on garde les lambdas pour la simplicité.

- **Qui a fait quoi :** _à compléter_.

#### Exercice 10 *(Bonus)* — Centralisation de logs dans Kafka
*Statut : fait.*

On centralise des logs de serveur web simulés dans Kafka, puis on les analyse. Le script fourni
`ressources/genlogs.py` génère ~1 ligne/seconde au format `IP<TAB>URL` (fréquentation pondérée).
On en a fait une **version Kafka** dans `src/log_producer.py` (on ne modifie pas le script du
prof) et un consommateur analytique `src/log_consumer.py`.

**Q1 — Topic des logs (3 partitions).** *(sortie réelle)*
```
$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic logs --partitions 3 --replication-factor 1
Created topic logs.
$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic logs
Topic: logs  TopicId: L72xK9fLQfqICQT7FcuouA  PartitionCount: 3  ReplicationFactor: 1  Configs:
    Topic: logs  Partition: 0  Leader: 0  ...
    Topic: logs  Partition: 1  Leader: 0  ...
    Topic: logs  Partition: 2  Leader: 0  ...
```

**Q2 — Producteur de logs** (`src/log_producer.py`). On reprend `randomip`/`randomurl` et les
pondérations de `genlogs.py`, mais on **publie dans le topic** au lieu d'imprimer. **Choix :
l'URL est mise en clé** du message → tous les hits d'une même URL tombent sur la **même
partition** (comptage cohérent quand on parallélise, cf. Q5).
```python
producer.send("logs", key=url, value="%s\t%s" % (user, url))   # clé = URL
```
*Sortie réelle (extrait), lancée avec 5 IP et 5 URL (`uv run python src/log_producer.py 5 5`) :*
```
Producteur de logs démarré → topic 'logs' (Ctrl+C pour arrêter)
envoyé : 24.94.250.86   https://localhost/H0Ajd
envoyé : 217.86.94.239  https://localhost/jo9eHEPImuFF
...
```

**Q3 — Consommateur compteur** (`src/log_consumer.py`). Pour chaque message, on extrait l'URL et
on incrémente `compteurs[minute][url]` (minute courante `AAAA-MM-JJ HH:MM`). Un seul consommateur
voit alors les 3 partitions. *Récapitulatif réel sur Ctrl+C (une minute) :*
```
2026-06-18 09:21 :
      20  https://localhost/h1PI
      16  https://localhost/dvKIjIxoauxu
      11  https://localhost/H0Ajd
       8  https://localhost/jo9eHEPImuFF
       7  https://localhost/sMMxbhksBF1AIS
```
On retrouve bien la **pondération** de `genlogs.py` (quelques URL nettement plus visitées) et le
**comptage par minute** demandé. *(Stockage en simple dict Python, comme le permet l'énoncé.)*

**Q4 — Si l'analyse ne suit pas le débit.**
- **Topic :** augmenter le **nombre de partitions** (condition pour avoir plus de consommateurs en
  parallèle) ; allonger la **rétention** pour ne pas perdre le backlog le temps de rattraper.
- **Consumer :** lancer **plusieurs instances dans le même groupe** (scale-out : Kafka répartit
  les partitions) ; alléger le traitement par message.
- **Producer :** **partitionner par clé** (ici l'URL) pour équilibrer la charge tout en gardant le
  comptage cohérent ; activer **batching/compression** pour absorber les pics.
- C'est le même levier qu'à l'**Exercice 6** (parallélisation par partitions).

**Q5 — Implémentation et vérification.** Topic déjà à 3 partitions → on lance **2 consommateurs**
avec le même `group_id="log-counter"`. Kafka **répartit les partitions** entre eux : *(sortie
réelle de `--describe`)*
```
GROUP        TOPIC  PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG  CONSUMER-ID
log-counter  logs   0          61              61              0    kafka-python-...-d85dd
log-counter  logs   1          97              99              2    kafka-python-...-d85dd
log-counter  logs   2          151             152             1    kafka-python-...-41d55
```
→ le consommateur `...d85dd` détient les **partitions 0 et 1**, le consommateur `...41d55` la
**partition 2**. Conséquence visible dans leurs sorties : ils comptent des **URL distinctes**
(grâce au keying par URL, aucune URL n'est comptée par les deux) :
```
# Consommateur 1 (partitions 0,1)           # Consommateur 2 (partition 2)
femPZhtW1hYL9Ra, nj31DLUcyXGg, ES4gvkEb      E7KMnbtLEfiIe8, PYdlCZxxIsjU
```
La charge d'analyse est donc bien **distribuée** sur les deux consommateurs, sans étape de fusion
des compteurs. *(Le `LAG` non nul vient du producteur encore actif au moment du `--describe`.)*

- **Qui a fait quoi :** _à compléter_.

#### Exercice 11 *(Bonus)* — Déploiement pseudo-distribué
*Statut : à faire.*

#### Exercice 12 *(Bonus)* — Déploiement distribué
*Statut : à faire.*

### Partie Avro

#### Exercice 13 — Installer Avro
*Statut : fait.*

On ajoute le package `avro` au projet (équivalent du `pip3 install avro` de l'énoncé, mais géré
par `uv`), puis on vérifie l'import. *(sorties réelles)*
```
$ uv add avro
...
 + avro==1.12.1
$ uv run python -c "import avro; import avro.schema; print('avro version =', avro.__version__)"
avro version = 1.12.1
```
L'import de `avro.schema` fonctionne (l'énoncé suggère aussi `help(avro.schema)`, qui affiche la
doc intégrée du module). *Documentation : https://avro.apache.org/docs/current/*

#### Exercice 14 — Premiers pas avec Avro
*Statut : fait.*

On écrit un schéma Avro, on sérialise une liste de personnes dans un fichier `.avro`, on le
relit, puis on fait **évoluer le schéma** (intérêts → enum → entreprise optionnelle). Trois
fichiers : `src/user.avsc` (schéma), `src/avro_serialize.py`, `src/avro_read.py`.

**Q1 — Liste de personnes (dict).** Chaque personne a au minimum un `nom` et un `age` :
```python
personnes = [
    {"nom": "Omar", "age": 25, ...},
    {"nom": "Priscile", "age": 23, ...},
    {"nom": "Romain", "age": 24, ...},
]
```

**Q2 — Schéma `user.avsc`.** Un `record` avec un **`namespace`** propre au groupe et un champ
**`doc`** décrivant l'objet (état de départ, nom + âge) :
```json
{
  "type": "record",
  "name": "Personne",
  "namespace": "fr.tp_kafka.opr",
  "doc": "Decrit une personne ... (groupe Omar/Priscile/Romain).",
  "fields": [
    { "name": "nom", "type": "string", "doc": "Nom de la personne." },
    { "name": "age", "type": "int",    "doc": "Age en annees." }
  ]
}
```

**Q3 — Sérialisation** (`avro_serialize.py`) : on charge le schéma et on écrit les personnes dans
`users.avro` avec `DataFileWriter` + `DatumWriter` :
```python
schema = avro.schema.parse(open("src/user.avsc").read())
writer = DataFileWriter(open("src/users.avro", "wb"), DatumWriter(), schema)
for personne in personnes:
    writer.append(personne)
writer.close()
```
*Sortie réelle :*
```
$ uv run python src/avro_serialize.py
3 personnes sérialisées dans /mnt/c/tp_kafka/src/users.avro
```

**Q4 — Lecture** (`avro_read.py`) : le schéma est **embarqué** dans le fichier `.avro`, donc
inutile de le fournir pour relire. `DataFileReader` + `DatumReader` :
```python
reader = DataFileReader(open("src/users.avro", "rb"), DatumReader())
for personne in reader:
    print(personne)
reader.close()
```

**Q5 — Ajout des centres d'intérêt (liste de strings).** On ajoute au schéma un champ tableau :
```json
{ "name": "interets", "type": { "type": "array", "items": "string" } }
```

**Q6 — Intérêts pris dans une liste prédéfinie (enum).** On remplace `"string"` par un **`enum`**
Avro, qui contraint les valeurs possibles :
```json
{
  "name": "interets",
  "type": { "type": "array",
            "items": { "type": "enum", "name": "Interet",
                       "symbols": ["SPORT","MUSIQUE","LECTURE","CINEMA","VOYAGE","CUISINE"] } }
}
```

**Q7 — Champ optionnel `entreprise`.** On ajoute un `record` `Entreprise` (`nom`, `siret`,
`effectifs`), rendu **optionnel** par une **union `["null", ...]`** avec `default: null` :
```json
{
  "name": "entreprise",
  "default": null,
  "type": [ "null",
    { "type": "record", "name": "Entreprise",
      "fields": [ {"name":"nom","type":"string"},
                  {"name":"siret","type":"string"},
                  {"name":"effectifs","type":"int"} ] } ]
}
```

**Résultat final** — la relecture (`avro_read.py`) montre bien les personnes avec intérêts (enum)
et entreprise optionnelle (`None` pour Priscile, qui n'a pas d'employeur) : *(sortie réelle)*
```
{'nom': 'Omar', 'age': 25, 'interets': ['SPORT', 'VOYAGE'], 'entreprise': {'nom': 'Padel SAS', 'siret': '12345678900011', 'effectifs': 12}}
{'nom': 'Priscile', 'age': 23, 'interets': ['LECTURE', 'MUSIQUE', 'CINEMA'], 'entreprise': None}
{'nom': 'Romain', 'age': 24, 'interets': ['CUISINE', 'VOYAGE', 'SPORT'], 'entreprise': {'nom': 'DataCorp', 'siret': '98765432100022', 'effectifs': 250}}
```

*Note (fichiers générés).* `users.avro` est un artefact binaire régénérable → il est **ignoré par
git** (`*.avro` dans `.gitignore`) ; seul le schéma `user.avsc` est versionné.

- **Qui a fait quoi :** _à compléter_.

#### Exercice 15 *(Bonus)* — Sérialisation sans fichiers (BytesIO)
*Statut : à faire.*

#### Exercice 16 *(Bonus)* — Sérialisation sans schéma (fastavro)
*Statut : à faire.*

### Partie Kafka + Avro

#### Exercice 17 — Sérialisation simple (Avro pour clés/valeurs)
*Statut : fait.*

On reprend le pipeline de logs de l'Exo 10, mais **clés et valeurs sont encodées en Avro**
(binaire brut, schéma non embarqué dans le message). Les schémas `.avsc` sont connus des deux
côtés ; un petit module `src/avro_utils.py` factorise l'encodage/décodage (`DatumWriter`/
`DatumReader` + `BinaryEncoder`/`BinaryDecoder` via `io.BytesIO`). Topic dédié `logs-avro`
(3 partitions) pour ne pas mélanger avec le texte brut de `logs`.

**Q1 — Deux schémas.** Un pour la **clé** (`src/log_key.avsc`), un pour la **valeur**
(`src/log_value_v1.avsc`) :
```json
// log_key.avsc                          // log_value_v1.avsc
{ "type":"record","name":"LogKey",       { "type":"record","name":"LogValue",
  "namespace":"fr.tp_kafka.opr",           "namespace":"fr.tp_kafka.opr",
  "fields":[                               "fields":[
    {"name":"url","type":"string"} ] }       {"name":"ip","type":"string"},
                                              {"name":"url","type":"string"} ] }
```

**Q2 — Producteur & consommateur en Avro** (`src/log_producer_avro.py`, `src/log_consumer_avro.py`).
Le producteur encode clé + valeur en bytes Avro et publie ; le consommateur les décode. *(extrait
producteur)*
```
$ uv run python src/log_producer_avro.py 5 5 1
Producteur Avro démarré → topic 'logs-avro' (version=1, Ctrl+C pour arrêter)
envoyé (v1) : 80.81.217.126   https://localhost/Xp2g
...
```
Côté consommateur, la clé et la valeur sont bien **décodées** (et non des octets bruts) :
```
[v1] cle=https://localhost/Xp2g  valeur={'ip': '80.81.217.126', 'url': 'https://localhost/Xp2g', ...}
```

**Q3 — Enrichir le log (date/heure + taille).** Nouvelle version de schéma `log_value_v2.avsc` :
ajoute `datetime` (string ISO) et `taille` (long, octets téléchargés, aléatoire), chacun avec une
**valeur par défaut** (utile pour la résolution en Q4) :
```json
{ "name":"datetime", "type":"string", "default":"" },
{ "name":"taille",   "type":"long",   "default":0  }
```
*Preuve (message v2 décodé) :*
```
[v2] cle=https://localhost/2uBv7xAZn2  valeur={'ip': '101.148.109.140', 'url': '.../2uBv7xAZn2',
      'datetime': '2026-06-18T10:42:02', 'taille': 9237, 'headers': {...}}
```

**Q4 — Consommateur compatible plusieurs versions.** Le producteur transmet la **version du
schéma dans un header Kafka** (`schema_version`). Le consommateur lit ce header, choisit le
**schéma d'écriture** correspondant, et décode en **résolvant** vers le schéma le plus récent
(reader = v3) → les champs absents des anciennes versions sont comblés par leurs **valeurs par
défaut**. Un **même** consommateur lit ainsi v1, v2 et v3 : *(sorties réelles)*
```
[v1] ... 'datetime': '',                  'taille': 0,       'headers': {'referer': '-', 'user_agent': '-'}
[v2] ... 'datetime': '2026-06-18T10:42:02','taille': 9237,    'headers': {'referer': '-', 'user_agent': '-'}
[v3] ... 'datetime': '2026-06-18T10:42:31','taille': 9698266, 'headers': {'referer': 'https://t.co', 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
```
On voit que les **v1** ont `datetime=''`/`taille=0`/headers par défaut, les **v2** ont
datetime/taille remplis mais headers par défaut, et les **v3** tous les champs.

**Q5 — Headers HTTP dans un record imbriqué.** `log_value_v3.avsc` ajoute un champ `headers` de
type **record `HttpHeaders { referer, user_agent }`** (contenu aléatoire) :
```json
{ "name":"headers", "default":{"referer":"-","user_agent":"-"},
  "type":{ "type":"record","name":"HttpHeaders",
           "fields":[ {"name":"referer","type":"string","default":"-"},
                      {"name":"user_agent","type":"string","default":"-"} ] } }
```
La preuve ci-dessus (ligne `[v3]`) montre le record `headers` correctement rempli et décodé.

**Bilan & lien Exo 19.** Le schéma n'étant **pas embarqué** dans les messages, producteur et
consommateur doivent partager les `.avsc` à l'avance et s'accorder sur la version (ici via un
header). C'est exactement le besoin que le **Schema Registry** (Confluent, Exo 19) industrialise :
centraliser les schémas et leur évolution au lieu de les distribuer manuellement.

- **Qui a fait quoi :** _à compléter_.

#### Exercice 18 *(Bonus)* — fastavro avec Kafka
*Statut : à faire.*

#### Exercice 19 *(Bonus)* — Confluent Kafka + Schema Registry
*Statut : à faire.*

---

## Répartition globale du travail
| Membre | Contributions principales |
|---|---|
| Omar | _à compléter_ |
| Priscile | _à compléter_ |
| Romain | _à compléter_ |
