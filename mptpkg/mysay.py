import platform

if platform.system() == "Windows":
    import pyttsx3
    try:
        engine = pyttsx3.init()
    except ImportError:
        pass
    except RuntimeError:
        pass
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.2)

    def print_say(txt):
        print(txt)
        engine.say(txt)
        engine.runAndWait()

if platform.system() == 'Darwin' or platform.system() == 'Linux':
    import os
    from pygame import mixer
    from gtts import gTTS

    def print_say(texts):
        print(texts)
        texts = texts.replace('"', '')
        texts = texts.replace("'", "")
        tts = gTTS(texts, lang='en')
        tts.save('test.mp3')
        mixer.init()
        mixer.music.load('test.mp3')
        mixer.music.play()
        # os.system(f'open test.mp3') # Opens mp3 in default player
        # os.system(f'gtts-cli --nocheck "{texts}" -o test.mp3 | open test.mp3') # Not working
