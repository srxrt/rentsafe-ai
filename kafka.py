from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from analyzer import analyze
import json

KAFKA_TOPIC = "contract_topic"
KAFKA_TOPIC_REPLY = "contract_topic.reply"
KAFKA_BROKER = "localhost:10000,localhost:10001,localhost:10002"

producer = None


async def produce(response_data):
    global producer
    if producer is None:
        producer = AIOKafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        await producer.start()
    try:
        print(await producer.send_and_wait(KAFKA_TOPIC_REPLY, value=response_data))
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        print("Message has been send!")


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
            # TODO: analyze the contract with OpenAI api
            # get the response_data
            print(f"📩 Received contract data: {msg.value}")

            response_data = await analyze(msg.value)
            await produce(response_data)
    finally:
        await consumer.stop()


async def stop_producer():
    global producer
    if producer:
        await producer.stop()
        producer = None
