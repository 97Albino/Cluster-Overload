import multiprocessing as mp
import sys
import os
import time
# from mpi4py import MPI


def worker(num):
    global b1,b2
    for i in 1000000000:
        
        num += 1
        #time.sleep(0.00001)
        print(run)
    

if __name__ == '__main__':
    # q1 = mp.Queue()
    # q2 = mp.Queue()
    # q3 = mp.Queue()
    # lock = mp.Lock()
    event = mp.Event()

    try:
        p1 = mp.Process(target=worker, args=(1,))
        p2 = mp.Process(target=worker, args=(2,))
        p3 = mp.Process(target=worker, args=(3,))
        p4 = mp.Process(target=worker, args=(4,))
        
        p1.daemon = True
        p2.daemon = True
        p3.daemon = True
        p4.daemon = True
        
        p1.start()
        p2.start()
        p3.start()
        p4.start()
       

        p1.join()
        p2.join()
        p3.join()
        p4.join()
        

        event.wait()
        while True:
            pass

    except KeyboardInterrupt:
        event.set()
        # q1.close()
        # q2.close()
        # q3.close()
        # q4.close()
        # q5.close()
        # q6.close()
        # q7.close()
        # q8.close()
        sys.exit(1)
        
event.set()
sys.exit(1)