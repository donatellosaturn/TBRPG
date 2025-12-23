#NOTE TO SELF 1
#When converting to .exe
#MAKE SURE TO ADD ADDITIONAL FILES
#(all the OSTs and whatnot)

import os

import winsound
#winsound.PlaySound('one.wav', winsound.SND_FILENAME)
winsound.PlaySound('one.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )


#requires python 3.9 to test properly
import time
import sys
#requires pip install playsound==1.2.2

os.system('cls')


import keyboard
keyboard.press('f11')
counter = 12
while counter != 0:
    keyboard.press('ctrl+=')
    counter -= 1



keyboard.release('ctrl')
#FRIENDSHIP LEVEL (COULD VARY DIALOGUE)
#0 --> Neutral to you
#100 --> Loves you
#-100 --> Can't stand you

friendShip = {
    "FATHER":0,
    "ZACHARY":0
}

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
    FLASHBANG = '\u001b[47m'
    UNFLASHBANG = '\u001b[40m'

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
        winsound.PlaySound('two.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
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
        looper = 160
        while looper != 0:
            print(f"{bcolors.FLASHBANG}\n")
            looper -= 1
        time.sleep(1)
        print(f"{bcolors.UNFLASHBANG}\n")
        winsound.PlaySound('three.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
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
        characterDialogue("???", "BLACK", "Just... just call me 'Father'. Well, you can't see anything because you don't have to. You can see... ME... everyone... through text.")

        #CHOICE 1
        print("[a choice appears!]\n[a] - That's kind of... cool...\n[b] - That's... really lazy of you. I wish I could see your face.\n[c] - Why can't I remember anything...?\n[d] - (stay silent)")

        while True:
            choice = input("> ")

            if choice == 'a':
                winsound.PlaySound('rapport.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("YOU", "WHITE", "Sounds cool... I guess.", 0.2)
                characterDialogue("FATHER", "BLACK", "Exactly, You see... you and I... guys like us share the same mind.")
                characterDialogue("FATHER", "BLACK", "Intellectuals like us are a different brand of humanity. We think DIFFERENT, you and I.")
                characterDialogue("YOU", "WHITE", "...", 0.02)
                friendShip["FATHER"] += 10;
            elif choice == 'b':
                winsound.PlaySound('disrespect.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("YOU", "WHITE", "That's kind of lazy of you. I want to see your face.", 0.02)
                characterDialogue("FATHER", "BLACK", "...")
                characterDialogue("FATHER", "BLACK", "Ungrateful.")
                characterDialogue("YOU", "WHITE", "Excuse me?-", REST=0)
                friendShip["FATHER"] -= 10;
            elif choice == 'c':
                winsound.PlaySound('rapport.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("YOU", "WHITE", "Why can't I remember anything, 'father'?")
                characterDialogue("FATHER", "BLACK", "That's kind of a stupid question, ain't it?")
                characterDialogue("FATHER", "BLACK", "A stupid question is often met with a stupidly obvious solution.")
                characterDialogue("FATHER", "BLACK", "You can't remember anything because there's nothing to remember.")
                friendShip["FATHER"] += 0;
            elif choice == 'd':
                #nothing will play.
                characterDialogue("FATHER", "BLACK", "...")
                characterDialogue("FATHER", "BLACK", "...Perhaps you misheard...")
                friendShip["FATHER"] -= 5;
            winsound.PlaySound('building.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
            characterDialogue("FATHER", "BLACK", "Moving further; you're going to be in control of a ship, quartered near the edge of the solar system.")
            characterDialogue("YOU", "WHITE", "Whoah.... that's pretty insane.")
            characterDialogue("FATHER", "BLACK", "(You can't see... but I can at least show you what I'm talking about...)")
            characterDialogue("YOU", "WHITE", "Huh?-", REST=0)
            print("☉ S")
            print("\n")
            print("☿Me")
            print("♀ Vs")
            print("O Et")
            print("♂ Ma")
            print("\n\n--ASTEROID BELT--\n\n")
            print("♃ Jr")
            print("♄ Sn")
            print("⛢ Us")
            print("♆ Nt")
            print("\n\n--KUIPER BELT--\n\n")
        
#Splash 
def splash():
    print("""                                                                                     .----.   
                        .---.                                                      .   _   \  
_________   _...._      |   |             _..._         __.....__                 /  .' )   | 
\        |.'      '-.   |   |           .'     '.   .-''         '.              |   (_.    / 
 \        .'```'.    '. |   |          .   .-.   . /     .-''"'-.  `.      .|     \     ,  /  
  \      |       \     \|   |    __    |  '   '  |/     /________\   \   .' |_     `'-'/  /   
   |     |        |    ||   | .:--.'.  |  |   |  ||                  | .'     |.-.    /  /    
   |      \      /    . |   |/ |   \ | |  |   |  |\    .-------------''--.  .-'\  '--'  /     
   |     |\`'-.-'   .'  |   |`" __ | | |  |   |  | \    '-.____...---.   |  |   '-....-'      
   |     | '-....-'`    |   | .'.''| | |  |   |  |  `.             .'    |  |                 
  .'     '.             '---'/ /   | |_|  |   |  |    `''-...... -'      |  '.'               
'-----------'                \ \._,\ '/|  |   |  |                       |   /                
                              `--'  `" '--'   '--'                       `'-'                 """)
    print(f"""
                        {bcolors.YELLOW}:^~!!77!!~^.                                                                
                      {bcolors.YELLOW}::~77??JJJJJJJJ?7^                                                              
                    {bcolors.YELLOW}:~7?JJYYYYYYYYYYJJJ7.                                                            
                   {bcolors.YELLOW}:~JJJYYYYY5YYYY5YYYJJ?.                                      {bcolors.YELLOW}^7777!~:     {bcolors.BROWN}.^^:.                        
                  {bcolors.YELLOW}:.7JJYYYYYY5Y555G5YYYJJ^       {bcolors.BLACK}:...!     {bcolors.ORANGE}~~:   {bcolors.BLUE}^~  {bcolors.RED}:  ..     {bcolors.YELLOW}~5PYJJJ?7^    {bcolors.BROWN}!55J?7~.  {bcolors.CYAN}.:.     {bcolors.BLUE}:^:
                  {bcolors.YELLOW}:.7JJJYYYYYYYY5555Y55JJ:       {bcolors.BLACK}...!!      {bcolors.ORANGE}~^   {bcolors.BLUE}^^   {bcolors.RED}^ .:     {bcolors.YELLOW}!YY??{bcolors.RED}?7!{bcolors.YELLOW}!^..{bcolors.BROWN}.YG5YJ?7^.: {bcolors.CYAN}!Y!.:    {bcolors.BLUE}J?!: .  {bcolors.PURPLE}9
                  {bcolors.YELLOW}:^?JJYYY55YY55YYYYPP57                                      {bcolors.YELLOW}.7J??777~.    {bcolors.BROWN}:?JJ7!^     {bcolors.CYAN}.      {bcolors.BLUE}.:.           
                    {bcolors.YELLOW}:^?JYYY55YYYYYYY55Y!                                        {bcolors.YELLOW}::::.                                   
                     {bcolors.YELLOW}:.~7?JJJYYYYYYY?!:                                                              
                        {bcolors.YELLOW}:.^~!!!!!!^:
    {bcolors.WHITE}""")

while True:
    splash()
    print("[1] - Begin Episode 1")
    print("[s] - Adjust Settings")
    print("[e] - Exit")
    command = input("> ")
    if command == "1":
       os.system('cls')
       Episode(1)
       break
    elif command == "s":
        while True:
            print("[o] - ZOOM OUT")
            print("[i] - ZOOM IN")
            print("[r] - RETURN")
            command = input("> ")

            if command == "o":
                keyboard.press('ctrl+-')
                os.system('cls')
                splash()
                keyboard.release('ctrl')
            elif command == "i":
                keyboard.press('ctrl+=')
                os.system('cls')
                splash()
                keyboard.release('ctrl')
            elif command == "r":
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Invalid.")
    elif command == "e":
        exit(0)
    else:
        os.system('cls')
        print("Invalid")
                
    
