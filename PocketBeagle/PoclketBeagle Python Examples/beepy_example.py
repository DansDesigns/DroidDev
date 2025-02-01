# pip3 install beepy
#
# beepy relies on a Python package called simpleaudio which can be also be installed using:
#    pip install simpleaudio
#
#

import beepy

beep(sound==5) # integer as argument
#beep(sound='coin') # string as argument



#sound argument takes eitheer integers (1-7) or string (from the list below) as argument.

# Following are the mappings for the numbers: 1 : 'coin', 2 : 'robot_error', 3 : 'error',
#                                             4 : 'ping', 5 : 'ready', 6 : 'success', 7 : 'wilhelm'