######################################
##                                  ##
## Friso's Irregular Beat Generator ##
##                                  ##
######################################

#######################
# Importing libraries #
#######################

from os import times
import simpleaudio as sa
import time
import random

####################
# Sample locations #
####################

samples = [sa.WaveObject.from_wave_file("../assets/kick.wav"),
            sa.WaveObject.from_wave_file("../assets/snare.wav"),
            sa.WaveObject.from_wave_file("../assets/hihat.wav")]

amountOfSamples = len(samples)

allSamples = []

for i in range(amountOfSamples):
    allSamples.append(samples[i])

####################
# User interaction #
####################

# Ask user for amount of time signature, notes, note length (with 1 being quarter note) and bpm # (default bpm is 120)

print("Welcome to the Sample Sequencer!")

# Asks for bpm input, if none use default bpm, if float/int escape while loop, if incorrect keep looping 
# (Based on lesson material)

bpm = 120.0

correctInputBPM = False

while (not correctInputBPM):
    userBPM = input("Default BPM is 120.0, please enter the bpm to change it or press enter to keep default BPM: ")
    if not userBPM:
        correctInputBPM = True
    else:
        try:
            bpm = float(userBPM)
            if(bpm > 0):
                correctInputBPM = True
            else:
                print("Please enter a positive number.")
        except:
            print("Incorrect input, please enter a bpm.")

quarterNote = (60.0 / bpm)

print("Bpm: ", bpm, "Quarternote duration: ", quarterNote, "sec")

# Catches ValueError's of inputs #

# Time signatures; 1 = 5/4, 2 = 7/8
# Default bars amount is 4

barsAmount = 4

while True:
    try:
        barsAmount = int(input("Please enter the amount of bars you would like to generate (standard is 4): "))
        if(barsAmount > 0):
            print("Amount of bars:", barsAmount)
            break
    except ValueError:
        print("Please enter a number.")
    else:
        print("Please enter a positive number.")

# Time signature input

eightNote = 0

def timeSignatureCheck(timeSignature):
    if(timeSignature == 1):
        eightNote = 10 
        return eightNote
    elif(timeSignature == 2):
        eightNote = 7
        return eightNote

while True:
    try:
        timeSignature = int(input("Please enter either 1 (5/4) or 2 (7/8) for the time signature: "))
        if(timeSignature == 1 or timeSignature == 2):
            eightNote = timeSignatureCheck(timeSignature)
            print("Eight note: ", eightNote)
            break
    except ValueError:
        print("Please enter either 1 or 2.")
    else:
        print("Please enter either 1 or 2.")

# Amount of sample plays

while True:
    try:
        numPlaybackTimes = int(input("Please enter the amount of times you would like for the sample to be played: "))
        if(numPlaybackTimes > 0):
            print(numPlaybackTimes, "times.")
            break
    except ValueError:
        print("Please enter a number.")
    else:
        print("Please enter a positive number.")

# Note length input

noteDurationsList = []

for amount in range(numPlaybackTimes):
    while True:
        try:
            noteDuration = (float(input("Please enter the duration of the notes as a float: ")))
            if(noteDuration > 0):
                noteDurationsList.append(noteDuration)
                break
        except ValueError:
            print("Please enter a float (a whole number will be transformed to a float (1 -> 1.0).")
        else:
            print("Please enter a number greater than 0.")
        
print(noteDurationsList)

##################################
# Note time duration calculation #
##################################

# Enumerates through note length list of user and transforms to length appropriate to bpm of user #

timeDurations = []

for i in range(len(noteDurationsList)):
    timeDurations.append(quarterNote * noteDurationsList[i])

print("timeDurations with", bpm, "bpm: ", timeDurations) 

###################################################
# Converting list of time durations to timestamps #
###################################################

# timeDurations where 1 is a quarter note will be transformed to timeStamp16thList where 1 will be a sixteenth note #

ts16thList = []

def timeDurationsToTS16th(timeDurationList):
    amount = 0
    ts16thList.append(amount)
    for i in range(len(timeDurationList)-1):
        amount = int(amount) + int(timeDurationList[i] * 4)
        ts16thList.append(amount)

timeDurationsToTS16th(timeDurations)

print("ts16list: ", ts16thList)

# timeStamp16thList will be transformed to timestamps in unix time #

unixTS = []

def ts16thListToUnix(bpm, ts16thList):
    value16th = 15 / bpm
    for timestamp in ts16thList:
        unixTS.append(value16th * timestamp)

ts16thListToUnix(bpm, ts16thList)

print("unixTS: ", unixTS)

##########################
# Event Handler Creation #
##########################

eventList = []

def eventHandler(unixTS, allSamples):
    for i in range(len(unixTS)):
        eventList.append(
            {"unixTS": unixTS[i],
            "allSamples": allSamples[random.randint(0, (amountOfSamples -1))]}
        )

eventHandler(unixTS, allSamples)

####################################
# Play amount of samples in rhythm #
####################################

# Give a start unix time #

startTime = time.time()

# Changing variable for each next timestamp in rhythm #

event = eventList.pop(0)

TSCounter = 0

# Sequence playing while loop from lesson #

while True:

  #var for storing the current time

  currentTime = time.time()

  #check if the current time - the start time is bigger or even with the current time stamp from the timeStampsTime list. if so, play the sample

  if(currentTime - startTime >= event["unixTS"]):

    event["allSamples"].play()

    # if there are timestamps left in the timestamps list

    if(eventList):

      #if the list timeStampsTime still isn't empty, fill the timestamp var with the first float from the list

      event = eventList.pop(0)

    else:

      #if the list is empty break the loops
       
      break
    
  else:

    # short wait to prevent we'll keep the processor busy when there's nothing to do

    time.sleep(0.001)

# let the last 'note' ring out

time.sleep(1)
    