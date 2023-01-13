import pika

host = 'localhost'
queue = 'my-queue'
exchange = "sample_exchange"
exchange_type='topic'
binding_key = "message.otp"

def on_message(ch, method, properties, body):
    message = body.decode('UTF-8')
    print(message)

def main():
    connection_params = pika.ConnectionParameters(host=host)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)

    channel.queue_declare(queue=queue)
    channel.queue_bind(exchange=exchange, queue= queue, routing_key=binding_key)

    channel.basic_consume(queue=queue, on_message_callback=on_message, auto_ack=True)

    print('Subscribed to ' + queue + ', waiting for messages...')
    channel.start_consuming()

if __name__ == '__main__':
    main()