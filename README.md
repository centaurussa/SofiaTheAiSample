A ready sample of **`SofiaTheAI`** that can be used to understand the inputted voice and act and respond upon it.

*NOTE: Refer to responder.py to add more if-else statements to increase the control and functionality of Sofia to fit your needs*

# How to launch the sample
**`cd`** to the sample's root directory and write in the Command Line Interface(a.k.a Terminal) the following line:-

**`python sofia.py`**

# Handling common errors
If you didn't install Pyaudio and portaudio from the included `.yml` file, then you might run into some problems. Some Linux users might face problems with SpeechRecognition library for not detecting their input mic devices, this problem can be solved by downloading the follow two libraries:
- Pyaudio
- Portaudio

> If that didn't help and another error occurred, then it means you downloaded the buggy ones. You can try **`Conda`** to install the bug-free ones from the mentioned channel [here](https://github.com/ContinuumIO/anaconda-issues/issues/4139#issuecomment-433710003).

# Changing voice settings
In order to change the outputted voice you can do the following:-
1. Open sofia.py with a text editor
2. Lookup the **responder()** function
3. The second parameter can be:-
    - "**sf.say1**" for a slow human-like voice. (Internet speed makes a difference)
    - "**sf.say2**" for a fast robotic voice.

*NOTE: For extra voice control view **sofia_functions.say1()** or **sofia_functions.say2()***
# Dependencies
- Pyaudio
- gTTS
- SpeechRecognition
- Pyttsx3
- Pygame


# Basic voice inputs
`Voice input: Hello Sofia / Hi Sofia / Hello / Hi / Hey`

Voice output: Some response...

`Voice input: What's your name? / Who are you?`

Voice output: Some response...

`Voice input: Open the browser`

Voice output: Some response...

`Voice input: Open Facebook / YouTube / Google / GitHub`

Voice output: Some response...
