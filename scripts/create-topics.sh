#!/usr/bin/env bash
set -e

until kafka-topics --bootstrap-server kafka:9092 --list >/dev/null 2>&1; do
  echo "Waiting for Kafka..."
  sleep 2
done

kafka-topics --bootstrap-server kafka:9092 \
  --topic messages --create --partitions 3 --replication-factor 1

kafka-topics --bootstrap-server kafka:9092 \
  --topic analytics --create --partitions 3 --replication-factor 1

echo "Topics created!"
