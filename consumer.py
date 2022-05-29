from kafka import KafkaConsumer

#Creates consumer that consumes messages from basic topic
consumer = KafkaConsumer(
    'basic',
     bootstrap_servers='localhost:9092',
     auto_offset_reset='earliest',
     enable_auto_commit=True,
)

counter = 0
#Fill in the if clause with keywords related to the topic you are tracking if you would like to see how often they come up.
for i in consumer:
    print(i.value.decode('utf-8'))
    if 'terra' in i or 'TERRA' in i or 'LUNA' in i or 'luna' in i:
        counter += 1
    print(f"{counter} tweets have mentioned terra or luna so far.")




