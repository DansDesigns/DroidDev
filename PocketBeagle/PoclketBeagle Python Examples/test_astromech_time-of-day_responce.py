#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ttastromech import TTAstromech
import datetime

say = []

r2 = TTAstromech()

while True:
    hour = datetime.datetime.now().hour
    if (hour >= 0) and (hour < 12):
        r2.speak("abg")
    elif (hour >= 12) and (hour < 18):
        r2.speak("tfs")
    elif (hour >= 18) and (hour < 24):
        r2.speak("qaef")

# ~~~~~~~~~~~~~~ EOF ~~~~~~~~~~~~~
