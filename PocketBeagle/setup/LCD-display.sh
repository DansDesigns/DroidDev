#!/bin/sh
# From: https://gist.github.com/jadonk/0e4a190fc01dc5723d1f183737af1d83

export FRAMEBUFFER=/dev/fb0

# Display an image
fbi -noverbose -T 1 -a images/borisLCD.jpg
# Cycle between several images
#fbi -t 5 -blend 1000 -noverbose -T 1 -a borisLCD.jpg

# Play a movie
#SDL_VIDEODRIVER=fbcon 
#SDL_FBDEV=/dev/fb0
#mplayer -vf-add rotate=4 -framedrop hst_1.mpg

# Look at the framebuffer settings
fbcon=map:10 fbcon=font:VGA8x8
fbset