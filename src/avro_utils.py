"""Exercice 17 — utilitaires de (dé)sérialisation Avro pour Kafka.

Encode/décode un enregistrement en **binaire Avro brut** (sans embarquer le
schéma dans le message, contrairement au format fichier `DataFileWriter`). Les
schémas `.avsc` sont donc connus à l'avance des deux côtés ; c'est cette
contrainte que le Schema Registry (Exo 19) industrialise.
"""

import io

import avro.schema
from avro.io import BinaryDecoder, BinaryEncoder, DatumReader, DatumWriter


def load_schema(path):
    """Charge un schéma Avro depuis un fichier .avsc."""
    with open(path, encoding="utf-8") as f:
        return avro.schema.parse(f.read())


def serialize(schema, datum):
    """Sérialise `datum` selon `schema` et renvoie les octets Avro bruts."""
    buffer = io.BytesIO()
    DatumWriter(schema).write(datum, BinaryEncoder(buffer))
    return buffer.getvalue()


def deserialize(writer_schema, reader_schema, data):
    """Désérialise `data` (octets Avro) avec résolution de schéma.

    `writer_schema` = schéma ayant servi à l'écriture (version du message),
    `reader_schema` = schéma attendu par le lecteur (les champs absents sont
    comblés par leurs valeurs par défaut).
    """
    reader = DatumReader(writer_schema, reader_schema)
    return reader.read(BinaryDecoder(io.BytesIO(data)))
