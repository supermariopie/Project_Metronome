import threading
import sys
import simpleaudio

command = ""
bm = 100
sound_name = ""

def play_sound(bm, sound_name):
	#plays the sound here!
	
	print("playing a sound!")

bm = input("input speed");
sound_name = input("input sound name");
play_sound(bm,sound_name)

#below is an attempt to implement a multiprocessor
"""
def stop_sound():
	
	pass
	
	
while (command != "q"):
	bm = input("input speed");
	sound_name = input("input sound name");
	
	signal = threading.Event();
	signal.clear();
	
	sound_thread = threading.Thread(target=play_sound,args=(bm,sound_name))
	stop_thread = threading.Thread(target=stop_sound)
	
"""