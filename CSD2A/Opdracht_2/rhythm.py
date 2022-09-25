###############################
##                           ##
## Friso's Rhythmic Playback ##
##                           ##
###############################

#######################
# Importing libraries #
#######################

import simpleaudio as sa
import time

####################
# User interaction #
####################

# Ask user for amount of times, length (with 1 being quarter note) and bpm #

numPlaybackTimes = int(input("Please enter the amount of times you would like for the sample to be played: "))

print(numPlaybackTimes, "times.")

noteDurationsList = []

for amount in range(numPlaybackTimes):
    noteDuration = (float(input("Please enter the duration of the notes as a float: ")))   
    noteDurationsList.append(noteDuration)
        
print(noteDurationsList)

bpm = float(input("Please enter the bpm as a float: "))
quarterNote = (60.0 / bpm)

print("Bpm: ", bpm, "Quarternote duration: ", quarterNote, "sec")

##################################
# Note time duration calculation #
##################################

# Enumerates through note length list of user and transforms to length appropriate to bpm of user #

timeDurations = []

for i in range(len(noteDurationsList)):
    timeDurations.append(quarterNote * noteDurationsList[i])

print(timeDurations) 

###################
# Sample location #
###################

wave_obj = sa.WaveObject.from_wave_file("../assets/kick.wav")

####################################
# Play amount of samples in rhythm #
####################################

for i in timeDurations:
    wave_obj.play()
    time.sleep(i)