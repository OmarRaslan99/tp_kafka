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
*Statut : à faire.*

#### Exercice 10 *(Bonus)* — Centralisation de logs dans Kafka
*Statut : à faire.*

#### Exercice 11 *(Bonus)* — Déploiement pseudo-distribué
*Statut : à faire.*

#### Exercice 12 *(Bonus)* — Déploiement distribué
*Statut : à faire.*

### Partie Avro

#### Exercice 13 — Installer Avro
*Statut : à faire.*

#### Exercice 14 — Premiers pas avec Avro
*Statut : à faire.*

#### Exercice 15 *(Bonus)* — Sérialisation sans fichiers (BytesIO)
*Statut : à faire.*

#### Exercice 16 *(Bonus)* — Sérialisation sans schéma (fastavro)
*Statut : à faire.*

### Partie Kafka + Avro

#### Exercice 17 — Sérialisation simple (Avro pour clés/valeurs)
*Statut : à faire.*

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
