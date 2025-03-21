from fastapi import FastAPI
from aiokafka import AIOKafkaConsumer
import asyncio
import json

app = FastAPI()

KAFKA_TOPIC = "contract_topic"
KAFKA_BROKER = "localhost:9092"  # Change to your Kafka broker address


async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id="contract_group",  # Consumer group ID
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"📩 Received contract data: {msg.value}")
    finally:
        await consumer.stop()


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(consume())


@app.get("/")
async def root():
    return {"message": "Hello World!"}
