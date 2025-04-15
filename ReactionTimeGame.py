import machine
import ssd1306
from time import sleep, time_ns
import picozero
import random
from datetime import datetime

#You can choose any other combination of I2C pins
i2c = machine.SoftI2C(scl=machine.Pin(5), sda=machine.Pin(4))
sensor = machine.ADC(4)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

red = picozero.LED(14)
blue = picozero.LED(16)
button = picozero.Button(15)
start = 0
first_press = False
count = 0
def handleButton():
    global first_press
    global start
    global count
    print(first_press)
    if first_press == True:
        if (count >= 9):
            blue.off()
            oled.fill(0)
            oled.text('You got:', 0, 0)
            oled.text(str((time_ns() - start) / 1000000000) + ' seconds', 0, 10)
            oled.show()
            count = 0
            first_press = False
            sleep(1)
        else:
            count += 1
            
        
        print(time_ns())
        print()
        
    else:
        red.on()
        blue.off()
        oled.fill(0)
        oled.text('prepare for blue', 0, 0)
        oled.show()
        first_press = True
        wait_time = 10 * random.random()
        sleep(wait_time)
        red.off()
        blue.on()
        print(time_ns()*1000)
        start = time_ns()
        
        print('done sleeping')
        
button.when_pressed = handleButton
