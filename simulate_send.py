import json
import pika

# parse json
with open("simulate_data.json") as json_file:
    message = json.load(json_file)


# connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create exchange
channel.exchange_declare(exchange='events',
                         exchange_type='direct')

# bind route
event_log = message[type]

# establish exchange
channel.basic_publish(exchange='direct_logs',
                      routing_key=event_log,
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
