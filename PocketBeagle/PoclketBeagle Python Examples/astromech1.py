from ttastromech import TTAstromech
import time


if __name__ == '__main__':
        r2 = TTAstromech()

        try:
                #r2.run()  # make random astromech sounds by feeding it random strings of letters
                r2.speak("abg")	# hello sound?
                time.sleep(1)
                r2.speak("tt")	# connected sound?
               # time.sleep(1)
               # r2.speak("c")	# warning - ooo
                time.sleep(1)
                r2.speak("xx")	# disconnected sound?
                time.sleep(1)


               # r2.runonce()	# speaks a random phrase once
                #time.sleep(2)
        except KeyboardInterrupt:
                print('bye ...')