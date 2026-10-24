from kafka import KafkaProducer, KafkaConsumer

BOOTSTRAP = "13.221.125.193:9092"  

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP)
producer.send("topic-prueba", b"Mision cumplida desde mi PC a AWS")
producer.flush()
print("Mensaje enviado con exito.")

consumer = KafkaConsumer(
    "topic-prueba",
    bootstrap_servers=BOOTSTRAP,
    auto_offset_reset="earliest",
    consumer_timeout_ms=5000
)
for msg in consumer:
    print("Recibido de vuelta:", msg.value.decode())
    break