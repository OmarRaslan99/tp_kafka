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
*Statut : à faire.*

#### Exercice 5 — Groupes et offsets
*Statut : à faire.*

#### Exercice 6 — Parallélisation du traitement
*Statut : à faire.*

#### Exercice 7 — Plusieurs traitements par message (groupes distincts)
*Statut : à faire.*

#### Exercice 8 — Explorer ZooKeeper
*Statut : à faire.*

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
