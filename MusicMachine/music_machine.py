from psonic import *
from threading import Thread

tick = Message()

bpm = 140

@in_thread
def psn(self, pitch, **kwargs): #play a single note
    nkwargs={}
    if 'synth' in kwargs.keys():
        use_synth(kwargs['synth'])
    for key, value in kwargs:
        if key != 'synth' and key != 'sleep':
            nkwargs[key] = value
    play(pitch,**nkwargs)
    if 'sleep' in kwargs.keys():
        sleep(kwargs['sleep'])
    

#psn(60)
#psn(60, synth=PROPHET, sleep=12)
#psn(60,synth=PROPHET)
        

@in_thread
def bass_sound():
    while True:
        print(4)
        #tick.sync()
        use_synth(PROPHET)
        play(C5)
        sleep(0.5)
        play(D5)
        sleep(0.5)
        play(G5)
        sleep(0.5)
        play(G5)
        sleep(0.5)
        
@in_thread
def snare_sound():
    while True:
        print(1)
        sample(ELEC_SNARE)
        sleep(0.5)

@in_thread
def main_sound():
    while True:
        print(5)
        #tick.cue()
        play(C5)
        sleep(0.5)
        play(D5)
        sleep(0.5)
        play(G5)
        sleep(0.5)
        play(C5)
        sleep(0.5)
        play(D5)
        sleep(0.5)


bass_sound()
main_sound()
snare_sound()

while True:
    pass