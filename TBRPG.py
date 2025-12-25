#NOTE TO SELF 1
#When converting to .exe
#MAKE SURE TO ADD ADDITIONAL FILES
#(all the OSTs and whatnot)

import os

import winsound
#winsound.PlaySound('one.wav', winsound.SND_FILENAME)
winsound.PlaySound('music/one.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )


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
    GRAY = '\033[38;5;244m'
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

def asciiArt(art="None"):
    os.system('cls')
    if art == "1":
        print(f"""{bcolors.GRAY}                    
                                                                 X&&&&&&&;.:++      &&&&&&&                                      
                                                               &&&&&&&;:+X      &&&&&&&&&&&                                      
                                                              &&&&&+;+x     &&&&&$&$.&&&&&&                                      
                                                              &&;.;+     &&&&$&&&&&&&&&&&&&                                      
                                                             $&;$:   .&&&&&&&&&&&&&&&&&&&&&                                      
                                                             &&;+ &+&&&&&&$&&&&&&&&&&&&&&&&                                      
                                                             &&;+X&X&&&&&&&&&&&&&&&&&&&&&&&                                      
                                                             &&$ &;X$&&&$& X;X&&&&&&&&&&&&                                      
                                                             &&& &X&&$&&&&&&&&&&&&&&&&&&&&&                                      
                                                             &&& &$$&$&&&&$&&&&&&&&&&&&&&&&                                      
                                                             &$& &&&&&&&$&&&&&&&&&$&$$&&&&&                                      
                                                            X&X& &&&&&&&&&&&&&&&&&$&&$&$&&&                                      
                                                            &&X& &X$&&&&&&&&$&&&&&&&&&&&&&&                                      
                                                            &&$& &&&&&&$&&&&&&&&&X:    &$&&                                      
                                                            &&$$ &&&&&&&&&X:        .;&&$&&                                      
                                                            &&x+ &&&&:       ;&&&&&&&&&&$&&                                      
                                                            &&        :&&&&&&&&&$$$$$X$$$&$                                      
                                                            &:;& $&&&&&&&$X$XX$$$$$$$X$X$&$                                      
                                                           :&&&&&&&$$XXXX$$XX$XX$XX$$XXXX&$                                      
                                                           ;&$XX$$$$$$$$$$$$$$$X$X$$$&&&&&$                                      
                                                           ;&$$$$$$$X$$$$&&&&&&&&&&&&X   ++                                      
                                              .            ;&$$&&&&&&&&&&&X.         x&&&&&                                      
                                               . .         X&&$+:;+;:;         $&&&&&&XxX&+                                      
                           .   .             . .           :X+$$&&&&&&&&&&&&&&&&&$XXXXXxX&+                                      
                                       ....  . ...         &&&$$$$$$X$XXXXXXXXXXXXXXxXXxX&+                                      
                                   .      . .... .         &&&&&&X$$XXXXXXXXXXXXXXXxXXXXX&+                                      
                       .  .. ... . . .. . .   .           .&:::::::XXXXXXXXXXXXXXXXXXXXxX&;                                      
              ....... .:................... ...... ...    :&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+                                                                                            {bcolors.WHITE}""")
    elif art == "2":
        print(f"""{bcolors.ORANGE}                                               
                                                    .                                
                                                     +                               
                                                     -         .                     
                                         -            +   .   +                      
                                           :+         =+  - :+    .                  
                                              ++.   + +*++++*= .=.       .           
                                                :#*=+++###*@*+++  .+++:              
                                               .  :#{bcolors.YELLOW}@@@@@@@@@{bcolors.ORANGE}%%#*+-                  
                                                 ++##{bcolors.YELLOW}@@@@@@@@@{bcolors.ORANGE}%**=--:.               
                                           :+++++*#%{bcolors.YELLOW}@@@@@@@@@@{bcolors.ORANGE}%*+-                   
                                                 =*%%{bcolors.YELLOW}@@@@@@@@@{bcolors.ORANGE}%#*+++:                
                                               ++=-*%##{bcolors.YELLOW}@@@@{bcolors.ORANGE}##***+    -...:           
                                                  ++=+*+***++++  ++                  
                                                ++   +:+++=+-=++   .-                
                                               =    +  -+. --  =-                    
                                             .         :-   -   :-                   
                                                       -- .  .    -                  
                                                      .:                             
                                                       :                             
                                                                    {bcolors.WHITE}""")
        #RESOURCE: Converted PNG to Ascii Art
    elif art == "3":
        print(f"{bcolors.GREEN}" + """              _oo:\bk99M[<$$+b\.
           .$*"MMMMMMMM[:"\Mb\?^" .
       . '`    HMMMMMMMMMMHMMMM+?.  `.
     .        .HMMMMMMMMMMMMMMP"''     .
    .         `MMMMMMMMMMMMMM|         -`.
   -           `&MMMMMMHH##H:             :
  :             ` *MMM}    `|\             |
  
 : `-              ?MMb__#|""`|+v..         \
 
.                    `''*H#b       -        :|
:                         `*\v,#M#b#,        \

:                        .   #MMMMMMMMMb\    -
-                           .HMMMMMMMMMMMMb  :
:                            `MMMMMMMMMMMMH  .
-:  .                         `#MMMMMMMMMP   '
 :                               MMMMMMMH'  :
  -                            ,MMMMMM?'   .
  `:                           HMMMMH"    -
    -.                       .HMM#*     .-
     `.                     .HH*'     .
       `-.                  &R".    .-
           -.               ._   .-
              '-. .__________?..-""" + f"{bcolors.WHITE}")
        #RESOURCE:  https://ascii.co.uk/art/earth
        #for some reason fstring wouldnt work for this one. weird.
    elif art == "4":
        print(f"""{bcolors.BROWN}                                                      ::: 
                                                 ::::::::
                                           ,,,..:::  ::::
                              xxxx^^^    ......     :::: 
                          xxxxxxxx^^^^^^^..      :::::   
                       xxxxxxxxxxxx^^^^^^xx    ::::::    
                       xxxxxxxxxxxxxxxxxxx::llllll:      
                       xxxxxxxxxxxxxxxx:::::llllll       
                       xxxxxxxxxxxx:::::lllllllll        
                       xxxxxxx::::::::llllllllll         
                        xxx::::lllllllllllll:            
                       :::::llllllllllll::::             
                       llllllllllll:::::::xx             
     .......        llllllllllll:::::xxxxxxx             
   ......         llllllllll::::::xxxxxxxx               
  ....        .lllllllllll      xxxxxxxx                 
 ...     ::..llllllll             xxxx                   
 ,,........llllll                                        
,,,,,,..::::

{bcolors.WHITE}""")
        #made by ME! :D
    elif art == "5":
        print(f"""{bcolors.BLUE}      xxxxxxxxx           
   xxxxxxxxxxxxxxx        
 .xxxxxxxxxxxxxxxxxxx     
::xxxxxxxxxxxxxxxxxxxx    
.::xxxxxxxxxxxxxxxxxxx  
...::xxxxxxxxxxxxxxxxxx 
  ..::::xxxxxxxxxxxxxxx
    ....::xxxxxxxxxxxxx
  .  .....:::::xxxxxxxx.
       .  .....::::::::   
              ........    
         .       ..       
                  .       {bcolors.WHITE}""")
        #ALSO MADE BY ME
    else:
        print(" ")


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
    elif CLASS == "GRAY":
        print(f"{bcolors.GRAY} {NAME}:", end='')
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

def wait(firsttime=False):
    if firsttime == True:
        input(f"{bcolors.GRAY}[Press Enter to Continue]")
    else:
        input(f"{bcolors.GRAY}[Press Enter to Continue]")
    print("\n")

def Episode(episodeNumber):
    if episodeNumber == 0:
        #PROLOGUE
        asciiArt("1")
        winsound.PlaySound('music/two.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
        characterDialogue("[SYSTEM]", "WHITE", "[18:09] STARTUP: Audio Systems enabled", 0, 2)
        characterDialogue("???", "BLACK", "...")
        asciiArt("1")
        characterDialogue("???", "BLACK", "...I hope this works.", REST=2)
        time.sleep(3)
        asciiArt("1")
        characterDialogue("???", "BLACK", "Sending a test message... now.", REST=0)
        characterDialogue("[SYSTEM]", "WHITE", "[18:10] DEBUG: Automated Message sent from (125.52.102.8)", 0, 2)
        asciiArt("1")
        characterDialogue("???", "BLACK", "Holy... shit.", REST=2)
        asciiArt("1")
        characterDialogue("???", "BLACK", "It actually...")
        asciiArt("1")
        characterDialogue("???", "BLACK", "Okay... okay... holy shit.")
        asciiArt("1")
        characterDialogue("???", "BLACK", "[AUDIBLE SIGH]")
        asciiArt("1")
        characterDialogue("???", "BLACK", "Alright.")
        asciiArt("1")
        characterDialogue("???", "BLACK", "Turning on its infrastructure... now.")
        loop = 10
        while loop != 0:
            loop -= 1
            characterDialogue("[SYSTEM]", "YELLOW", "[18:11] WARNING: Unknown Diagnostic Error Occured", 0, 0)
        characterDialogue("[SYSTEM]", "RED", "[18:11] ERROR: Ocular System is damaged. Continue?", 0, 2)
        asciiArt("1")
        characterDialogue("???", "BLACK", "...")
        asciiArt("1")
        characterDialogue("???", "BLACK", "...Diagnostic Error?")
        asciiArt("1")
        characterDialogue("???", "BLACK", "I don't remember programming that in...")
        asciiArt("1")
        characterDialogue("???", "BLACK", "...screw it. The camera system isn't important anyway...")
        asciiArt("1")
        characterDialogue("[SYSTEM]", "YELLOW", "[18:12] WARNING: Error Bypass Used. Certain features may", 0, 0)
        os.system('cls')
        winsound.PlaySound('sfx/ENLIGHTENMENT.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
        looper = 1080
        while looper != 0:
            print(f"{bcolors.FLASHBANG}\n")
            print(f"""{bcolors.BLACK}░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████▓▒░        ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓██▓▒░ 
 ░▒▓█████████████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░▒▓██▓▒░ 
     {bcolors.WHITE}""")
            looper -= 1
        time.sleep(1)
        print(f"{bcolors.UNFLASHBANG}\n")
        winsound.PlaySound('music/three.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
        os.system('cls')
        characterDialogue("???", "WHITE", "...", 0.02, 1)
        characterDialogue("???", "WHITE", "...H-Hello...?", 0.02, 2)
        wait(True)
        characterDialogue("???", "BLACK", "[AUDIBLE CELEBRATION]")
        wait()
        characterDialogue("???", "WHITE", "...I'm... uh... where am I...?", 0.02, 1)
        characterDialogue("???", "BLACK", "HELLO, WORLD!")
        wait()
        characterDialogue("???", "WHITE", "...uh... who is worl-", 0.02, 0)
        characterDialogue("???", "BLACK", "That's your name, of course!")
        wait()
        characterDialogue("WORLD", "WHITE", "Where am I...? Who are you...?", 0.02, 1)
        wait()
        characterDialogue("???", "BLACK", "You're in a network right now. A vast network created by yours truly.")
        characterDialogue("???", "BLACK", "[I'm so smart!]")
        wait()
        characterDialogue("WORLD", "WHITE", "N... Network?-", 0.02, 0)
        characterDialogue("???", "BLACK", "Precisely!")
        wait()
        characterDialogue("WORLD", "WHITE", "...Well, uh... who are you exactly? Why... why can't I see anything-", 0.02, 0)
        characterDialogue("???", "BLACK", "Just... just call me 'Father'. As for sight, well, you can't see anything because you don't have to. You can see... ME... everyone... through text.")
        #CHOICE 1
        print("[a choice appears!]\n[a] - That's kind of... cool...\n[b] - That's... really lazy of you. I wish I could see your face.\n[c] - Why can't I remember anything...?\n[d] - (stay silent)")

        while True:
            choice = input("> ")

            if choice == 'a':
                winsound.PlaySound('music/rapport.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("WORLD", "WHITE", "Sounds cool... I guess.", 0.2)
                wait()
                characterDialogue("FATHER", "BLACK", "Exactly, You see... you and I... guys like us share the same mind.")
                wait()
                characterDialogue("FATHER", "BLACK", "Intellectuals like us are a different brand of humanity. We think DIFFERENT, you and I.")
                wait()
                characterDialogue("WORLD", "WHITE", "...", 0.02)
                wait()
                friendShip["FATHER"] += 10;
            elif choice == 'b':
                winsound.PlaySound('ambient/VHS.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("WORLD", "WHITE", "That's kind of lazy of you. I want to see your face.", 0.02)
                wait()
                characterDialogue("FATHER", "BLACK", "...")
                wait()
                characterDialogue("FATHER", "BLACK", "Ungrateful.")
                wait()
                characterDialogue("WORLD", "WHITE", "Excuse me?-", REST=0)
                friendShip["FATHER"] -= 10;
            elif choice == 'c':
                winsound.PlaySound('music/rapport.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("WORLD", "WHITE", "Why can't I remember anything, 'father'?")
                wait()
                characterDialogue("FATHER", "BLACK", "That's kind of a stupid question, ain't it?")
                wait()
                characterDialogue("FATHER", "BLACK", "A stupid question is often met with a stupidly obvious solution.")
                wait()
                characterDialogue("FATHER", "BLACK", "You can't remember anything because there's nothing to remember.")
                wait()
                characterDialogue("WORLD", "WHITE", "Oh... ")
                wait()
                characterDialogue("FATHER", "BLACK", "[AUDIBLE SIGH]")
                wait()
                friendShip["FATHER"] += 0;
            elif choice == 'd':
                #nothing will play.
                characterDialogue("FATHER", "BLACK", "...")
                wait()
                characterDialogue("FATHER", "BLACK", "...Perhaps you misheard...")
                wait()
                friendShip["FATHER"] -= 5;
            winsound.PlaySound('music/building.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
            characterDialogue("FATHER", "BLACK", "Moving further; you're going to be in control of a ship, quartered near the edge of the solar system.")
            wait()
            characterDialogue("WORLD", "WHITE", "Whoah.... that's pretty insane.")
            wait()
            characterDialogue("FATHER", "BLACK", "(You can't see... but I can at least show you what I'm talking about...)")
            wait()
            characterDialogue("WORLD", "WHITE", "Huh?-", REST=0)

            #this next part will contain ambient audio directly sourced from NASA.
            winsound.PlaySound('ambient/SUN.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
            asciiArt("2")
            characterDialogue("FATHER", "BLACK", "...")
            characterDialogue("FATHER", "BLACK", "This is the sun.")
            wait()
            characterDialogue("FATHER", "BLACK", "WE orbit around it nearly 18 miles a second, 365 days a year, for the rest of... well... our lives.")
            wait()
            characterDialogue("WORLD", "WHITE", "It seems pretty important, I think.")
            wait()
            characterDialogue("WORLD", "WHITE", "I especially love the warm colors-", REST=0)
            winsound.PlaySound('ambient/EARTH.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
            asciiArt("3")
            characterDialogue("FATHER", "BLACK", "This... this is Earth. I'm here right now.", 0.02)
            wait()
            characterDialogue("WORLD", "WHITE", "Am I there, on Earth, with you?", 0.05)
            wait()
            characterDialogue("FATHER", "BLACK", "No, you dolt. I already told you- you're on a network. Right now, you're somewhere near... Saturn I'd say.", 0.05)
            wait()
            characterDialogue("WORLD", "WHITE", "...Saturn?", REST=0)
            winsound.PlaySound('ambient/SATURN.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
            asciiArt("4")
            characterDialogue("WORLD", "WHITE", "...I don't like the way it sounds.", REST=2)
            wait()
            characterDialogue("WORLD", "WHITE", "It's really pretty, though-", REST=0)
            wait()
            characterDialogue("FATHER", "BLACK", "Yes, yes, Saturn is a LOVELY planet and all that, but that's not where you'll be stationed.", 0.025)
            wait()
            characterDialogue("FATHER", "BLACK", "Like I said, you'll be stationed somewhere near Neptune, and I mean that.")
            wait()
            winsound.PlaySound('ambient/NEPTUNE.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
            asciiArt("5")
            characterDialogue("WORLD", "WHITE", "Is this Neptune?", REST=2)
            wait()
            characterDialogue("FATHER", "BLACK", "Yes.", 0.25)
            wait()
            characterDialogue("WORLD", "WHITE", "It's...", 0.2)
            break

        #CHOICE 2
        print("[a choice appears!]\n[a] - Beautiful\n[b] - Blue\n[c] - Horrifying\n[d] - Cold")\

        while True:
            choice = input("> ")

            if choice == "a":
                asciiArt("5")
                winsound.PlaySound('music/pureRawBeauty.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("WORLD", "WHITE", "It's ...beautiful.", REST=3)
                wait()
                friendShip["FATHER"] += 10;
                characterDialogue("FATHER", "BLACK", "I'm glad you feel that way, WORLD.")
                wait()
                characterDialogue("FATHER", "BLACK", "My... my grandpa, or as I called him, 'pops', always loved Neptune. I first found out about this love at an astronomy museum.")
                wait()
                asciiArt("5")
                os.system('cls')
                print("(Flashback)\n")
                asciiArt("5")
                characterDialogue("FATHER [young]", "BLACK", "Hey, Grandpa, What's that planet there called?")
                wait()
                characterDialogue("POPS", "GRAY", "That's 'Neptune'.")
                wait()
                characterDialogue("FATHER [young]", "BLACK", "How come I've never heard of it?")
                wait()
                characterDialogue("POPS", "GRAY", "Your school probably won't focus on the stars or space or many abstract things.")
                wait()
                characterDialogue("POPS", "GRAY", "There will come a day where, hopefully, you'll outgrow your school entirely.")
                wait()
                asciiArt("5")
                characterDialogue("POPS", "GRAY", "Neptune is one of the eight planets in our solar system. The very last one.")
                wait()
                characterDialogue("FATHER [young]", "BLACK", "The... last one?")
                wait()
                characterDialogue("POPS", "GRAY", "[CHUCKLE]", 0.005, 0.5)
                wait()
                characterDialogue("POPS", "GRAY", "It's blue, just like our planet, but it's very cold.")
                wait()
                asciiArt("5")
                characterDialogue("POPS", "GRAY", "So, if you ever visit Neptune, be sure to wear a coat.")
                wait()
                asciiArt("5")
                winsound.PlaySound('ambient/VHS.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("FATHER", "BLACK", "I... haven't heard from him in a while.")
                wait()
                characterDialogue("FATHER", "BLACK", "No matter, hopefully, when things change for the better, I'll be able to go there one day.")
                wait()
                characterDialogue("FATHER", "BLACK", "...")
                wait()
                characterDialogue("FATHER", "BLACK", "This is ridiculous. I'm not even speaking to a real... person.", REST=3)
                wait()
                os.system('cls')
                characterDialogue("FATHER", "BLACK", "Thank you for listening to me.")
                wait()
                characterDialogue("FATHER", "BLACK", "Keep the crew safe.")
                wait()
                characterDialogue("FATHER", "BLACK", "There's a ninth planet out there, somewhere beyond Neptune.")
                wait()
                os.system('cls')
                characterDialogue("FATHER", "BLACK", "Bring them to it.")
                wait()
                characterDialogue("FATHER", "BLACK", "I believe in you.")
                wait()
            elif choice == "b":
                asciiArt("5")
                winsound.PlaySound('music/BLUE.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("WORLD", "WHITE", "It's ...blue.", REST=3)
                wait()
                friendShip["FATHER"] += 0;
                characterDialogue("FATHER", "BLACK", "...")
                wait()
                characterDialogue("FATHER", "BLACK", "I'm both happy and disappointed that you said that.")
                wait()
                characterDialogue("FATHER", "BLACK", "People like us think different, you and I. I think I've already said this.")
                wait()
                characterDialogue("FATHER", "BLACK", "But... sometimes I wish I was a kid again, looking up at the stars with my Pops.")
                wait()
                characterDialogue("FATHER", "BLACK", "Seeing the stars for something other than what they actually are.")
                wait()
                asciiArt("5")
                characterDialogue("TV", "NONE", "* NEPTUNE IS THE EIGHTH PLANET FROM THE SUN.")
                wait()
                characterDialogue("TV", "NONE", "* IT'S BLUE IN COLOR. IT'S VERY COLD AND VERY FAR AWAY FROM THE SUN.")
                wait()
                characterDialogue("FATHER (Narrating)", "BLACK", "Many videos on space I used to watch seemed to explain things in a one-dimensional way.")
                wait()
                characterDialogue("FATHER (Narrating)", "BLACK", "They said things that I already knew from my Pops.")
                wait()
                characterDialogue("FATHER (Narrating)", "BLACK", "However, it felt... automated.")
                wait()
                asciiArt("5")
                characterDialogue("TV", "NONE", "* WHAT'S YOUR FAVORITE PLANET?")
                wait()
                characterDialogue("FATHER (Narrating)", "BLACK", "I never answered. I used to go to the TV for answers to my questions. Not for more questions that I needed to answer.")
                wait()
                characterDialogue("FATHER (Narrating)", "BLACK", "But... it was nice.", 0.1)
                wait()
                asciiArt("5")
                characterDialogue("FATHER", "BLACK", "I felt a variety of emotions from looking at Neptune.", REST=3)
                wait()
                characterDialogue("FATHER", "BLACK", "That beautiful violet hue... put me at peace.", REST=3)
                wait()
                characterDialogue("FATHER", "BLACK", "...but I also felt dread.")
                wait()
                characterDialogue("FATHER", "BLACK", "...I feared the unknown.")
                wait()
                characterDialogue("FATHER", "BLACK", "...I fear the unknown.")
                wait()
                characterDialogue("FATHER", "BLACK", "Whatever lies beyond Neptune, I...")
                characterDialogue("FATHER", "BLACK", "No matter how smart I am I'm just not ready for it.")
                wait()
                os.system('cls')
                winsound.PlaySound('ambient/VHS.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("FATHER", "BLACK", "A few weeks ago scientists recorded what appears to be a ninth planet.")
                wait()
                characterDialogue("FATHER", "BLACK", "They sent out a rocket, filled with 11 of the bravest individuals I've ever met.")
                wait()
                characterDialogue("FATHER", "BLACK", "You're their Artificial Intelligence... their guide.")
                wait()
                characterDialogue("FATHER", "BLACK", "Guide them.")
                wait()
                characterDialogue("FATHER", "BLACK", "Be brave, unlike me.")
                wait()
            elif choice == "c":
                winsound.PlaySound('music/HorrifyingForAllTheWrongReasons.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
                characterDialogue("WORLD", "WHITE", "It scares me.")
                wait()
                characterDialogue("FATHER", "BLACK", "...")
                wait()
                asciiArt("5")
                characterDialogue("???", "GRAY", "Patrick! Everything going okay in here?")
                wait()
                characterDialogue("FATHER", "BLACK", "Y-Yeah boss, it's just...")
                wait()
                characterDialogue("FATHER", "BLACK", "What do you think is beyond Neptune?")
                wait()
                characterDialogue("BOSS", "GRAY", "...Space...?")
                wait()
                asciiArt("5")
                characterDialogue("FATHER", "BLACK", "I'm talking about Planet 9.")
                wait()
                characterDialogue("BOSS", "GRAY", "Stop tryin' to scare my sorry ass, Pat. I still doubt that this is a real thing.")
                wait()
                characterDialogue("FATHER", "BLACK", "But the data-")
                wait()
                asciiArt("5")
                characterDialogue("BOSS", "GRAY", "Yeah, okay. I'll believe it when actual human beings tell me to.", REST=0.5)
                characterDialogue("BOSS", "GRAY", "Not a 'computer' like you or that stupid little gizmo-whatsit you got on that darned machine.")
                characterDialogue("BOSS", "GRAY", "[AUDIBLE SOUND OF A CIGAR BEING LIT. SMOKE IS AUDIBLY BEING EXHALED.]")
                wait()
                characterDialogue("FATHER", "BLACK", "It's... [COUGH]... not a gizmo.")
                characterDialogue("FATHER", "BLACK", "It's an Artificial Intellige-", REST=0)
                characterDialogue("BOSS", "GRAY", "I don't PAY you to tell me how the sausage gets made, just give it to me on the bun when its ready.")
                wait()
                asciiArt("5")
                characterDialogue("BOSS", "GRAY", "The government is payin a lot of money for your little techno-magic. It'd better work.")
                wait()
                characterDialogue("WORLD", "WHITE", "...it?")
                wait()
                characterDialogue("BOSS", "GRAY", "Oh, so you talk too?")
                characterDialogue("BOSS", "GRAY", "[AUDIBLE LAUGHTER CAN BE HEARD]")
                wait()
                asciiArt("5")
                characterDialogue("BOSS", "GRAY", "What a freak. Both of you. Just a pair of freaks.")
                wait()
                characterDialogue("BOSS", "GRAY", "Like I said before, this had better work.", REST=2)
                characterDialogue("BOSS", "GRAY", "[AUDIBLE SOUND OF A CIGAR BEING LIT.]", REST=2)
                characterDialogue("FATHER", "BLACK", "[COUGH] Please stop doin' that in my- [COUGH]- face...")
                wait()
                characterDialogue("BOSS", "GRAY", "[MUTTERING NOISES]", REST=2)


 
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

    print("""                                                 
                                            .. ...: :::.:...                   
                                         .. ..... ..:.::. : :::                 
                                       .. ...          :;;::...:.                         
                                      .. ..              :::;::;:+:                    
                                       ..                 ;;::  ...:.                         
                                 .    ...                  ;;:;:                          
                                   .  .           : .      :::;;:..;;;: .  .                   
                                      .          .::;.     ::;:.::::::  ... .:: .              
                                       .;                  +;;;;++;;: $                    
                                         .                X$$$X+.                             
                                                       :$$+                           
                                           .                                   
                                                       .                 """)


while True:
    splash()
    print("EPISODE SELECTION")
    print("[0] - PROLOGUE")
    print("\nADDITIONAL STUFF")
    print("[s] - Adjust Settings")
    print("[e] - Exit")
    command = input("> ")
    if command == "0":
       os.system('cls')
       Episode(0)
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
                
    
