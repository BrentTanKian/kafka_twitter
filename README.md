# kafka_twitter
Small kafka project that streams tweet data according to a specified topic. 
## Instructions
1. In the producer.py script, fill in the access_tokens and api keys/secrets with your own (You can get them from the twitter developer website)
2. Get your local Kafka cluster up and running.
-Run the command .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties to get zookeeper running (I'm on a windows machine, so you might need
to replace .bat with .sh if you're using a mac)
-Then run the command .\bin\windows\kafka-server-start.bat .\config\server.properties to get the kafka broker started
3. Fill in the track argument in the last line of the producer.py file with the keyword that you wish to track tweets on and run producer.py
4. Fill in the if clause in the consumer.py file with additional related keywords if you want to track how often they come up and run consumer.py

If everything runs smoothly, you should see tweet data flowing in and look like what you see on the Capture.PNG screenshot.
