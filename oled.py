import machine #This allows us to talk to the pico
import ssd1306 #This is a package that helps us use the screen

#This is all just initialization code for the oled. If you connected the scl and sda pins differently, you can change the pin numbers
i2c = machine.SoftI2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.invert(False) #If this is set to true, then all of the black pixels turn white and vice versa
oled.fill(0) #This fills the screen with all black pixels to reset it
oled.text('Hello World', 0, 0) #This will display the text at the point 0, 0
oled.text('Hello World 2', 0, 10) #This will display the text just under the other
oled.show() #This actually shows the screen, without this, the screen wouldn't work

#Now, try to combine the button press and the oled screen into one pico
#This should display some kind of text when the button is pressed
