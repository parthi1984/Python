import os
import pathlib
import platform
import speech_recognition as sr

speech = sr.Recognizer()
directory = pathlib.Path.cwd()


def voice_to_text():
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input


def open_file(filename):
    if platform.system() == "Windows":
        os.system(f"explorer {directory}\\files\\{filename}")
    elif platform.system() == "Darwin":
        os.system(f"open {directory}/files/{filename}")
    else:
        os.system(f"xdg-open {directory}/files/{filename}")


while True:
    print('Python is listening...')
    inp = voice_to_text().lower()
    print(f'You just said: {inp}')

    if inp == 'stop listening':
        print('Goodbye!')
        break
    elif "open pdf" in inp:
        inp = inp.replace('open pdf ', '')
        my_file = f'{inp}.pdf'
        open_file(my_file)
        continue
    elif "open word" in inp:
        inp = inp.replace('open word ', '')
        my_file = f'{inp}.docx'
        open_file(my_file)
        continue
    elif "open excel" in inp:
        inp = inp.replace('open excel ', '')
        my_file = f'{inp}.xlsx'
        open_file(my_file)
        continue
    elif "open powerpoint" in inp:
        inp = inp.replace('open powerpoint ', '')
        my_file = f'{inp}.pptx'
        open_file(my_file)
        continue
    elif "open audio" in inp:
        inp = inp.replace('open audio ', '')
        my_file = f'{inp}.mp3'
        open_file(my_file)
        continue
