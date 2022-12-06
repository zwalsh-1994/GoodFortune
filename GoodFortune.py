# Good Fortune
# Author: Zachary Walsh
# Last edited December 3, 2022
# A fortune-telling Python application that includes an Oracle Deck and a Magic Eight-Ball.

import random
import time
import tkinter as tk
from tkinter import ttk


fortyWindow = None
eightballWindow = None

welcome = str("Welcome, traveler.")
goodbye = str("Goodbye, traveler.")


class Servant:
    instances = []
    def __init__(self, name, meaning, question, comment):
        self.name = name
        self.meaning = meaning
        self.question = question
        self.comment = comment
        # Create a list using the attributes from metadata area
        __class__.instances.append(self)

# Servant metadata using Servant class:
# Name, meaning, question, comment.
    def compose_fortune(self):
        name = self.name
        num_meanings = random.randint(1, len(self.meaning))
        meaning = self.meaning[:num_meanings]
        question = random.choice(self.question) # Questionable
        comment = random.choice(self.comment)   # Questionable
        return ("You drew " + str(name) + ", which represents the following: " + str(meaning) 
        + ".\n The card wants me to ask you: " + str(question)
        + "\n The card wants me to say: " + str(comment))

servants = [
    Servant("The Adventurer",
    ["adventure","a journey","excitement","new experiences"],
    ["Is there anything exciting coming up that you're looking forward to?"],
    ["Life is an adventure sometimes, whether or not you want it to be."]),
    Servant("The Balancer",
     ["symmetry", "equity", "normalcy", "equilibrium"],
     ["Have you considered how your goals affect other areas of your life?"],
     ["If you don't maintain balance, the universe will forcibly restore it eventually."]),
    Servant("The Carnal",
    ["attraction","dating","creative urges","romance"],
    ["Do you know that the world wants something that you have to offer?"],
    ["Sometimes, people are animals. Always, people are part animal."]),
    Servant("The Chaste",
    ["moderation","chastity","temperance","restraint"],
    ["Is there anything you really want to do that you might be better off not doing?"],
    ["Sometimes, abstaining is the more effective action to take."]),
    Servant("The Conductor",
    ["planning","orchestration","organization","taking charge",],
    ["Are you following a plan that you created, or are you drifting?"],
    ["Whether or not you steer the boat, the current moves you."]),
    Servant("The Contemplator",
    ["the unconscious mind", "meditation","rumination","introspection",],
    ["Have you really carefully considered what you want?"],
    ["Many dishes taste better if they spend a little time on the back burner."]),
    Servant("The Dancer",
    ["a routine", "gratitude in the face of adversity", "resilience", "hope for the future"],
    ["Do you recognize the good in the world when things look bleak?"],
    ["If you can smile about the bad times, you'll enjoy the good times even more."]),
    Servant("The Dead",
    ["the end of a cycle", "death", "a finale", "something that is stopping"],
    ["Are you ready to accept that this, too, shall pass?"],
    ["Everything comes to an end eventually."]),
    Servant("The Depleted",
    ["loss", "depletion", "depression", "emptiness"],
    ["Do any areas of your life feel like they're hollow?"],
    ["Make sure you don't completely burn yourself out."]),
    Servant("The Desperate",
    ["pain", "desperation", "anxiety", "chaos"],
    ["Is there something that you're having trouble handling?"],
    ["When the worst is happening, it is soon to be over."]),
    Servant("The Devil",
    ["personal limitations", "addiction", "the chains that bind you", "your dark side"],
    ["Do you feel that some parts of you are holding the rest of you back?"],
    ["Sometimes you might find you can be your own worst enemy."]),
    Servant("The Explorer",
    ["discovery", "personal development", "potential", "hidden talent"],
    ["Are you willing to go into uncharted territory?"],
    ["The greatest peaks and valleys you can explore are in your own head."]),
    Servant("The Eye",
    ["the divine plan", "omniscience", "destiny", "fate"],
    ["Do you recognize how everything came together to bring you here?"],
    ["Everything is going according to plan."]),
    Servant("The Father",
    ["tough love", "guidance", "learning lessons", "facing challenges"],
    ["Are you willing to push through discomfort?"],
    ["Hard times make stronger people."]),
    Servant("The Fixer",
    ["dedication", "solving problems no matter the cost", "persisting through adversity", "dirty work"],
    ["Are you certain that you're willing to pay the price to get what you want?"],
    ["You can have anything you want, but not for free."]),
    Servant("The Fortunate",
    ["bounty", "good luck", "happiness", "the good life"],
    ["Do you recognize the great treasures you may have reaped since starting your journey?"],
    ["Good things are likely headed your way."]),
    Servant("The Gatekeeper",
    ["blocked entry", "delay", "feeling locked out", "finding a way in"],
    ["Is there something blocking you from reaching your goal?"],
    ["There's always a way to get what you want."]),
    Servant("The Giver",
    ["gifts", "generosity", "charity", "gratitude"],
    ["Last time you were involved in a gift exchange, were you the giver, or the receiver?"],
    ["You receive gifts every day--you just have to look for them."]),
    Servant("The Guru",
    ["self-mastery", "putting lessons into practice", "self-discipline", "practicality"],
    ["Do you notice a difference between what you think you should do and what you end up doing?"],
    ["Without action, planning serves no purpose."]),
    Servant("The Healer",
    ["health", "restoration", "medicine", "caring for others"],
    ["Are there any areas of your life that need healing?"],
    ["Not all sickness is immediately obvious."]),
    Servant("The Idea",
    ["inventiveness", "new ideas", "creativity", "inspiration" ],
    ["If you had to, could you think of a uniquely creative way to solve your problem?"],
    ["If an idea is just an idea for too long, it disappears."]),
    Servant("The Levitator",
    ["new perspectives", "detachment", "rising up", "aloofness"],
    ["If you were watching your actions from above, how would you feel about them?"],
    ["Try not to let yourself get too rooted in problems."]),
    Servant("The Librarian", 
    ["knowledge", "theory", "studying", "information"],
    ["Is your repository of knowledge sufficient?"],
    ["Knowledge is power."]),
    Servant("The Lovers", 
    ["commitment", "attachment", "deep connections", "relationships"],\
    ["Are you prepared to stay committed to your journey?"],
    ["Devotion is extremely powerful."]),
    Servant("The Master", 
    ["your highest possible self", "a savior", "making good choices", "acting out of love"],\
    ["What would your Highest Self do?"],
    ["The best version of you, is still you."]),
    Servant("The Media", 
    ["getting the word out", "advertisement", "propaganda", "interpretation"],\
    ["Is there something you would like to tell the world?"],
    ["Not everything is always as it seems."]),
    Servant("The Messenger", 
    ["communication", "receptiveness", "being open to the world's messages", "receiving a message"],\
    ["Is there perhaps a piece of correspondence in transit?"],
    ["Someone may be trying to tell you something."]),
    Servant("The Monk", 
    ["simplicity", "decluttering", "minimalism", "quiet elegance"],\
    ["Have any parts of your journey become too complicated?"],
    ["Most plans are best kept simple."]),
    Servant("The Moon", 
    ["illusions", "lies", "self-deception", "that which is hidden"],\
    ["Have you considered the fact that something may be hidden from you right now?"],
    ["There's something about the situation that you don't know."]),
    Servant("The Mother", 
    ["nurturing", "fertility", "new steps in life", "taking care of oneself"],\
    ["Are you taking good care of yourself?"],
    ["The universe loves you and wants you to be happy."]),
    Servant("The Opposer", 
    ["restrictions", "outside intervention", "an enemy or enemies", "obstacles"],\
    ["Do you feel that someone or something is trying to hinder your progress?"],
    ["Not everyone out there wants to help you."]),
    Servant("The Planet",
    ["our place in creation", "the universe's beauty", "the world around you", "Earth"],\
    ["Do you feel that you're not certain of your place in the world?"],
    ["For some reason or another, you do belong here."]),
    Servant("The Protector", 
    ["safety", "security", "protecting ourselves", "a guardian"],\
    ["Is there something that you feel is endangering you?"],
    ["Don't be paranoid, but don't be reckless."]),
    Servant("The Protester",
    ["fighting for what is right", "speaking out", "justice", "righteous passion"],
    ["Do you know what you are willing to stand for?"],
    ["You will be heard, if you choose to speak."]),
    Servant("The Road Opener", 
    ["opportunities", "open doors", "removal of obstacles", "seeing the path"],\
    ["Do you see the numerous opportunities that present themselves every day?"],
    ["The future might take you to some exciting places."]),
    Servant("The Saint", 
    ["asking for help", "outside assistance", "an expert", "intervention"],\
    ["Might you simply need to ask an expert or mentor for guidance?"],
    ["The best person for a job is someone who knows how it's done."]),
    Servant("The Seer",
    ["intuition", "inner guidance", "gut feelings", "the subconscious"],\
    ["Has your gut been telling you that you're doing something right?"],
    ["Sometimes you can feel the truth without actually learning it."]),
    Servant("The Sun", 
    ["radiance", "energy", "light", "a source of power"],\
    ["Do you feel the energy that is coursing through you?"],
    ["The light shines on us all."]),
    Servant("The Thinker", 
    ["the conscious mind", "rational thought", "logic", "analysis"],\
    ["Have you spent enough time considering your next move?"],
    ["You may wish to take the most intelligent step next."]),
    Servant("The Witch", 
    ["magic", "mystery", "sorcery", "the spiritual world"],\
    ["Do you believe in magic?"],
    ["Something special is in the works."])
]

