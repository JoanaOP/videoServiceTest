import paho.mqtt.client as mqtt

import cv2 as cv2
import numpy as np
import base64

def on_message(cli, userdata, message):
    command = message.topic
    if command == 'videoFrame':
        image = base64.b64decode(bytes(message.payload.decode("utf-8"), "utf-8"))
        npimg = np.frombuffer(image, dtype=np.uint8)
        frame = cv2.imdecode(npimg, 1)
        img = cv2.resize(frame, (300, 400))
        res = cv2.flip(img, 1)
        cv2.imshow('image', res)
        cv2.waitKey(1)


def startService(connection_mode, operation_mode, external_broker, username, password):
    global cap
    global client

    print('Connection mode: ', connection_mode)
    print('Operation mode: ', operation_mode)

    # broker_address = "broker.hivemq.com"
    # broker_address = "localhost"

    if connection_mode == 'global':
        broker_address = external_broker
    else:
        broker_address = 'localhost'

    print('External broker: ', broker_address)

    broker_port = 8000

    cap = cv2.VideoCapture(0)

    client = mqtt.Client("VideoService",transport="websockets")
    if broker_address == 'classpip.upc.edu':
        client.username_pw_set(username, password)
    client.on_message = on_message # Callback function executed when a message is received
    client.max_queued_messages_set(1)
    client.max_inflight_messages_set(1)
    client.connect(broker_address, broker_port)
    client.subscribe('videoFrame')
    print('Waiting connection')

    client.loop_forever()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys

    connection_mode = sys.argv[1]  # global or local
    operation_mode = sys.argv[2]  # simulation or production
    username = None
    password = None
    if connection_mode == 'global':
        external_broker = sys.argv[3]
        if external_broker == 'classpip.upc.edu':
            username = sys.argv[4]
            password = sys.argv[5]
    else:
        external_broker = None

    startService(connection_mode,operation_mode, external_broker, username, password)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
