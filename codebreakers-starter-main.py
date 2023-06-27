from microbit import *
import radio
radio.on()

radio.config(queue=1, channel=7)

while True:
    display.show(Image.HEART)
    sleep(1000)
    display.scroll('I am a micro:bit')
