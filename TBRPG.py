import time
import sys
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

def characterDialogue(NAME, CLASS, TEXT, SPEED=.02):
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

    time.sleep(1)

    print("\n")

characterDialogue("???", "BLACK", "This is a test message")
characterDialogue("SCOT", "BLUE", "This is a test message")
characterDialogue("BRYNNE", "BROWN", "This is a test message")
characterDialogue("MILO", "CYAN", "This is a test message")
characterDialogue("GARRETT", "GREEN", "This is a test message")
characterDialogue("AMITY", "ORANGE", "This is a test message")
characterDialogue("DAKOTA", "PURPLE", "This is a test message")
characterDialogue("HEATHER", "PINK", "This is a test message")
characterDialogue("JADEN", "RED", "This is a test message")
characterDialogue("CASEY", "TEAL", "This is a test message")
characterDialogue("EVEREST", "WHITE", "This is a test message")
characterDialogue("JAYE", "YELLOW", "This is a test message")
characterDialogue("(you)", "MAGENTA", "This is a test message")

time.sleep(8)
