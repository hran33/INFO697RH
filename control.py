from microbit import *
import time
pin1.write_digital(0)
pin0.write_digital(0)
while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
        pin1.write_digital(1)
        time.sleep(3)
        pin1.write_digital(0)
    if button_b.was_pressed():
        display.show(Image.COW)
        pin0.write_digital(1)
        time.sleep(3)
        pin0.write_digital(0)
    else:
        display.show(Image.ARROW_W)
        pin1.write_digital(0)
        pin0.write_digital(0)