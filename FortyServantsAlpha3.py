# forty-servants-alpha - a sandbox
# Author: Zachary Walsh
# Last edited November 26, 2022
# A divination game based off of the 40 Servants Oracle Deck, designed by Tommie Kelly. Alpha 3 includes more descriptions and a more complex fortune-generation scheme.

import random
import time
import tkinter as tk

class Servant:
    instances = []
    def __init__(self, *args): #name, meaning, question, comment):
        self.name = args
        self.meaning = args
        self.question = args
        self.comment = args
        # Create a list using the attributes from metadata area
        __class__.instances.append(self)

# Servant metadata for fortune generation
serv1  = Servant("The Adventurer", ["adventure", "a journey", "excitement", "new experiences"],
                ["Is there anything exciting coming up that you're looking forward to?"], 
                ["Life is an adventure sometimes, whether or not you want it to be."])
serv2  = Servant("The Balancer", ["symmetry", "equity", "normalcy", "equilibrium"],
                ["Have you considered how your goals affect other areas of your life?"], 
                ["If you don't maintain balance, the universe will forcibly restore it eventually."])
serv3  = Servant("The Carnal", ["attraction", "dating", "creative urges", "romance"],
                ["Do you know that the world wants something that you have to offer?"], 
                ["Sometimes, people are animals. Always, people are part animal."])
serv4  = Servant("The Chaste", ["moderation", "chastity", "temperance", "restraint"],
                ["Is there anything you really want to do that you might be better off not doing?"], 
                ["Sometimes, abstaining is the more effective action to take."])
serv5  = Servant("The Conductor", ["planning", "orchestration", "organization", "taking charge"],
                ["Are you following a plan that you created, or are you drifting?"],
                ["Whether or not you steer the boat, the current moves you."])
serv6  = Servant("The Contemplator", ["the unconscious mind", "meditation", "rumination", "introspection"],
                ["Have you really carefully considered what you want?"], 
                ["Many dishes taste better if they spend a little time on the back burner."])
serv7  = Servant("The Dancer", ["a routine", "gratitude in the face of adversity", "resilience", "hope for the future"],\
                ["Do you recognize the good in the world when things look bleak?"],
                ["If you can smile about the bad times, you'll enjoy the good times even more."])
serv8  = Servant("The Dead", ["the end of a cycle", "death", "a finale", "something that is stopping"],\
                ["Are you ready to accept that this, too, shall pass?"],
                ["Everything comes to an end eventually."])
serv9  = Servant("The Depleted", ["loss", "depletion", "depression", "emptiness"],\
                ["Do any areas of your life feel like they're hollow?"],
                ["Make sure you don't completely burn yourself out."])
serv10 = Servant("The Desperate", ["pain", "desperation", "anxiety", "chaos"],\
                ["Is there something that you're having trouble handling?"],
                ["When the worst is happening, it is soon to be over."])
serv11 = Servant("The Devil", ["personal limitations", "addiction", "the chains that bind you", "your dark side"],\
                ["Do you feel that some parts of you are holding the rest of you back?"],
                ["Sometimes you might find you can be your own worst enemy."])
serv12 = Servant("The Explorer", ["discovery", "personal development", "potential", "hidden talent"],\
                ["Are you willing to go into uncharted territory?"],
                ["The greatest peaks and valleys you can explore are in your own head."])
Serv13 = Servant("The Eye", ["the divine plan", "omniscience", "destiny", "fate"],\
                ["Do you recognize how everything came together to bring you here?"],
                ["Everything is going according to plan."])
Serv14 = Servant("The Father", ["tough love", "guidance", "learning lessons", "facing challenges"],\
                ["Are you willing to push through discomfort?"],
                ["Hard times make stronger people."])
Serv15 = Servant("The Fixer", ["dedication", "solving problems no matter the cost", "persisting through adversity", "dirty work"],\
                ["Are you certain that you're willing to pay the price to get what you want?"],
                ["You can have anything you want, but not for free."])
Serv16 = Servant("The Fortunate", ["bounty", "good luck", "happiness", "the good life"],\
                ["Do you recognize the great treasures you may have reaped since starting your journey?"], 
                ["Good things are likely headed your way."])
Serv17 = Servant("The Gatekeeper", ["blocked entry", "delay", "feeling locked out", "finding a way in"],\
                ["Is there something blocking you from reaching your goal?"],
                ["There's always a way to get what you want."])
Serv18 = Servant("The Giver", ["gifts", "generosity", "charity", "gratitude"],\
                ["Last time you were involved in a gift exchange, were you the giver, or the receiver?"],
                ["You receive gifts every day--you just have to look for them."])
Serv19 = Servant("The Guru", ["self-mastery", "putting lessons into practice", "self-discipline", "practicality"],\
                ["Do you notice a difference between what you think you should do and what you end up doing?"],
                ["Without action, planning serves no purpose."])
Serv20 = Servant("The Healer", ["health", "restoration", "medicine", "caring for others"],\
                ["Are there any areas of your life that need healing?"],
                ["Not all sickness is immediately obvious."])
