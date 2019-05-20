import os
from random import choice
from time import sleep
from sofia_functions import linkOpener

def responder(text, say, clearer):
    '''Analyze the passed text, do a response or an action with the preferred voice'''

    s_text = text.lower()  # To small letters in order to reduce the if-else(s)

    inputOutputData = [  # Useable and compare-able data. (NOTE:[n][0] ignored)
    [[0], "hello", "hi", "hey"],
    [[1], "How may I help you?", "How can I help you", "What's up?"],
    [[2], "what is your name", "what's your name"],
    [[3], "open the browser", "open browser", "start the browser"],
    [[4], "facebook", "youtube", "google", "gmail", "yahoo", "github"]
    ]

    # Check if user greeted me with a keyword I might understand
    if any(i in s_text for i in inputOutputData[0][1:]):
        # Greet randomly
        say(f"{choice(inputOutputData[0][1:]).title()}. {choice(inputOutputData[1][1:])}")

    elif "who are you" in s_text:
        say("I am Sofia.")

    elif s_text in inputOutputData[2][1:]:
        say("My name is Sofia.")

    # End session if said Exit or Quit
    elif s_text in ["exit", "quit"]:
        say("Ok. Have a nice day")
        raise SystemExit

    # Open the default web browser
    elif s_text in inputOutputData[3][1:]:
        say("Done.")
        os.system(f"{linkOpener()} 'http://'")
        sleep(3)  # Wait till it finishes writing on the CLI
        clearer()  # Then clear

        print("Listening...\n--->The default web browser launched.")

    # Open <A_WEBSITE_EXIST_IN_THE_LIST>
    elif ("open" in s_text or "search for" in s_text) and (s_text.split(" ")[-1] in inputOutputData[4][1:]):
        whichSite = s_text.split(" ")[-1]
        say(f"Sure. Opening {whichSite}.")
        os.system(f'{linkOpener()} https://www.{whichSite}.com')
        sleep(3)
        clearer()
        print(f"Listening...\n--->Opening {whichSite}.")

    else:
        print("\nYou:", text)
