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
import random

####################
# User interaction #
####################

# Ask user for amount of times, length (with 1 being quarter note) and bpm # (default bpm is 120)

numPlaybackTimes = int(input("Please enter the amount of times you would like for the sample to be played: "))

print(numPlaybackTimes, "times.")

noteDurationsList = []

for amount in range(numPlaybackTimes):
    noteDuration = (float(input("Please enter the duration of the notes as a float: ")))   
    noteDurationsList.append(noteDuration)
        
print(noteDurationsList)

bpm = 120.0

# Based on lesson material
# Asks for bpm input, if none use default bpm, if float/int escape while loop, if incorrect keep looping

correctInput = False

while (not correctInput):
    userBPM = (input("Default BPM is 120.0, please enter the bpm to change it or press enter to keep default BPM: "))
    if not userBPM:
        correctInput = True
    else:
        try:
            bpm = float(userBPM)
            correctInput = True
        except:
            print("Incorrect input, please enter a bpm.")

quarterNote = (60.0 / bpm)

print("Bpm: ", bpm, "Quarternote duration: ", quarterNote, "sec")

##################################
# Note time duration calculation #
##################################

# Enumerates through note length list of user and transforms to length appropriate to bpm of user #

timeDurations = []

for i in range(len(noteDurationsList)):
    timeDurations.append(quarterNote * noteDurationsList[i])

print('timedurations: ', timeDurations) 

###################################################
# Converting list of time durations to timestamps #
###################################################

# timeDurations where 1.0 is a quarter note will be transformed to timeStamp16thList where 1 will be a sixteenth note #

ts16thList = []

def timeDurationsToTS16th(timeDurationList):
    amount = 0
    ts16thList.append(amount)
    for i in range(len(timeDurationList)-1):
        amount = int(amount) + int(timeDurationList[i] * 4)
        ts16thList.append(amount)

timeDurationsToTS16th(timeDurations)

print('ts16list: ', ts16thList)

# timeStamp16thList will be transformed to timestamps in unix time #

unixTs = []

def ts16thListToUnix(bpm, ts16thList):
    value16th = 15 / bpm
    for timestamp in ts16thList:
        unixTs.append(value16th * timestamp)

ts16thListToUnix(bpm, ts16thList)

print('unixts: ', unixTs)

###################
# Sample location #
###################

waveObj = sa.WaveObject.from_wave_file("../assets/kick.wav")

####################################
# Play amount of samples in rhythm #
####################################

for i in timeDurations:
    waveObj.play()
    time.sleep(i)