Serv21 = Servant("The Idea", ["inventiveness", "new ideas", "creativity", "inspiration"],\
                ["If you had to, could you think of a uniquely creative way to solve your problem?"],
                ["If an idea is just an idea for too long, it disappears."])
Serv22 = Servant("The Levitator", ["new perspectives", "detachment", "rising up", "aloofness"],\
                ["If you were watching your actions from above, how would you feel about them?"],
                ["Try not to let yourself get too rooted in problems."])
Serv23 = Servant("The Librarian", ["knowledge", "theory", "studying", "information"],\
                ["Is your repository of knowledge sufficient?"],
                ["Knowledge is power."])
Serv24 = Servant("The Lovers", ["commitment", "attachment", "deep connections", "relationships"],\
                ["Are you prepared to stay committed to your journey?"],
                ["Devotion is extremely powerful."])
Serv25 = Servant("The Master", ["your highest possible self", "a savior", "making good choices", "acting out of love"],\
                ["What would your Highest Self do?"],
                ["The best version of you, is still you."])
Serv26 = Servant("The Media", ["getting the word out", "advertisement", "propaganda", "interpretation"],\
                ["Is there something you would like to tell the world?"],
                ["Not everything is always as it seems."])
Serv27 = Servant("The Messenger", ["communication", "receptiveness", "being open to the world's messages", "receiving a message"],\
                ["Is there perhaps a piece of correspondence in transit?"],
                ["Someone may be trying to tell you something."])
Serv28 = Servant("The Monk", ["simplicity", "decluttering", "minimalism", "quiet elegance"],\
                ["Have any parts of your journey become too complicated?"],
                ["Most plans are best kept simple."])
Serv29 = Servant("The Moon", ["illusions", "lies", "self-deception", "that which is hidden"],\
                ["Have you considered the fact that something may be hidden from you right now?"],
                ["There's something about the situation that you don't know."])
Serv30 = Servant("The Mother", ["nurturing", "fertility", "new steps in life", "taking care of oneself"],\
                ["Are you taking good care of yourself?"],
                ["The universe loves you and wants you to be happy."])
Serv31 = Servant("The Opposer", ["restrictions", "outside intervention", "an enemy or enemies", "obstacles"],\
                ["Do you feel that someone or something is trying to hinder your progress?"],
                ["Not everyone out there wants to help you."])
Serv32 = Servant("The Planet", ["our place in creation", "the universe's beauty", "the world around you", "Earth"],\
                ["Do you feel that you're not certain of your place in the world?"],
                ["For some reason or another, you do belong here."])
Serv33 = Servant("The Protector", ["safety", "security", "protecting ourselves", "a guardian"],\
                ["Is there something that you feel is endangering you?"],
                ["Don't be paranoid, but don't be reckless."])
Serv34 = Servant("The Protester", ["fighting for what is right", "speaking out", "justice", "righteous passion"],\
                ["Do you know what you are willing to stand for?"],
                ["You will be heard, if you choose to speak."])
Serv35 = Servant("The Road Opener", ["opportunities", "open doors", "removal of obstacles", "seeing the path"],\
                ["Do you see the numerous opportunities that present themselves every day?"],
                ["The future might take you to some exciting places."])
Serv36 = Servant("The Saint", ["asking for help", "outside assistance", "an expert", "intervention"],\
                ["Might you simply need to ask an expert or mentor for guidance?"],
                ["The best person for a job is someone who knows how it's done."])
Serv37 = Servant("The Seer", ["intuition", "inner guidance", "gut feelings", "the subconscious"],\
                ["Has your gut been telling you that you're doing something right?"],
                ["Sometimes you can feel the truth without actually learning it."])
Serv38 = Servant("The Sun", ["radiance", "energy", "light", "a source of power"],\
                ["Do you feel the energy that is coursing through you?"],
                ["The light shines on us all."])
Serv39 = Servant("The Thinker", ["the conscious mind", "rational thought", "logic", "analysis"],\
                ["Have you spent enough time considering your next move?"],
                ["You may wish to take the most intelligent step next."])
Serv40 = Servant("The Witch", ["magic", "mystery", "sorcery", "the spiritual world"],\
                ["Do you believe in magic?"],
                ["Something special is in the works."])


# Functions
def draw():
    # Pick a random number
    randIndex = random.randrange(len(Servant.instances)) # Removing Servants from the list will not prevent the script from functioning
    # Pick a Servant based on the random number
    randCard = Servant.instances[randIndex]

    randMeaning = random.sample(Servant.meaning, k= 2) # Pick two random describers
    # Compose the Fortune
    introduction = str(f"You drew {randCard.name}...")
    description = str(f"That Servant represents", randMeaning[0], " and", randMeaning[1], ".")
    print(introduction) 
    time.sleep(2) # Pause for dramatic effect
    print(description)

# Window Setup
root = tk.Tk()
root.title("Forty Servants GUI")
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.minsize(800, 600)

# Custom Icon
root.iconbitmap('./appIcon.ico')

# Main loop
root.mainloop()
# while True:
#    draw()
#    choice = input("Hit Enter to draw another Servant. Enter anything else to quit.")
#    if choice == "":
#        continue
#    else:
#        break
