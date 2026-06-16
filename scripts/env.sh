#!/usr/bin/env bash
# Variables d'environnement pour le TP Kafka.
# À sourcer dans CHAQUE terminal WSL avant de lancer ZooKeeper/Kafka :
#   source /mnt/c/tp_kafka/scripts/env.sh
#
# (On ne modifie pas ~/.bashrc volontairement : l'env reste explicite et local au TP.)

export JAVA_HOME="$HOME/jdk-17"
export PATH="$JAVA_HOME/bin:$HOME/kafka/bin:$PATH"
