import multiprocessing, time

from pygame import mixer
mixer.pre_init(44100, -16, 1, 512)
mixer.init()
sound = mixer.Sound('bass.wav')

#this function plays a sound until the computer breaks down or the thread is terminated
def play_sound(bm):
    while(True):
        sound.play()
        time.sleep(60/bm)

#idk why this is here
if __name__ == "__main__":

    #the quit variable is used so the client can use the metronome multiple times
    hola="continue"
    bm = 100
    
    while (hola!="quit"):
        
        print("Welcome to the met!")
    
        try:
            bm=int(input("Please input the speed of the metronome: "))
        except:
            print("Please type in an int next time")
            bm=100
            
        m2 = multiprocessing.Process(target=play_sound,args=(bm,))

        m2.start()
        
        while (hola!="stop"):
            hola = input("Type stop to stop, or an int to set a new speed: ")
            try:
                hola = int(hola)
                m2.terminate()
                m2 = multiprocessing.Process(target=play_sound,args=(int(hola),))
                m2.start()
            except:
                pass
               
            
        
        m2.terminate()
        hola=input("Do you want to continue or quit, type quit if you want to quit: ")
    
    print()
    print ("Thank you for using our metronome!")
    print()
    print("Credits")
    print("AC -- programming")
    print("NF -- programming")
    print("JF -- programming")