from kafka import KafkaConsumer
import json
from pymongo import MongoClient



client = MongoClient('mongodb+srv://jaunty:9410993055@mydb.drbzqzi.mongodb.net/')
db = client.kafkadb
colletion = db.kafkacollection
# Create an instance of the Kafka consumer
consumer = KafkaConsumer('tempo',
    bootstrap_servers='localhost:9091',
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Consume messages from the Kafka topic
for message in consumer:
    print(message.value)
    # vals = message.value['data']['message']
    # print(type(vals))
    # _ = colletion.insert_one({"value":vals})    
    # if(_):
    #     print("message consumed and stored")
    # consumer.close()
