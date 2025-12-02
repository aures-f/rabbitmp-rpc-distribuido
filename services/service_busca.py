import pika, json, time

params = pika.ConnectionParameters(
    "localhost",
    heartbeat=0,
    blocked_connection_timeout=0
)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="rpc_busca")

def busca(q):
    time.sleep(1)
    banco = ["banana", "uva", "maçã", "laranja", "abacaxi"]
    return [x for x in banco if q.lower() in x.lower()]

def on_request(ch, method, props, body):
    data = json.loads(body.decode())
    result = busca(data["query"])

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        body=json.dumps(result)
    )

    ch.basic_ack(method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="rpc_busca", on_message_callback=on_request)
print("Service iniciado. Aguardando mensagens...")

while True:
    try:
        connection.process_data_events(time_limit=1)
    except KeyboardInterrupt:
        break

