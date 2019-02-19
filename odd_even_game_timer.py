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
    if button_a.is_pressed():             #when button_a is pressed
        if (num % 2 == 0):                #if even
            display.show(Image.HAPPY)     #Correct
            sleep(1000)
            score += 1                    #Score+1
            num = random.randint(1, 100)  #generate new num
            display.show(str(num))        #show number
            count = 0                     #restart countdown
        else:                             #if odd
            display.show(Image.SAD)       #Wrong
            sleep(1000)
            num = random.randint(1, 100)  #generate new num
            display.show(str(num))        #show number
            count = 0                     #restart countdown
    elif button_b.is_pressed():           #if button-bis pressed
        if (num % 2 == 0):                #if even
            display.show(Image.SAD)       #Wrong
            sleep(1000)
            num = random.randint(1, 100)  #generate new num
            display.show(str(num))        #show number
            count = 0                     #restart countdown
        else:                             #if odd
            display.show(Image.HAPPY)     #Correct
            sleep(1000)
            num = random.randint(1, 100)  #generate new num
            display.show(str(num))        #show number
            score += 1                    #score+1
            count = 0
    elif count == 5:                      #when reach 5s
        display.show(Image.SAD)           #Wrong
        sleep(1000)
        num = random.randint(1, 100)      #generate new num
        display.show(str(num))
        count = 0
    elif accelerometer.was_gesture("shake"):    #show score when shake
        break
display.scroll('You got' + str(score) + '!')