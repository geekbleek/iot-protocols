import paho.mqtt.client as mqtt

broker_ip = "128.107.70.30" #external Broker when running local [mqtt.cisco.com]
broker_port = 1883
#mqtt_topic = 'devnetzone/mqtt/topic'
train_topic = 'devnetzone/train/data'

class ReadMsg:
    def on_connect(self, master, obj, flags, rc):
        self.master.subscribe(train_topic) # change MQTT topic to reflect your bot

    def on_message(self, master, obj, msg):
        msgStr = msg.payload.decode("utf-8")
        print('MESSAGE Received [x] ' + msgStr)

    def __init__(self, master):
        self.master = master
        self.master.on_connect = self.on_connect
        self.master.on_message = self.on_message
        self.master.connect(broker_ip, broker_port, 60)

if __name__ == '__main__':
    client = mqtt.Client()
    ob1 = ReadMsg(client)
    client.loop_forever()