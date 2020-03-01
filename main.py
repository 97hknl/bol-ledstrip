import machine
import settings
# import connect
import wifimgr

from color import colors
from ledstrip import LedStrip
from umqtt.robust import MQTTClient


strip_length = 60
brightness = 0.1
strip = LedStrip(machine.Pin(settings.LEDSTRIP_PIN), strip_length)

strip.blink(2, colors['YELLOW'])

wlan = wifimgr.get_connection()
if wlan.isconnected():
    strip.blink(2, colors['BLUE'])
else:
    strip.blink(10, colors['RED'])


def on_message(topic, msg):
    msg = msg.decode().lower()
    print('received cmd: {}'.format(msg))
    cmds = msg.split('/')
    print(cmds)

    if cmds[0]=='clear':
        strip.all(colors['BLACK'])
    elif cmds[0]=='all':
        strip.all(colors[cmds[1].upper()])
    elif cmds[0]=='set':
        strip.set_color(int(cmds[1]), colors[cmds[2].upper()])
    elif cmds[0]=='blink':
        strip.blink(int(cmds[1]), colors[cmds[2].upper()])
    
    strip.update()
        

mqtt_client = MQTTClient("client", settings.MQTT_HOST)
mqtt_client.set_callback(on_message)

if not mqtt_client.connect():
    mqtt_client.subscribe(settings.MQTT_TOPIC)

while True:
    mqtt_client.wait_msg()
