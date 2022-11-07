import time
import board
import busio

import paho.mqtt.client as mqtt
import uuid

import board
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/testing'


while True:
    gesture = apds.gesture()
    val = ""
    if gesture == 0x01:
        print("up")
        val = "up"
        client.publish(topic, val)
    elif gesture == 0x02:
        print("down")
        val = "down"
        client.publish(topic, val)
    elif gesture == 0x03:
        print("left")
        val = "left"
        client.publish(topic, val)
    elif gesture == 0x04:
        print("right")
        val = "right"
        client.publish(topic, val)
    