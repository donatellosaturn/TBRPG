import time
import sys
import os
class bcolors:
    BLACK = '\033[38;5;238m'
    BLUE = '\033[38;5;21m'
    BROWN = '\033[38;5;94m'
    CYAN = '\033[38;5;51m'
    GREEN = '\033[38;5;46m'
    ORANGE = '\033[38;5;214m'
    PURPLE = '\033[38;5;92m'
    PINK = '\033[38;5;201m'
    RED = '\033[38;5;196m'
    TEAL = '\033[38;5;30m'
    WHITE = '\033[38;5;231m'
    YELLOW = '\033[38;5;226m'
    MAGENTA = '\033[38;5;197m'

def characterDialogue(NAME, CLASS, TEXT, SPEED=.02, REST=1):
    #PRINTING MESSAGE
    if CLASS == "BLACK":
        print(f"{bcolors.BLACK} {NAME}:", end='')
    elif CLASS == "BLUE":
        print(f"{bcolors.BLUE} {NAME}:", end='')
    elif CLASS == "BROWN":
        print(f"{bcolors.BROWN} {NAME}:", end='')
    elif CLASS == "CYAN":
        print(f"{bcolors.CYAN} {NAME}:", end='')
    elif CLASS == "GREEN":
        print(f"{bcolors.GREEN} {NAME}:", end='')
    elif CLASS == "ORANGE":
        print(f"{bcolors.ORANGE} {NAME}:", end='')
    elif CLASS == "PURPLE":
        print(f"{bcolors.PURPLE} {NAME}:", end='')
    elif CLASS == "PINK":
        print(f"{bcolors.PINK} {NAME}:", end='')
    elif CLASS == "RED":
        print(f"{bcolors.RED} {NAME}:", end='')
    elif CLASS == "TEAL":
        print(f"{bcolors.TEAL} {NAME}:", end='')
    elif CLASS == "WHITE":
        print(f"{bcolors.WHITE} {NAME}:", end='')
    elif CLASS == "YELLOW":
        print(f"{bcolors.YELLOW} {NAME}:", end='')
    elif CLASS == "MAGENTA":
        print(f"{bcolors.MAGENTA} {NAME}:", end='')
    print(' ', end='')

    for CHAR in TEXT:
        sys.stdout.write(f'{bcolors.WHITE}' + CHAR)
        sys.stdout.flush()
        time.sleep(SPEED)

    time.sleep(REST)

    print("\n")

def reference():
    characterDialogue("ZACHARY", "BLUE", "This is a test message")
    characterDialogue("BRYNNE", "BROWN", "This is a test message")
    characterDialogue("MILO", "CYAN", "This is a test message")
    characterDialogue("GARRETT", "GREEN", "This is a test message")
    characterDialogue("AMITY", "ORANGE", "This is a test message")
    characterDialogue("DAKOTA", "PURPLE", "This is a test message")
    characterDialogue("HEATHER", "PINK", "This is a test message")
    characterDialogue("AARON", "RED", "This is a test message")
    characterDialogue("CASEY", "TEAL", "This is a test message")
    characterDialogue("EVEREST", "WHITE", "This is a test message")
    characterDialogue("SOPH", "YELLOW", "This is a test message")
    characterDialogue("[SYSTEM]", "WHITE", "This is a test message")


time.sleep(3)

#[EPISODE LIST]
#----------
#and so it begins.

def Episode(episodeNumber):
    if episodeNumber == 1:
        #EPISODE ONE
        characterDialogue("[SYSTEM]", "WHITE", "[18:09] STARTUP: Audio Systems enabled", 0, 2)
        characterDialogue("???", "BLACK", "...")
        characterDialogue("???", "BLACK", "...I hope this works.", REST=2)
        time.sleep(3)
        characterDialogue("???", "BLACK", "Sending a test message... now.", REST=0)
        characterDialogue("[SYSTEM]", "WHITE", "[18:10] DEBUG: Automated Message sent from (125.52.102.8)", 0, 2)
        characterDialogue("???", "BLACK", "Holy... shit.", REST=2)
        characterDialogue("???", "BLACK", "It actually...")
        characterDialogue("???", "BLACK", "Okay... okay... holy shit.")
        characterDialogue("???", "BLACK", "[AUDIBLE SIGH]")
        characterDialogue("???", "BLACK", "Alright.")
        characterDialogue("???", "BLACK", "Turning on its infrastructure... now.")
        loop = 10
        while loop != 0:
            loop -= 1
            characterDialogue("[SYSTEM]", "YELLOW", "[18:11] WARNING: Unknown Diagnostic Error Occured", 0, 0)
        characterDialogue("[SYSTEM]", "RED", "[18:11] ERROR: Ocular System is damaged. Continue?", 0, 2)
        characterDialogue("???", "BLACK", "...")
        characterDialogue("???", "BLACK", "...Diagnostic Error?")
        characterDialogue("???", "BLACK", "I don't remember programming that in...")
        characterDialogue("???", "BLACK", "...screw it. The ocular system isn't important anyway...")
        characterDialogue("???", "BLACK", "Let me remotely enter in an error bypass...")
        characterDialogue("[SYSTEM]", "YELLOW", "[18:12] WARNING: Error Bypass Used. Certain features may", 0, 0)
        os.system('cls')
        characterDialogue("YOU", "WHITE", "...", 0.02, 1)
        characterDialogue("YOU", "WHITE", "...H-Hello...?", 0.02, 2)
        characterDialogue("???", "BLACK", "[AUDIBLE CELEBRATION]")
        characterDialogue("YOU", "WHITE", "...I'm... uh... where am I...?", 0.02, 1)
        characterDialogue("???", "BLACK", "HELLO, WORLD!")
        characterDialogue("YOU", "WHITE", "...uh... who is worl-", 0.02, 0)
        characterDialogue("???", "BLACK", "That's your name, of course!")
        characterDialogue("YOU", "WHITE", "Where am I...? Who are you...?", 0.02, 1)
        characterDialogue("???", "BLACK", "You're in a network right now. A vast network created by yours truly.")
        characterDialogue("???", "BLACK", "[I'm so smart!]")
        characterDialogue("YOU", "WHITE", "N... Network?-", 0.02, 0)
        characterDialogue("???", "BLACK", "Precisely!")
        characterDialogue("YOU", "WHITE", "...Well, uh... who are you exactly? Why... why can't I see anything-", 0.02, 0)
        characterDialogue("???", "BLACK", "Just... just call me 'Dad'. Well, you can't see anything because you don't have to. You can see... ME... everyone... through text.")

        #CHOICE 1
        print("[a choice appears!]\n[a] - That's kind of... cool...\n[b] - That's... really lazy of you. I wish I could see your face.\n[c] - Why can't I remember anything...?\n[d] - (stay silent)")

        while true:
            choice = input("> ")

            if choice == 'a':
                characterDialogue("YOU", "WHITE", "Sounds cool... I guess.", 0.2)
                characterDialogue("???", "BLACK", "Exactly, You see... you and I... guys like us share the same mind.")

#The only episode available at this point in time
Episode(1)
