from microbit import *

#DISPLAY ON MICROBIT
while True:
    #get temperature and compass info
    temp = temperature()
    comp = compass.heading()
    #dispplay on microbit
    display.scroll(str(temp)+"C")
    display.scroll("Heading %s" % str(comp))
    with open('tempandcomp.csv', 'w') as new_file:
        new_file.write(str(temp)+','+ str(comp))
    #stay for 5s
    sleep(5000)