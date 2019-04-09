from microbit import *

#scale mode - set up
def setup():
    display.scroll("Please empty the scale to set up.")
    scale_ready = False
    pin1.write_digital(1)
    #sense if the scale is empty
    #if it's empty, initialization finished
    #display.scroll ("Initialization complete")
def brew():
    #First brew
    display.scroll("First brew 1")
    #Weigh the cup
    #weigh the ground coffee-30 grams
    #Add 60grams of water
    #if scale number >= 60
        #start timer
        #countdown 30 seconds
        #display.scroll("Second brew 2")
        #Add 90 grams of water to 150 grams total
        #if scale number >= 150
            #start timer
            #countdown 30 seconds
            #display.scroll("Third brew 3")
            #Add 100 grams of water to 250 grams total
            #if scale number >= 250
                #start timer
                #countdown 20 seconds
                #display.scroll("Fourth brew 4")
                #Add 100 grams of water to 250 grams total
                #if scale number >= 250
                    #start timer
                    #countdown 20 seconds
                    #display.scroll("Enjoy!")
while True:
    if button_a.was_pressed():
        #enter scale mode
        setup()
        display.show("scale mode 0")
    elif button_b.was_pressed():
        #enter brewing mode
        brew()
