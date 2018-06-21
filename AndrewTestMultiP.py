import multiprocessing
import time
import simpleaudio
    

#this function plays a sound until the computer breaks down or the thread is terminated
def play_sound(bm):
    while(True):
        print ("bye")
        time.sleep(.5)

#idk why this is here
if __name__ == "__main__":

    #the quit variable is used so the client can use the metronome multiple times
    quit="continue"
    bm = 100
    
    while (quit!="quit"):
        
        print("Welcome to the met!")
        hola="go"
        
        bm=int(input("Please input the speed of the metronome"))
        
        m2 = multiprocessing.Process(target=play_sound,args=(bm,))

        m2.start()

        while (hola!="stop"):
            hola = input("input?")
            
            
        
        m2.terminate()
        quit=input("Do you want to continue or quit")
    
    print()
    print ("Thank you for using our metronome!")
    print()
    print("Credits")
    print("AC -- programming")
    print("NF -- programming")
    print("JF -- programming")