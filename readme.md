ls /dev/ | grep -i "tty" | grep -i "usb"

screen /dev/tty.SLAB_USBtoUART 115200
ampy -d 0.5 -p /dev/tty.SLAB_USBtoUART -b 115200 put <<file>>


192.168.4.1

mosquitto_pub -h <<MQTT_HOST>> -t <<MQTT_TOPIC>> -m 'clear'
mosquitto_pub -h <<MQTT_HOST>> -t <<MQTT_TOPIC>> -m 'all/green'
mosquitto_pub -h <<MQTT_HOST>> -t <<MQTT_TOPIC>> -m 'blink/5/red'
mosquitto_pub -h <<MQTT_HOST>> -t <<MQTT_TOPIC>> -m 'set/0/red'
mosquitto_pub -h <<MQTT_HOST>> -t <<MQTT_TOPIC>> -m 'set/1/yellow'

