# Qns: https://inventwithpython.com/bigbookpython/project20.html

import random, shutil, sys, time

# Config constants
# For selection of a random number between MIN_STREAM_LENGTH and MAX_STREAM_LENGTH, to specify the length of a stream (col) of 1/0.
# Ideally, the length should not be too long or it take longer for the stream to end and this tends to crowd the screen with 1/0.
MIN_STREAM_LENGTH = 6       # Minimum 1
MAX_STREAM_LENGTH = 14
PAUSE = 0.1                 # Delay before printing next row 
STREAM_CHARS = ['0', '1']  
DENSITY = 0.02              # Range from 0.0 to 1.0 to compare with random.random()
WIDTH = shutil.get_terminal_size()[0]   
# Cannot print to the last column on Windows without a newline being added automatically, so reduce the width by one
WIDTH -= 1

# Validation
if MIN_STREAM_LENGTH > MAX_STREAM_LENGTH:
    print("Error: Min stream length cannot be greater than max stream length. MIN_STREAM_LENGTH <= MAX_STREAM_LENGTH")
    time.sleep(1)
    sys.exit()
if DENSITY < 0 or DENSITY > 1: 
    print("Error: DENSITY must be in range of [0.0, 1.0]")
    time.sleep(1)
    sys.exit()


print('Digital Stream Screensaver')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    columns = [0] * WIDTH       # Create a list of 0 which represents a col e.g. [0, 0, 0, 0...]

    while True:
        for i in range(WIDTH):
            # Plant numbers in the rows randomly (increase DENSITY to increase chances), a number is a random stream length between the range specified by MIN_STREAM_LENGTH and MAX_STREAM_LENGTH
            if columns[i] == 0:    
                if random.random() <= DENSITY:          
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)      

            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')      # For a planted number, choose to display either 1/0
                columns[i] -= 1                                 # Decrement the stream length after each row. Stream disappears after stream length reached 
            else:          
                print(' ', end='')
        
        print()  
        sys.stdout.flush()      # Immediately push any buffer in stdout to terminal/console (unecessary since print() does that already)
        time.sleep(PAUSE)       # Delay to print next row 
except KeyboardInterrupt:
    sys.exit()      
