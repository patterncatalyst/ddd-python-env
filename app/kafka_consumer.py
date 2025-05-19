import json
import os
import threading
import asyncio
from confluent_kafka import Consumer, KafkaError
from typing import Dict, Any
from sqlalchemy.orm import Session
from .models import SessionLocal, Message

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
KAFKA_TOPIC = "messages"


class KafkaConsumer:
    def __init__(self):
        self.consumer = None
        self.running = False
        self._lock = threading.Lock()
        self._task = None

    async def start(self):
        with self._lock:
            if not self.running:
                conf = {
                    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
                    'group.id': 'message_consumer_group',
                    'auto.offset.reset': 'earliest'
                }
                self.consumer = Consumer(conf)
                self.consumer.subscribe([KAFKA_TOPIC])
                self.running = True
                self._task = asyncio.create_task(self.consume_messages())
                print("Kafka consumer started")

    async def stop(self):
        with self._lock:
            if self.running:
                self.running = False
                if self._task:
                    self._task.cancel()
                    try:
                        await self._task
                    except asyncio.CancelledError:
                        pass
                if self.consumer:
                    self.consumer.close()
                    self.consumer = None
                print("Kafka consumer stopped")

    async def consume_messages(self):
        try:
            while self.running:
                msg = self.consumer.poll(1.0)

                if msg is None:
                    # No message, continue polling
                    await asyncio.sleep(0.1)
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event - not an error
                        continue
                    else:
                        print(f"Error: {msg.error()}")
                        continue

                try:
                    # Deserialize message
                    message_value = json.loads(msg.value().decode('utf-8'))
                    print(f"Received message: {message_value}")

                    # Process in a separate task to not block the consumer
                    asyncio.create_task(self.process_message(message_value))

                except Exception as e:
                    print(f"Error processing message: {e}")

        except Exception as e:
            print(f"Error in consume_messages: {e}")
            if self.running:
                # Wait before reconnecting
                await asyncio.sleep(5)
                # Restart consumer loop
                self._task = asyncio.create_task(self.consume_messages())

    async def process_message(self, message: Dict[str, Any]):
        try:
            with SessionLocal() as db:
                db_message = Message(content=message.get("content", ""))
                db.add(db_message)
                db.commit()
                print(f"Stored message in database: {db_message}")
        except Exception as e:
            print(f"Error processing message: {e}")


consumer = KafkaConsumer()