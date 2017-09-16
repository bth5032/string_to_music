#!/usr/bin/bash 

#Setup Script, does everything in the README

#Install Brew if it's not there
which -s brew
if [[ $? != 0 ]] ; then
    # Install Homebrew
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

brew install wget
brew install fluid-synth


sudo easy_install pip

#You might want to run in a virtualenv if installing mingus gives an error as it was for me
#pip install virtual_env

pip install mingus

wget http://www.bobak.io/Nice-Keys-B-JNv1.5.sf2

echo "You should be able to run:"
echo "python test.py --help"
echo "now to see how to run the program, have fun..."
