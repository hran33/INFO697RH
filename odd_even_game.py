from microbit import *
import random

score = 0
gameround = 0

#display.scroll('If you see an even number, press button A')
#display.show(Image.ARROW_W)
#sleep(3000)

#display.scroll('If you see an odd number, press button B')
#display.show(Image.ARROW_E)
#sleep(3000)

while (gameround < 5):
    display.show(str(num))                  #display number
    sleep(6000)
    if (num % 2 == 0) :                 #if even
        if button_a.was_pressed():       #if button-a is pressed
            display.show(Image.HAPPY)   #Correct
            sleep(1000)
            score += 1                  #Score+1
        elif button_b.was_pressed():     #if button-b is pressed
            display.show(Image.SAD)     #Wrong
            sleep(1000)
        elif running_time() > 5000:     #if no response
            display.show(Image.SAD)     #Wrong
            sleep(1000)
    else:                               #if odd
        if button_a.was_pressed():       #if button-a is pressed
            display.show(Image.SAD)     #Wrong
            sleep(1000)
        elif button_b.was_pressed():     #if button-b is pressed
            display.show(Image.HAPPY)   #Corret!
            sleep(1000)
            score += 1                  #Score+1
        elif running_time() > 5000:     #if no response
            display.show(Image.SAD)     #Wrong
            sleep(1000)
    gameround = gameround + 1
display.scroll('You got' + str(score) + '!')     #show score

display.scroll('Press the button on the back to play again!')     #how to restart
display.show(Image.ARROW_N)
display.clear()