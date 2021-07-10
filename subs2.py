import random
import time
from paho.mqtt import client as mqtt_client

def connect_mqtt(client: mqtt_client):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!\n")
        else:
            print("Failed to connect, return code %d\n", rc)

    client.on_connect = on_connect
    client.connect("broker.emqx.io", port=1883)

def subs_menu(client):
    subs = []
    SM = "SMTOWN"
    YG = "YGEntertaiment"
    print(f"Sekarang sedang subscribe {subs}")
    print(f"Subscribe: \n 1 {SM} \n 2 {YG}")
    command = input()
    if command == str(1):
            subs.append(SM)
            client.subscribe(SM)
    elif command == str(2):
            subs.append(YG)
            client.subscribe(YG)

    print(f"Sekarang subscribe {subs}")
    if subs == SM:
        print(f"Jadwal Default {subs} ")
    else:
        print(f"Jadwal Default {subs} ")
    print()

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

def run():
    global client_id
    client_id = f"python-mqtt-{random.randint(0, 1000)}"
    client = mqtt_client.Client(client_id)
    connect_mqtt(client)
    client.loop_start()
    time.sleep(1)
    subs_menu(client)

    while True:
        client.on_message = on_message
        inputs = input()
        if inputs == "menu":
            subs_menu(client)
        time.sleep(1)
        try:
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            print("keluar")
            client.disconnect()
    client.loop_stop()


if __name__ == "__main__":
    run()
