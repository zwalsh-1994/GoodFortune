# Magic 8 Ball v3
# Author: Zachary Walsh
# Last edited September 25, 2022
# v3 includes colorama support, may require installation at beginning of program

import random
from colorama import init
init()
from colorama import Fore
# Magic 8 Ball Responses Below
    # AFFIRMATIVE responses are GREEN text
    # NON-COMMITTAL responses are YELLOW text
    # NEGATIVE responses are RED text
    # Dialogue is MAGENTA if present
responses = [Fore.GREEN + "It is certain.\n" + Fore.RESET, Fore.GREEN + "It is decidedly so.\n" + Fore.RESET, Fore.GREEN + "Without a doubt.\n" + Fore.RESET, \
             Fore.GREEN + "Yes, definitely.\n" + Fore.RESET, Fore.GREEN + "You may rely on it.\n" + Fore.RESET, Fore.GREEN + "As I see it, yes.\n" + Fore.RESET, \
             Fore.GREEN + "Most likely.\n" + Fore.RESET, Fore.GREEN + "Outlook good.\n" + Fore.RESET, Fore.GREEN + "Yes.\n" + Fore.RESET, \
             Fore.GREEN + "Signs point to yes.\n" + Fore.RESET, Fore.YELLOW + "Reply hazy, try again.\n" + Fore.RESET, Fore.YELLOW + "Ask again later.\n" + Fore.RESET, \
             Fore.YELLOW + "Better to not tell you now.\n" + Fore.RESET, Fore.YELLOW + "Cannot predict now.\n" + Fore.RESET, Fore.YELLOW + "Concentrate and ask again.\n" + Fore.RESET, \
             Fore.RED + "Don't count on it.\n" + Fore.RESET, Fore.RED + "My reply is no.\n" + Fore.RESET, Fore.RED + "My sources say no.\n" + Fore.RESET, \
             Fore.RED + "Outlook not so good.\n" + Fore.RESET, Fore.RED + "Very doubtful.\n" + Fore.RESET]
while True:
    main = input("Press ENTER to hear my response to your question. Any input will end the program: \n") # the break makes the output neater
    if main == "":
        reply = random.choice(responses)
        print(reply)
    else:
        print(Fore.MAGENTA + "Goodbye for now." + Fore.RESET)
        break