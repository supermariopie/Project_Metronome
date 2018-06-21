import time, sys
from pygame import mixer
import multiprocessing
from timeit import default_timer as timer
mixer.pre_init(44100, -16, 1, 512)
mixer.init()
sound = mixer.Sound('bass.wav')




def calc_square(numbers):
    pass
    # #sound.play()
    # for i in range(8):
        # start = timer()
        # while True:
            # end = timer()
            # if end-start>.5:
                # sound.play()
                # break
def calc_cube(numbers):
    while True:
        sound.play()
        time.sleep(1)
    
if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    
    p2.start()
    #end = time.time()
    p1.join()
    p2.join()
print('end2')
print("Done!")
