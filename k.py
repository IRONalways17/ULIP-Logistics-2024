import paho.mqtt.client as mqtt

# Define the callback when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode('utf-8')}")

# MQTT setup
client = mqtt.Client()
client.on_message = on_message

client.connect("broker.hivemq.com", 1883)
client.subscribe("logistics/sensor")

client.loop_forever()
