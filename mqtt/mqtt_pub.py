import paho.mqtt.client as mqtt


broker_ip = "128.107.70.30" #external Broker when running local [mqtt.cisco.com]
broker_port = 1883
mqtt_topic = 'devnetzone/topic'
payload = '{"message":"Hello World"}'


def mqtt_pub(payload): #function to publish payload to a topic
    client = mqtt.Client()
    client.connect(broker_ip, broker_port, 60)
    client.publish(mqtt_topic, payload)
    print('MESSAGE PUB [x] ' + payload)
    client.disconnect()


if __name__ == '__main__':
    mqtt_pub(payload)