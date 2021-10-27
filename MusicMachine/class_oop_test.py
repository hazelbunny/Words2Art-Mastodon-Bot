from psonic import *
from threading import Thread
import random
import logging

class Player(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return
    def note(self, pitch, **kwargs): #play a single note
        nkwargs={}
        if 'synth' in kwargs.keys():
            use_synth(kwargs['synth'])
        for key, value in kwargs:
            if key != 'synth' and key != 'sleep':
                nkwargs[key] = value
        play(pitch,**nkwargs)
        print([pitch,nkwargs])
        if 'sleep' in kwargs.keys():
            sleep(kwargs['sleep'])
    def scale(self, notes):
        while True:
            play(random.choice(notes), release=0.6)
            sleep(0.5)
player1 = Player()
player2 = Player()
player1.scale(chord(E3, MAJOR7))
player2.note(60)
