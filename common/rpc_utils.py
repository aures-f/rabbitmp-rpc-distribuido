import pika
import json

class RPCClient:
    def __init__(self):
        params = pika.ConnectionParameters(
            "localhost",
            heartbeat=0,
            blocked_connection_timeout=0
        )

        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self._on_response,
            auto_ack=True
        )

        self.response = None

    def _on_response(self, ch, method, props, body):
        self.response = body

    def call(self, queue, payload):
        self.response = None

        self.channel.basic_publish(
            exchange='',
            routing_key=queue,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue
            ),
            body=json.dumps(payload)
        )

        while self.response is None:
            self.connection.process_data_events()

        return json.loads(self.response.decode())
