import os

from gtts import gTTS  # Google's Text to Speech
import pyttsx3
from platform import system


def clearer():
    '''Clears the CLI'''

    os.system("cls" if os.name == "nt" else "clear")


def cache_clearer():
    '''Removes past session\'s activity'''

    try:
        os.remove("output.mp3")
        os.remove(".google-cookie")
    except OSError:
        pass


# Use Google's Text to Speech, save it as mp3, play it, and then delete it
def say1(lines):
    '''Text parsed to Google\'s Text-to-Speech API
        to return a playable voice'''

    if os.name == "nt":
        tts = gTTS(text=lines, lang='en', slow=False)
        tts.save("output.mp3")

        import pygame.mixer
        from time import sleep
        pygame.mixer.init()
        pygame.mixer.music.load(open(f"{os.getcwd()}/output.mp3", "rb"))
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            sleep(1)

        cache_clearer()

    else:
        import pygame
        gTTS(text=lines, lang='en', slow=False).save("output.mp3")
        pygame.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        clock = pygame.time.Clock()
        clock.tick(10)

        # Don't let the function finish until the entire mp3 is loaded
        # to prevent the program from hearing itself
        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            clock.tick(10)

        cache_clearer()


# Use pyttsx3's offline Text to Speech
def say2(lines):
    '''Text parsed to pyttsx3's offline Text-to-Speech'''

    engine = pyttsx3.init()
    engine.setProperty('volume', 1)

    if os.name != "nt":  # Set the female voice for Linux systems
        engine.setProperty('voice', 'english+f4')
        engine.setProperty('rate', 140)
    else:
        voices = engine.getProperty('voices')  # Set the female voice for Windows systems
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 120)

    engine.say(lines)
    engine.runAndWait()
    clearer()
    print("Listening...")
