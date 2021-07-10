import random
import time
import datetime
from paho.mqtt import client as mqtt_client

def connect_mqtt():
    ### CONNECT PUBLISHER TO BROKER ###
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client_id = f"python-mqtt-{random.randint(0, 1000)}"
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect("broker.emqx.io", port=1883)
    return client

def agency():
    ### Fungsi untuk pemilihan agensi ###
    global topic
    SM = "SMTOWN"
    YG = "YGEntertaiment"
    print(f"pilih input ke : \n 1 SMTOWN \n 2 YGEntertaiment")
    command = input()
    if command == str(1):
        topic = SM
    elif command == str(2):
        topic = YG
    print()

def publish(client):
    global topic
    SM = "SMTOWN"
    YG = "YGEntertaiment"
    if topic == SM:
        client.publish(topic, "default jadwal:2021-06-11 10:15:00")
        client.publish(topic, "default jadwal:2021-06-12 06:30:00")
        client.publish(topic, "default jadwal:2021-06-22 16:45:00")
    elif topic == YG:
        client.publish(topic, "default jadwal:2021-06-11 11:11:00")
        client.publish(topic, "default jadwal:2021-06-12 11:11:00")
        client.publish(topic, "default jadwal:2021-06-22 11:11:00")

    command = 1
    while command != 0:
        print(
            "pilih input ke : \n 0 untuk keluar \n 1 untuk melakukan publish \n 2 untuk ke menu utama"
        )
        command = input()
        if command == str(0):
            exit()
        if command == str(1):
            pesan = input("pesan :")
            jadwal = datetime.datetime.strptime(
                input("Jadwal mulai `YYYY/mm/dd - HH:MM`  format: "), "%Y/%m/%d - %H:%M")
            msg = f"{pesan} jadwal:{jadwal}"
            client.publish(topic, msg)
            client.loop_start()
            client.loop_stop()
        if command == str(2):
            agency()

def run():
    global topic
    agency()
    print(topic)
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == "__main__":
    run()

# while Connected != True:  # Wait for connection
#     time.sleep(0.1)
# try:
#     while True:
#         time.sleep(1)
#
# except KeyboardInterrupt:
#     print("exiting")
#     client.disconnect()
#     client.loop_stop()
