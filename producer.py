from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
import json

#make sure to keep your twitter developer access keys secret
access_token = "Insert your own here"
access_token_secret = "Insert your own here"
api_key = "Insert your own here"
api_secret = "Insert your own here"

auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

#Creates a producer that sends data to the basic topic
class StdOutListener(Stream):
    def on_data(self, data):
        json_ = json.loads(data)
        producer.send("basic", json_["text"].encode('utf-8'))
        return True
    def on_error(self, status):
        print(status)

producer = KafkaProducer(bootstrap_servers='localhost:9092')
l = StdOutListener(api_key, api_secret, access_token, access_token_secret)
#Fill in the track argument with any keywords you would like to track
l.filter(track=["crypto"])

