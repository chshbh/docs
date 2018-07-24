# work queue

The assumption behind a work queue is that each task is delivered to exactly one worker.

# publish/subscribe pattern

Deliver a message to multiple consumers.

# exchanges

```
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
```

- ``` sudo rabbitmqctl list_exchanges ```
- ``` sudo rabbitmqctl list_bindings ```

## messaging model

- A producer is a user application that sends messages.
- A queue is a buffer that stores messages.
- A consumer is a user application that receives messages.

- *producer -> exchanges[exchanges_type] -> queue*
- *temporary queues*
- The relationship between exchange and a queue is called a binding.

# logging system

- ``` python receive_logs.py > logs_from_rabbit.log ```
- ``` python receive_logs.py ```
- ``` python emit_log.py ```
