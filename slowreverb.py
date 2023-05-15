from pyo import *
import time
import os

home = os.path.expanduser('~')
SONG_PATH = SNDS_PATH+'\\Songs'

originalFile = input("What is the song name? ")
originalFile = SONG_PATH+'\\'+originalFile+'.flac'


s = Server(audio='offline').boot()
t = SndTable(originalFile)
pitchAdj = .82
#########STRev implementation
sf = Looper(t, pitch=pitchAdj, dur=t.getDur()*2, xfade=0, mul=0.5)
#sf.ctrl()
rev = STRev(sf, inpos=0.5, revtime=1.5, cutoff=5000, bal=.4, roomSize=1).out()

length = t.getDur()/pitchAdj
s.recordOptions(
    dur=length,  # give some room for the reverb trail! This is what decides the files length
    filename=originalFile.replace(".flac","SlowedReverbed.wav"),
    fileformat="WAV",
)

s.start()

s.shutdown()
