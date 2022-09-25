###############################
## Friso's Rhythmic Playback ##
###############################

#######################
# Importing libraries #
#######################

import simpleaudio as sa
import time

###################
# Sample location #
###################

wave_obj = sa.WaveObject.from_wave_file("../assets/kick.wav")

##################################
# Define sample playing function #
##################################

def playSample(amount):
    for x in range(amount):
        play_obj = wave_obj.play()
        play_obj.wait_done()

####################
# User interaction #
####################

# Ask user for amount of times, length (with 1 being quarter note) and bpm #

numPlaybackTimes = int(input("Please enter the amount of times you would like for the sample to be played: "))

print(numPlaybackTimes, "times.")

noteDurationsList = []

for i in range(numPlaybackTimes):
    noteDuration = (float(input("Please enter the duration of the notes as a float: ")))   
    noteDurationsList.append(noteDuration)
        
print(noteDurationsList)

bpm = float(input("Please enter the bpm: "))
quarterNote = 60.0 / bpm

print("Bpm: ", bpm, "Quarternote duration: ", quarterNote, "sec")



################################
# Run rhythmic playback engine #
################################

playSample(numPlaybackTimes)
