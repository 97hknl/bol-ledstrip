import machine
import sys
import settings
import time
import ubinascii
# import connect
import wifimgr

from color import colors
from ledstrip import LedStrip
from umqtt.simple import MQTTClient


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
    try:
        msg = msg.decode().lower()
        print('received cmd: {}'.format(msg))
        cmds = msg.split('/')
        print(cmds)

        if cmds[0]=='clear':
            strip.all(colors['BLACK'])
        elif cmds[0]=='add':
            strip.add(colors[cmds[1].upper()])
        elif cmds[0]=='all':
            strip.all(colors[cmds[1].upper()])
        elif cmds[0]=='set':
            strip.set_color(int(cmds[1]), colors[cmds[2].upper()])
        elif cmds[0]=='blink':
            strip.blink(int(cmds[1]), colors[cmds[2].upper()])
        else:
            strip.blink(2, colors['RED'])
            print('Unknown command: {}'.format("/".join(cmds)))
        
        strip.update()
    
    except Exception as e:
        sys.print_exception(e)
        strip.blink(2, colors['RED'])

def connect():
    while True:
        try:
            mqtt_client.connect(clean_session=True)
            mqtt_client.subscribe(settings.MQTT_TOPIC)
            break
        except Exception as e:
            sys.print_exception(e)
            time.sleep(1)


mqtt_client = MQTTClient(ubinascii.hexlify(machine.unique_id()), settings.MQTT_HOST)
mqtt_client.DEBUG=True
mqtt_client.set_callback(on_message)

connect()

while True:
    try:
        mqtt_client.wait_msg()
    except Exception as e:
        sys.print_exception(e)
        connect()


mqtt_client.disconnect()
