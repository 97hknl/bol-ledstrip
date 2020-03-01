import network
import utime

from color import colors
import settings

def connect(strip):
    
    wlan = network.WLAN(network.STA_IF)
    while not wlan.isconnected():
        strip.set_color(0, colors['YELLOW'])
        strip.update()
        print('connecting to network ' + settings.WIFI_SSID + ' ...')
        
        wlan.active(True)
        wlan.connect(settings.WIFI_SSID, settings.WIFI_PASSWORD)
        strip.set_color(0, colors['RED'])
        strip.update()
        utime.sleep(5)

    strip.clear()
    print('connected to ' + settings.WIFI_SSID)
