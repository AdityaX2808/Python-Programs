import time

def stopwatch():

    #Initialize the timer
    input("Press Enter to start the timer:")
    start_time = time.time()  #start the precise timer

    #Stop the timer
    input("Press Enter to stop timer:")
    end_time = time.time()  #end the precise timer

    #Calculate the time it was on
    lapped_time = end_time - start_time

    print(f"Elapsed time is {lapped_time: .2f} seconds")

if __name__ == "__main__":
    stopwatch()
        