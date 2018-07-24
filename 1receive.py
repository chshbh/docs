import pika

# connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create message queue
# can avoid this step if queue declared previously, doesn't matter, queue_declare is idempotent
channel.queue_declare(queue='hello')


# listing queues
# sudo rabbitmqctl list_queues

#  subscribing a callback function to a queue
def callback(ch, method, properties, body):
    print(" [x] Received {}".format(body))


# tell which queue to subscribe to
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
