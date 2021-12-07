from mptpkg import voice_to_text
from mptpkg import print_say


while True:
    print('Python is listening...')
    inp = voice_to_text()
    if inp == 'stop listening':
        print_say(f'you just said {inp}; goodbye!')
        break
    else:
        print_say(f'you just said {inp}')
        continue
