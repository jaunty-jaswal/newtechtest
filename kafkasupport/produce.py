from kafka import KafkaProducer
import json
from model import models
from fastapi import APIRouter

router = APIRouter()
@router.post('/produce')
def produce(ob:models.data):
    producer = KafkaProducer(bootstrap_servers='localhost:9091',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send('tempo', {'data':ob.model_dump()})
    producer.flush
    producer.close
    return {"response":"message sent"}