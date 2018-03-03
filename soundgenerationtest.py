"""
Testing sound generation wiht pydub, using tkiter for gui
"""
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play
from Tkinter import *

##############################
### Initialize things here ###
##############################

#Generate 1k,2k,3k tones of 3 sec duration
#tone1 = Sine(1000).to_audio_segment(duration=3000)
#tone2 = Sine(2000).to_audio_segment(duration=3000)
#tone3 = Sine(3000).to_audio_segment(duration=3000)

#Append each tone onto other with crossfade
#multitone = tone1.append(tone2, crossfade=2500).append(tone3, crossfade=2500)

# Play final tone
#play(multitone)


def play_sound(val):
    #print val
    #play(Sine(int(val)).to_audio_segment(duration=10))
    play(Sine(int(val)).to_audio_segment(duration=5))
    #play(Sine(int(1000)).to_audio_segment(duration=1000))

root = Tk()
scale = Scale(root, from_=100, to=7000, command=play_sound)
scale.pack()
#w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
#w.pack()

#mainloop()

##############################
########## Main loop #########
##############################

#while 1:
    #root.show_values()
    #root.update()
#    root.mainloop()
root.mainloop()