# Functions
def openForty():
    global fortyWindow
    fortyWindow = tk.Toplevel(root)
    fortyWindow.title("Forty Servants")
    window_width = 500
    window_height = 575
    screen_width = fortyWindow.winfo_screenwidth()
    screen_height = fortyWindow.winfo_screenheight()
    center_x = int((3*screen_width/4) - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    fortyWindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    fortyWindow.resizable(True,True)

    def show_fortune():
        card = random.choice(servants)

        fortune = card.compose_fortune()

        frame = tk.Frame(fortyWindow)
        tk.Label(frame, text="".join(fortune)).pack()
        frame.pack()
    tk.Button(fortyWindow, text="Draw a Card", command=show_fortune).pack()

def openEightball():
    global eightballWindow
    eightballWindow = tk.Toplevel(root)
    eightballWindow.title("Magic 8 Ball")
    window_width = 800
    window_height = 600
    screen_width = eightballWindow.winfo_screenwidth()
    screen_height = eightballWindow.winfo_screenheight()
    center_x = int((3*screen_width/4) - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    eightballWindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    eightballWindow.minsize(800, 600)
    eightballWindow.resizable(False, False)

    eightball_quit_button = ttk.Button(
        eightballWindow,
        text="Quit",
        command= lambda: eightballWindow.destroy()
    )
    eightball_quit_button.pack(
        ipadx=5,
        ipady=5,
        side=tk.BOTTOM,
        anchor=tk.S
    )

    eightballWindow.mainloop()


# Root Window
root = tk.Tk()
root.title("Good Fortune")
window_width = 750
window_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int((3*screen_width/4) - window_width / 2) # Moved to off-center for editing
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False,False)

# Root Window Components
# Title and Explanation
title = ttk.Label(
    root,
    anchor= tk.CENTER, 
    background=('#702048'), 
    font=("Arial", 32),
    foreground=('white'),
    text= "Good Fortune \nA Fortune-Telling Python Program",
    justify=('center')
)

title.pack()


# Buttons
# Button for Forty Servants
    # Place on the left and expand, background should be image of cards
forty_button = ttk.Button(
    root,
    text= "Forty Servants",
    command= openForty
)
forty_button.pack()

# Button for Eight-Ball
    # Place on the right and expand, background should be image of eight-ball
eight_button = ttk.Button(
    root,
    text= "Magic Eight-Ball",
    command= openEightball
)

eight_button.pack()

# Quit Button
    # Place between the two other buttons
quit_button = ttk.Button(
    root,
    text="Quit",
    command= lambda: quit() # was root.quit() but that didn't work properly for some reason
)

quit_button.pack()

# Custom Icon(s)
root.iconbitmap('./assets/appIcon.ico')

# Main loop
root.mainloop()