from mptpkg import voice_to_text, print_say, wakeup, timer, alarm, joke, email


while True:
    # Capture voice command quietly in standby
    wake_up = wakeup()
    # You can wake up the Virtual Personal Assistant (VPA) by saying "Hello Python"
    while wake_up == "Activated":
        print_say("How may I help you?")
        inp = voice_to_text().lower()
        print_say(f"You just said {inp}.")
        if "back" in inp and "stand" in inp:
            print_say("OK, back to standby; let me know if you need help!")
            break
        # Activate the timer
        elif "timer for" in inp and ("hour" in inp or "minute" in inp):
            timer(inp)
            continue
        # Activate the alarm clock
        elif "alarm for" in inp and ("a.m." in inp or "p.m." in inp):
            alarm(inp)
            continue
        # Activate the joke-telling functionality
        elif "joke" in inp and "tell" in inp:
            joke()
            continue
        # Activate the email-sending functionality
        elif "send" in inp and "email" in inp:
            email()
            continue
        else:
            continue

    # End the script by including "stop' in your voice command
    if wake_up == "ToQuit":
        print_say("OK, exit the script; goodbye!")
        break
