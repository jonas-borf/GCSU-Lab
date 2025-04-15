from picozero import LED, Button

red = LED(14) #Set the GP14 pin as the LED
button = Button(15) #Set the GP15 pin as the button
red.off()
def buttonHandler(): #This function will run when the button is pressed
    red.toggle() #This turns the LED on if it is off, and off if it is on

button.when_pressed = buttonHandler #This tells the code what function to run when the button is pressed
    

