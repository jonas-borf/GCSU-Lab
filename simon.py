from machine import ADC
from time import sleep
from picozero import PWMLED, Speaker, Button
from random import random
blue_button = Button(16)
green_button = Button(17)
yellow_button = Button(0)
white_button = Button(11)
blue = PWMLED(13)
green = PWMLED(12)
yellow = PWMLED(9)
white = PWMLED(8)
speaker = Speaker(22)
sequence = []
sleep_time = 1
player = []
sound = False
num = random()
if num > .5:
    sound = True
    
BEAT = .25

song = [ ['d5', BEAT / 2], ['d#5', BEAT / 2], ['f5', BEAT], ['d6', BEAT], ['a#5', BEAT], ['d5', BEAT],  
              ['f5', BEAT], ['d#5', BEAT], ['d#5', BEAT], ['c5', BEAT / 2],['d5', BEAT / 2], ['d#5', BEAT], 
              ['c6', BEAT], ['a5', BEAT], ['d5', BEAT], ['g5', BEAT], ['f5', BEAT], ['f5', BEAT], ['d5', BEAT / 2],
              ['d#5', BEAT / 2], ['f5', BEAT], ['g5', BEAT], ['a5', BEAT], ['a#5', BEAT], ['a5', BEAT], ['g5', BEAT],
              ['g5', BEAT], ['', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT / 2], ['d6', BEAT / 2], ['c6', BEAT / 2],
              ['a#5', BEAT / 2], ['a5', BEAT / 2], ['g5', BEAT / 2], ['a5', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT],
              ['f5', BEAT], ['f5', BEAT], ['f5', BEAT / 2], ['d#5', BEAT / 2], ['d5', BEAT], ['f5', BEAT], ['d6', BEAT],
              ['d6', BEAT / 2], ['c6', BEAT / 2], ['b5', BEAT], ['g5', BEAT], ['g5', BEAT], ['c6', BEAT / 2],
              ['a#5', BEAT / 2], ['a5', BEAT], ['f5', BEAT], ['d6', BEAT], ['a5', BEAT], ['a#5', BEAT * 1.5]]
if sound == True:
    for note in song:
        speaker.play(note)
else:
    sleep(2)
def buttonHandlerBlue():
    player.append(1)
    sleep(.05)
    print(player)
def buttonHandlerGreen():
    player.append(2)
    sleep(.05)
def buttonHandlerYellow():
    player.append(3)
    sleep(.05)
def buttonHandlerWhite():
    player.append(4)
    sleep(.05)
blue_button.when_pressed = buttonHandlerBlue
green_button.when_pressed = buttonHandlerGreen
white_button.when_pressed = buttonHandlerWhite
yellow_button.when_pressed = buttonHandlerYellow

def lightShow():
    blue.on()
    sleep(.05)
    blue.off()
    green.on()
    sleep(.05)
    green.off()
    white.on()
    sleep(.05)
    white.off()
    yellow.on()
    sleep(.05)
    yellow.off()
    sleep(.05)
    for i in range(5):
        blue.on()
        white.on()
        green.on()
        yellow.on()
        sleep(.1)
        blue.off()
        white.off()
        green.off()
        yellow.off()
        sleep(.1)

lightShow()
sleep(2)
def playLosingSound():
    speaker.play('g4', 0.5)
    speaker.play('e4', 0.5)
    speaker.play('d4', 0.5)
    speaker.play('c4', 0.5)
    sleep(.5)
    speaker.play('c4', 0.5)
def playWinningSound():
    speaker.play('c4', 0.15)
    speaker.play('e4', 0.15)
    sleep(.2)
    speaker.play('c4', 0.15)
    speaker.play('e4', 0.15)
    sleep(.2)
    speaker.play('g4', 0.2)
    

def ReadPotentiometer():
    adcpin = 27
    pot = ADC(adcpin)
    
    adc_value = pot.read_u16()
    volt = (3.3/65535)*adc_value
    
    percentPot = ScalePercent(volt)
    
    return percentPot

def ScalePercent(volt):
    percent = (volt/3.3)*100
    return int(percent)



while True:
    for color in sequence:
        br = ReadPotentiometer() / 100
        if color == 1:
            blue.on(br)
            sleep(sleep_time)
            blue.off()
            sleep(.05)
        elif color == 2:
            green.on(br)
            sleep(sleep_time)
            green.off()
            sleep(.05)
        elif color == 3:
            yellow.on(br)
            sleep(sleep_time)
            yellow.off()
            sleep(.05)
        elif color == 4:
            white.on(br)
            sleep(sleep_time)
            white.off()
            sleep(.05)
    while True:
        if len(player) >= len(sequence):
            print('breaking')
            break
    if len(sequence) == 0:
            ran = random()
            if ran < .25:
                sequence.append(1)
            elif ran < .5:
                sequence.append(2)
            elif ran < .75:
                sequence.append(3)
            else:
                sequence.append(4)
            continue
    correct = player == sequence
    if correct:
        print('correct')
        ran = random()
        if sound == True:
            playWinningSound()
        if len(sequence) % 10 == 0:
            lightShow()
        if ran < .25:
            sequence.append(1)
        elif ran < .5:
            sequence.append(2)
        elif ran < .75:
            sequence.append(3)
        else:
            sequence.append(4)
        print(sequence)
        player = []
    else:
        print('incorrect')
        sequence = []
        if sound == True:
            playLosingSound()
        player = []
        
        

def c_note():
    speaker.play('c4', 0.5) # play the middle c for half a second




