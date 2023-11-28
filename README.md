# CSCI 602 Holy City IoT - Temperature Sensor WebApp

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Environment Setup (WebApp)

1.) Install Flask [here](https://flask.palletsprojects.com/en/2.2.x/installation/). If you have Pip installed use `pip3`.

```bash
pip3 install Flask
```

2.) Install Twilio [here](https://www.twilio.com/docs/libraries/python). If you have Pip installed use `pip3`.

```bash
pip3 install twilio
```

3.) Install Paho MQTT [here](https://www.eclipse.org/paho/index.php?page=clients/python/index.php). If you have Pip installed use `pip3`.

```bash
pip3 install paho-mqtt
```

4.) Clone down the repository from Github

```bash
git clone git@git.github.com:CitadelCS/pulsar-iot-{yourUsername}.git
```

5.) Replace strings with connection information in variables: `hostname` and `host`, and replace `if` statements with desired MQTT `topic/s`

6.) Run the receive_sms.py file

```bash
cd twilio_handler
python3 receive_sms.py
```

You should see a message saying `Running on http://<your_IP_ADDRESS:5002>` if the Flask App is running.

## Environment Setup (Microcontroller Endpoint)

1.) Connect the Microcontroller and Temperature Sensor together in the following configuration:

![alt text](https://raw.githubusercontent.com/CitadelCS/pulsar-iot/master/WiringDiagram.jpg?token=GHSAT0AAAAAAB37ZNYY3R2SR5NNNENBLQF4Y4YCSQQ)

2.) Install the 8266 compiler in Arduino IDE [here](https://randomnerdtutorials.com/how-to-install-esp8266-board-arduino-ide/) or use an ESP/8266 compatible IDE+compiler.

3.) Open firmware in IDE `\Firmware\tempToPubSub_X2.ino'.`

4.) Select board `NodeMCU 1.0 (ESP-12E)`.

5.) Replace strings with connection information in variables: `ssid`, `password`, and `mqtt_server`, and specify desired topic in `client.publish("<insert topic>", msg);`

6.) Flash microcontroller

You should see a message in the Serial Port Monitor saying:

```
WiFi connected
IP address: 
<Your IP Address>
Attempting MQTT connection...connected
Publish message: Temperature in ºF : #<Your Temp>
```

## Environment Setup (Twilio Webhooks)

1.) Setup a Twilio Account

2.) Create an Active Number [here](https://console.twilio.com/us1/develop/phone-numbers/manage/incoming) and verify Caller IDs [here](https://console.twilio.com/us1/develop/phone-numbers/manage/verified)

3.) Go to Active Numbers [here](https://console.twilio.com/us1/develop/phone-numbers/manage/incoming). Click on the desired number. 

4.) Under the `Messaging` field, confirm `Webhook` is selected in the drop down box under `A Message Comes In`.

5.) In the HTTP field, enter the server IP or Domain Address followed by the port number and `/sms/` and confirm `HTTP Post` is selected. Example: `http://<you_IP_ADDRESS>:5002/sms`

6.) Send your `topic` name to the desired number selected in 3.)

7.) Message should be received with temperature.

8.) Success!

## Resources

### Flask

For further references with Flask:

- [Getting Started](https://flask.palletsprojects.com/en/2.2.x/)

### Eclipse MQTT and Paho

For further references with Paho:

- [Getting Started](https://www.eclipse.org/paho/index.php?page=documentation.php)

### Twilio

For further references with Twilio in Python:

- [Getting Started](https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python)

### NodeMCU CP2102 ESP-12E

Link to purchase the 8266 Microcontroller:

- [Amazon](https://a.co/d/8uU6RHk)


### DS18B20 Temperature Sensor

Link to purchase the temperature sensor:

- [Amazon](https://a.co/d/dlplqOH)


