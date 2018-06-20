import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received {}".format(body))
    time.sleep(10 * body.count(b'.'))
    print(" [x] Done")
    # ack config
    ch.basic_ack(delivery_tag=method.delivery_tag)


# fair dispatch
channel.basic_qos(prefetch_count=1)

# remove no_ack=True flag
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
