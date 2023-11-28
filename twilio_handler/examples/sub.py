import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("temp", hostname="<insert webapp domain name or ip address>")
print("%s %s" % (msg.topic, msg.payload))

