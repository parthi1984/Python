from io import BytesIO

import requests
import bs4
from pygame import mixer

from mptpkg import voice_to_text, print_say


def news_brief():
    # Locate the website for the NPR news brief
    url = 'https://www.npr.org/podcasts/500005/npr-news-now'
    # Convert the source code to a soup string
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # Locate the tag that contains the mp3 file
    casts = soup.findAll('a', {'class': 'audio-module-listen'})
    # Obtain the web link for the mp3 file
    cast = casts[0]['href']
    # Remove the unwanted components in the link
    mp3 = cast.find("?")
    my_mp3 = cast[0:mp3]
    # Play the mp3 using the pygame module
    my_mp3 = requests.get(my_mp3)
    voice = BytesIO()
    voice.write(my_mp3.content)
    voice.seek(0)
    mixer.init()
    mixer.music.load(voice)
    mixer.music.play()


while True:
    print_say('Python is listening...')
    inp = voice_to_text()
    if inp == 'stop listening':
        print_say('Goodbye!')
        break
    # If "news" in your voice command, play news brief
    elif "news" in inp:
        news_brief()
        while True:
            background = voice_to_text().lower()
            if "stop playing" in background:
                mixer.music.stop()
                break
        continue
