from fastapi import FastAPI
from aiokafka import AIOKafkaConsumer
import asyncio
import json

app = FastAPI()

KAFKA_TOPIC = "contract_topic"
KAFKA_BROKER = "localhost:10000,localhost:10001,localhost:10002"  # Change to your Kafka broker address


async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id="contract_group",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"📩 Received contract data: {msg.value}")
    finally:
        await consumer.stop()


@app.on_event("startup")
async def start_kafka_consumer():
    asyncio.create_task(consume())  # Run the consumer in the background


@app.get("/")
async def root():
    return {"message": "Hello World!"}
