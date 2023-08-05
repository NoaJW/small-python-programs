# Qns: https://inventwithpython.com/bigbookpython/project74.html

import pyttsx3

print("Enter the text to speak, or QUIT to quit.")

tts_engine = pyttsx3.init()

while True: 
    text = input("> ")

    if text.upper() == "QUIT": 
        print("Thanks for playing!")
        break
    else: 
        tts_engine.say(text)
        tts_engine.runAndWait()

    # TODO: configure options (e.g. rate, vol) using pyttsx3 
    

