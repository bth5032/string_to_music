README:

To set this up, you need mingus, fluidsynth, and "SoundFont" library.

You need to open your Terminal program to run this code. Hit Command+Space and type Terminal, then open that up, a little window will pop up.

In the window type 

``bash
mkdir text_to_music
cd text_to_music
open ./
``

That should pop up a little finder window in a new directory you made.

Then on this github page, click on the "Clone or Download" button on the upper right of this list of files and click Download as Zip. Unzip the contents in the new folder you made and go back to the terminal.

It's probably easiest from here to just run

``bash
source setup.sh
``

But just for the sake of documentation, that script will download a few software dependancies for you.

First you need "Homebrew", which will let you download fluid-synth, the software that plays notes for us. That's accomplished by typing

``bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
``

and hitting enter. Then you want to install fluid-synth, this is done by running:

``bash
brew install fluid-synth
``

Then you want to grab a "SoundFont" library. The one I downloaded was from [this page](https://sites.google.com/site/soundfonts4u/), and it's [this file](https://drive.google.com/file/d/0B4_6p-MMrzwLLVZqV0gyTkFlams/view?usp=sharing). To do this automatically, you'll need wget...

``bash 
brew install wget
``

Then you can get the file off my server:

``bash 
wget http://www.bobak.io/Nice-Keys-B-JNv1.5.sf2
``

Finally, you need to install '[mingus](http://bspaans.github.io/python-mingus/index.html)', which is a front end to fluid-synth and has a lot of other features which can help you make this more musically literate instead of just playing notes based on letters.
To do this, you first need 'pip'

``bash
sudo easy_install pip
``

You will have to enter your password there (the letters won't show up on the terminal, but don't worry you are entering characters.)

Once that's done, install mingus

``bash
pip install mingus
``

If an error message pops up here, let me know and I'll show you how to install "virtualenv", which I had to do to get this running, but you might be more lucky.

Otherwise, you are ready to run the program. Just type

``bash
python test.py --help
``

for instructions. Have fun!



