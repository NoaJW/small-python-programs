# Qns: https://inventwithpython.com/bigbookpython/project25.html

import random
import time
import threading

def com_draw(): 
    global com_end_time
    time.sleep(random.uniform(0, 10))   # Com sleeps for a randomly generated time under 10 sec, inclusive
    print("DRAW!")
    com_end_time = time.time()


def user_draw(): 
    input()


print("""
    Time to test your reflexes and see if you are the fastest
    draw in the west!
    When you see "DRAW", you have 0.3 seconds to press Enter.
    But you lose if you press Enter before "DRAW" appears.
    """)

while True:        
    user_total_time = None
    com_total_time = None
    user_end_time = None
    com_end_time = None

    print("Press Enter to begin...")
    input()
    print("It is high noon...")

    t1 = threading.Thread(target=com_draw)
    t2 = threading.Thread(target=user_draw)

    start_time = time.time()

    t1.start()
    t2.start()

    # Only when t2 finish executing, then make judgement (t2 can finish early or later)
    t2.join()
    user_end_time = time.time()
    user_total_time = user_end_time - start_time

    if not com_end_time: 
        print('You drew before "DRAW" appeared! You lose.')
    else:
        com_total_time = com_end_time - start_time
        diff_time = user_total_time - com_total_time
        
        if 0 <= diff_time <= 0.3: 
            print("You took {} seconds to draw.".format(diff_time))
            print("You are the fastest draw in the west! You win!")
        else: 
            print("You took {} seconds to draw. Too slow!".format(diff_time))
        
    print("Enter QUIT to stop, or press Enter to play again.")
    end = input()
    if end.upper() == "QUIT":
        print('Thanks for playing!')
        break



