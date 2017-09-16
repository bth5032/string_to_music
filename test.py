from mingus.midi import fluidsynth
from mingus.containers.note import Note
from mingus.containers.note_container import NoteContainer
from time import sleep

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--prose", help="Text to play", type=str, default="He was alone and young and wilful and wildhearted")
parser.add_argument("-t", "--tempo", help="Time between notes", type=float, default=0.1)
parser.add_argument("-c", "--chord", help="Play the first N characters", type=int, default=1)

fluidsynth.init("Nice-Keys-B-JNv1.5.sf2")

args=parser.parse_args()

text=args.prose
chord=args.chord

letter_map = {
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
}

tempo=args.tempo

for word in text.split():
  nc = NoteContainer([ letter_map[letter.lower()] for letter in word[:chord] ])
  fluidsynth.play_NoteContainer(nc)
  sleep(tempo)