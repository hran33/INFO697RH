from microbit import *
import random
import time

score = 0
count = 0

#display.scroll('If you see an even number, press button A')
#display.show(Image.ARROW_W)
#sleep(3000)

#display.scroll('If you see an odd number, press button B')
#display.show(Image.ARROW_E)
#sleep(3000)

#display.scroll('To exit and see your score, shake!')
#display.scroll('Start!')

num = random.randint(1, 100)
display.show(str(num))

while count < 5:
    time.sleep(1)
    count += 1
    if button_a.is_pressed():          #if even
        if (num % 2 == 0):              #if button-a is pressed
            display.show(Image.HAPPY)   #Correct
            sleep(1000)
            score += 1                  #Score+1
            num = random.randint(1, 100)
            display.show(str(num))
            count = 0
        else:
            display.show(Image.SAD)     #Wrong
            sleep(1000)
            num = random.randint(1, 100)
            display.show(str(num))
            count = 0
    elif button_b.is_pressed():
        if (num % 2 == 0):              #if button-a is pressed
            display.show(Image.SAD)     #Correct
            sleep(1000)
            num = random.randint(1, 100)
            display.show(str(num))
            count = 0
        else:
            display.show(Image.HAPPY)   #Wrong
            sleep(1000)
            num = random.randint(1, 100)
            display.show(str(num))
            score += 1
            count = 0
    elif count == 5:
        display.show('done')
        sleep(1000)
        num = random.randint(1, 100)
        display.show(str(num))
        count = 0
    elif accelerometer.was_gesture("shake"):
        break
display.scroll('You got' + str(score) + '!')