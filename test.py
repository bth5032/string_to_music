from mingus.midi import fluidsynth
from mingus.containers.note import Note
from mingus.containers.note_container import NoteContainer
from time import sleep

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--prose", help="Text to play", type=str, default="He was alone and young and wilful and wildhearted")
parser.add_argument("-t", "--tempo", help="Time between notes", type=float, default=0.1)
parser.add_argument("-c", "--chord", help="Play the first N characters", type=int, default=1)
parser.add_argument("-r", "--rhythm", help="Use the length of the word to make a rhythm", action='store_true', default=False)

fluidsynth.init("Nice-Keys-B-JNv1.5.sf2")

args=parser.parse_args()

text=args.prose
chord=args.chord

"""letter_map = {
"a": "A-4", 
"b": "A#-4",
"c": "B-4",
"d": "C-4",
"e": "C#-4",
"f": "D-4",
"g": "D#-4",
"h": "E-4",
"i": "F-4",
"j": "F#-4",
"k": "G-4",
"l": "G#-4",
"m": "A-5",
"n": "A#-5",
"o": "B-5",
"p": "C-5",
"q": "C#-5",
"r": "D-5",
"s": "D#-5",
"t": "E-5",
"u": "F-5",
"v": "F#-5",
"w": "G-5",
"x": "G#-5",
"y": "A-6",
"z": "A#-6",
}"""
letter_map = {
"a": "C-3", 
"b": "D-3",
"c": "E-3",
"d": "F-3",
"e": "G-3",
"f": "A-4",
"g": "B-4",
"h": "C-4",
"i": "D-4",
"j": "E-4",
"k": "F-4",
"l": "G-4",
"m": "A-5",
"n": "B-5",
"o": "C-5",
"p": "D-5",
"q": "E-5",
"r": "F-5",
"s": "G-5",
"t": "A-6",
"u": "B-6",
"v": "C-6",
"w": "D-6",
"x": "E-6",
"y": "F-6",
"z": "G-6",
}
lm = lambda char: letter_map[char.lower()] if char.lower() in letter_map.keys() else "C-5"

tempo=args.tempo

def makePause():
  def pauseWithRhythm(word):
    return sleep(min(tempo*len(word), 0.5))
  def pauseWithoutRhythm(word):
    return sleep(tempo)
  
  if (args.rhythm):
    return pauseWithRhythm
  else:
    return pauseWithoutRhythm
    

#====================Notes For Clay=======================================
# If you want to extend, you should probably do two things...
# First, you can change how long the pause is between notes by multiplying the variable tempo by something like the count of the number of letters in the word
# Second, you can stop notes from playing by using stop_NoteContainer(nc)
# Third, you can look into the Natural Language Toolkit to see if you can find a better way to map words into notes/chords: http://www.nltk.org/
# Have fun!
#=========================================================================

pause = makePause()

for word in text.split():
  nc = NoteContainer( map(lm , word[:chord]) ) #This line you won't understand Clay, but I can explain if you are interested in playing
  fluidsynth.play_NoteContainer(nc)
  pause(word)