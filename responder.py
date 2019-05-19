import os
from random import choice

def responder(text, say, clearer):
    '''Analyze the passed text, do a response or an action with the preferred voice'''


    s_text = text.lower()  # Convert all of the words to small to reduce if-else(s)
    greeting = [
    ["hello", "hi", "hey"],
    ["How may I help you?", "How can I help you", "What's up?"],
    ]


    if s_text in greeting[0]:
        say(f"{choice(greeting[0]).title()}. {choice(greeting[1])}")
    elif "who are you" in s_text:
        say("I am Sofia.")
    elif "what is your name" in s_text or "what's your name" in s_text:
        say("My name is Sofia.")
    elif "exit" or "quit" in s_text:
        raise SystemExit
    else:
        print("\nYou:", text)
