# forty-servants-alpha - a sandbox
# Author: Zachary Walsh
# Last edited November 25, 2022
# A divination game based off of the 40 Servants Oracle Deck, designed by Tommie Kelly.

import random
from breezypythongui import EasyFrame

#servantsList = ["The Adventurer", "The Balancer", "The Carnal", "The Chaste", "The Conductor", "The Contemplator", "The Dancer", "The Dead", "The Depleted", "The Desperate", \
#                "The Devil", "The Explorer", "The Eye", "The Father", "The Fixer", "The Fortunate", "The Gate Keeper", "The Giver", "The Guru", "The Healer", \
#                "The Idea", "The Levitator", "The Librarian", "The Lovers", "The Master", "The Media", "The Messenger", "The Monk", "The Moon", "The Mother", \
#                "The Opposer", "The Planet", "The Protector", "The Protester", "The Road Opener", "The Saint", "The Seer", "The Sun", "The Thinker", "The Witch"]

# test functions
def print_pass(test_name):
    print(test_name, "pass ✔️\n")
def print_fail(test_name):
    print(test_name, "fail ❌\n")

class Servant:
    instances = []
    def __init__(self, name, meaning):
        self.name = name
        self.meaning = meaning
        __class__.instances.append(self)

# Servant metadata for fortune generation
serv1  = Servant("The Adventurer", "Adventure and Journeying")
serv2  = Servant("The Balancer", "Balance and Equity")
serv3  = Servant("The Carnal", "Attraction and Dating")
serv4  = Servant("The Chaste", "Moderation and Chastity")
serv5  = Servant("The Conductor", "Planning and Orchestration")
serv6  = Servant("The Contemplator", "Unconscious Insight and Meditation")
serv7  = Servant("The Dancer", "Celebration and Gratitude")
serv8  = Servant("The Dead", "The End of a Cycle")
serv9  = Servant("The Depleted", "Loss and Depletion")
serv10 = Servant("The Desperate", "Pain and Desperation")
serv11 = Servant("The Devil", "Personal Limitations")
serv12 = Servant("The Explorer", "Discovery and Exploration")
Serv13 = Servant("The Eye", "The Grand Plan and Awareness")
Serv14 = Servant("The Father", "Tough Love and Guidance")
Serv15 = Servant("The Fixer", "Solving a Problem at Any Cost")
Serv16 = Servant("The Fortunate", "Bounty and Good Luck")
Serv17 = Servant("The Gatekeeper", "Delay and Blocked Entry")
Serv18 = Servant("The Giver", "Charity and Gifts")
Serv19 = Servant("The Guru", "Self-Mastery and Success")
Serv20 = Servant("The Healer", "Health and Restoration")
Serv21 = Servant("The Idea", "New Ideas and Concepts")
Serv22 = Servant("The Levitator", "Top-Down Perspective and Insight")
Serv23 = Servant("The Librarian", "Knowledge and Information")
Serv24 = Servant("The Lovers", "Attachment and Commitment")
Serv25 = Servant("The Master", "The Highest Self Possible")
Serv26 = Servant("The Media", "Propaganda and Advertisement")
Serv27 = Servant("The Messenger", "Communication and Reception")
Serv28 = Servant("The Monk", "Simplicity and Decluttering")
Serv29 = Servant("The Moon", "Illusions and Lies")
Serv30 = Servant("The Mother", "Nurturing and Fertility")
Serv31 = Servant("The Opposer", "Opposition and Resistance")
Serv32 = Servant("The Planet", "The Beauty of Creation")
Serv33 = Servant("The Protector", "Safety and Security")
Serv34 = Servant("The Protester", "Fighting for What's Right")
Serv35 = Servant("The Road Opener", "Opportunities and Open Doors")
Serv36 = Servant("The Saint", "Experts and Outside Assistance")
Serv37 = Servant("The Seer", "Instinct and Intuition")
Serv38 = Servant("The Sun", "Radiance and Energy")
Serv39 = Servant("The Thinker", "Reasoning and Logic")
Serv40 = Servant("The Witch", "Magic and Mystery")

# Functions
def shuffle():
    randIndex = random.randrange(len(Servant.instances))
    randCard = Servant.instances[randIndex]
    print(f"You drew {randCard.name} which represents {randCard.meaning}.")

# Main loop
while True:
    shuffle()
    choice = input("Hit Enter to draw another Servant. Enter anything else to quit.")
    if choice == "":
        continue
    else:
        break
