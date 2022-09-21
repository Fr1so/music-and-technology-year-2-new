###############################
## Friso's Rhythmic Playback ##
###############################

# Importing libraries

import simpleaudio as sa
import time

# Sample location

wave_obj = sa.WaveObject.from_wave_file("../../assets/kick.wav")

# Define sample playing function

def playSample(amount):
    for x in range(amount):
        play_obj = wave_obj.play()
        play_obj.wait_done()

# User interaction

amountOfTimes = int(input("Please enter the amount of times you would like for the sample to be played: "))
print(amountOfTimes, "times.")

# Run sample playing function

playSample(amountOfTimes)
