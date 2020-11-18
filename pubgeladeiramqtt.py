import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import random
import time
import configparser

broker = "mqtt.thingspeak.com"
port = 1883

config = configparser.ConfigParser()
config.read('conf')
topic = config['THINGSPEAK']['TOPIC_PUBLISH']

status_geladeira = 0

while True:
  status_geladeira = random.randint(0,1)

  if status_geladeira == 1:
    dados="field1={}&status=MQTTPUBLISH".format(status_geladeira)
    publish.single(payload=dados,topic=topic,port=port,hostname=broker)
    print(dados)
    time.sleep(10)