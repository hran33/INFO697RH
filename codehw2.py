from microbit import *
import time

full = Image("99999:""99999:""99999:""99999:""99999:")
empty = Image("00000:""00000:""00000:""00000:""00000:")

#scale mode - set up
def setup():
    display.scroll("Please empty the scale to set up.")
    scale_ready = False
    pin1.write_digital(1)
    #sense if the scale is empty
    #if it's empty, initialization finished
    #display.scroll ("Initialization complete")
#brew mode - 4 brews
def brew():
    #Weigh the cup
    #Weigh the ground coffee-30 grams
    #Add 60grams of water
    display.scroll("Add water to 60")
    #First brew
    display.scroll("First brew 1")
    #if scale number >= 60
    #start timer, countdown 30 seconds
    for i in range(30, 0, -1):
        display.show(i)
        time.sleep(1)
    #flash led when times up and remind to add water
    for x in range (5):
        display.show(full)
        sleep(100)
        display.show(empty)
        sleep(100)
    #Add 90 grams of water
    display.scroll("Add water to 150")
    #Second brew
    display.scroll("Second brew 2")
    #if scale number >= 150
    #start timer, countdown 30 seconds
    for i in range(30, 0, -1):
        display.show(i)
        time.sleep(1)
    #flash led and remind to start third brew
    for x in range (5):
        display.show(full)
        sleep(100)
        display.show(empty)
        sleep(100)
    display.scroll("Add water to 250")
    display.scroll("Third brew 3")
    #Add 100 grams of water to 250 grams total
    #if scale number >= 250
    #start timer, countdown 20 seconds
    for i in range(20, 0, -1):
        display.show(i)
        time.sleep(1)
    #flash led and remind to start third brew
    for x in range (5):
        display.show(full)
        sleep(100)
        display.show(empty)
        sleep(100)
    display.scroll("Add water to 350")
    display.scroll("Fourth brew 4")
    #if scale number >= 350
    #start timer, countdown 20 seconds
    for i in range(20, 0, -1):
        display.show(i)
        time.sleep(1)
    #flash led and complete brewing
    for x in range (5):
        display.show(full)
        sleep(100)
        display.show(empty)
        sleep(100)
    display.scroll("Enjoy!")
while True:
    if button_a.was_pressed():
        #enter scale mode
        setup()
        display.show("scale mode 0")
    elif button_b.was_pressed():
        #enter brewing mode
        brew()
