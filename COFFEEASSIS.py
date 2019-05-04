from gpiozero import DigitalInputDevice
from gpiozero import Button
import sys
import I2C_LCD_driver
import time
import RPi.GPIO as GPIO

pin0 = DigitalInputDevice(17)
pin1 = DigitalInputDevice(27)
#button = Button (22, pull_up = False)
mylcd = I2C_LCD_driver.lcd()

globalWeight = 0

EMULATE_HX711=False

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711
hx = HX711(5, 6)
hx.set_reference_unit(379)
hx.reset()
hx.tare()

def showweight():
    val = hx.get_weight(5)
    global globalWeight
    globalWeight = globalWeight + val
    mylcd.lcd_display_string("W:"+str(globalWeight)+"g",2)

def timer():
	for i in range (0,30,1):
	    mylcd.lcd_display_string("T:"+str(i)+"s",2,8)
	    time.sleep(1)
	    if pin1.value == 1:
                continue

def instruct():
    mylcd.lcd_display_string("Button A: Timer", 1)
    mylcd.lcd_display_string("button B: Reset", 2)
    time.sleep(2)
    mylcd.lcd_clear()

while True:
    #instruct()
    mylcd.lcd_display_string("WEIGHING..",1)
    showweight()
    if pin1.value == 1:
        for i in range (0,30,1):
	    mylcd.lcd_display_string("T:"+str(i)+"s",2,8)
	    time.sleep(1)
	    if pin1.value == 1: break
	mylcd.lcd_display_string(" "*6,2,8)
    if pin0.value == 1:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("RESETING..",1)   
        time.sleep(3)
GPIO.cleanup()
