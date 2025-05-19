import json
import os
from confluent_kafka import Producer
from typing import Dict, Any
import threading

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC = "messages"


class KafkaProducer:
    def __init__(self):
        self.producer = None
        self._lock = threading.Lock()

    async def start(self):
        with self._lock:
            if self.producer is None:
                conf = {'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS}
                self.producer = Producer(conf)
                print("Kafka producer started")

    async def stop(self):
        with self._lock:
            if self.producer:
                # Flush any remaining messages
                self.producer.flush()
                self.producer = None
                print("Kafka producer stopped")

    async def send_message(self, message: Dict[str, Any]):
        await self.start()

        # Serialize the message to JSON
        message_json = json.dumps(message).encode('utf-8')

        # Produce the message
        self.producer.produce(KAFKA_TOPIC, value=message_json)
        # Flush to ensure delivery
        self.producer.flush()

        print(f"Sent message to Kafka: {message}")


producer = KafkaProducer()