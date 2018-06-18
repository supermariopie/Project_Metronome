import multiprocessing
import sys
import simpleaudio


command = ""
bm = 100
sound_name = ""
should_quit = ""

def play_sound(bm, sound_name, should_stop):
	#plays the sound here!
	while(should_stop != True):
		#play the sound here
		pass
#Here is a non multiprocessing version of the program

"""
bm = input("input speed");
sound_name = input("input sound name");
play_sound(bm,sound_name)
"""

#below is an attempt to implement a multiprocessor

def stop_sound(should_stop):
	stop = input("type s and click ENTER to stop the metronome")
	if (stop == "s"):
		should_stop = True
	
	
while (command != "q"):
	bm = input("input speed");
	sound_name = input("input sound name");
	
	should_stop = multiprocessing.Value('b')
	should_stop = False

	stop_process = multiprocessing.Process(target=stop_sound,args=(should_stop,))
	
	sound_process = multiprocessing.Process(target=play_sound,args=(bm,sound_name))
	
	stop_process.start()
	sound_process.start()
	
	sound_process.join()
	
	#Determine whether the another sound should be played
	
	command = input("Do you want to continue? Type q to quit")
	