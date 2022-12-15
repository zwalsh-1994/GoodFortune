# Good Fortune
# Author: Zachary Walsh
# Last edited December 14, 2022
# A fortune-telling Python application that includes an Oracle Deck and a Magic Eight-Ball.
# The Forty Servants oracle deck was created by Tommie Kelly.

import random
import time
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
fortyWindow = None
eightballWindow = None

welcome = str("Welcome, traveler.")
goodbye = str("Goodbye, traveler.")

root = tk.Tk()
root.title("Good Fortune")
window_width = 825
window_height = 535
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int((3*screen_width/4) - window_width / 2) # Moved to off-center for editing
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False,False)

class Servant:
    instances = []
    def __init__(self, name, image, meaning, question, comment):
        self.name = name
        self.image = tk.PhotoImage(file=image)
        self.meaning = meaning
        self.question = question
        self.comment = comment
        # Create a list using the attributes from metadata area
        __class__.instances.append(self)

    def compose_fortune(self):
        name = self.name
        num_meanings = random.randint(1, len(self.meaning))
        meaning = self.meaning[:num_meanings]
        question = random.choice(self.question) # Questionable
        comment = random.choice(self.comment)   # Questionable
        return ("You drew " + str(name) + ", which represents the following: " + str(meaning) 
        + ".\n The card wants me to ask you: " + str(question)
        + "\n The card wants me to say: " + str(comment))

    def sayName(self):
        name = self.name
        image = self.image
        nameText = ("You drew " + str(name) + ".\n")
        nameFrame = tk.Frame(fortyWindow)
        cardFrame = tk.Frame(fortyWindow)
        tk.Label(nameFrame, text="".join(nameText)).pack()
        nameFrame.pack()
        tk.Label(cardFrame, image=image).pack()
        cardFrame.pack()
        fortyWindow.update()

    def sayMean(self):
        num_meanings = random.randint(2, len(self.meaning))
        meaning = self.meaning[:num_meanings]
        meanText = ("That Servant can represent the following: " + str(meaning) + ".\n")
        meanFrame = tk.Frame(fortyWindow)
        tk.Label(meanFrame, text="".join(meanText)).pack()
        meanFrame.pack()
        fortyWindow.update()

    def sayQues(self):
        name = self.name
        question = random.choice(self.question)
        quesText = (str(name) + " wants me to ask you: " + str(question) + "\n")
        quesFrame = tk.Frame(fortyWindow)
        tk.Label(quesFrame, text="".join(quesText)).pack()
        quesFrame.pack()
        fortyWindow.update()

    def sayComm(self):
        comment = random.choice(self.comment)
        commText = ("Finally, the card wants me to say: " + str(comment))
        commFrame = tk.Frame(fortyWindow)
        tk.Label(commFrame, text="".join(commText)).pack()
        commFrame.pack()
        fortyWindow.update()






# Servant metadata using Servant class:
# Name, meaning, question, comment.
servants = [
    Servant("The Adventurer",
    ["./assets/adventurerFull.png"],
    ["adventure","a journey","excitement","new experiences"],
    ["Is there anything exciting coming up that you're looking forward to?"],
    ["Life is an adventure sometimes, whether or not you want it to be."]),
    Servant("The Balancer",
    ["./assets/balancerFull.png"],
    ["symmetry", "equity", "normalcy", "equilibrium"],
    ["Have you considered how your goals affect other areas of your life?"],
    ["If you don't maintain balance, the universe will forcibly restore it eventually."]),
    Servant("The Carnal",
    ["./assets/carnalFull.png"],
    ["attraction","dating","creative urges","romance"],
    ["Do you know that the world wants something that you have to offer?"],
    ["Sometimes, people are animals. Always, people are part animal."]),
    Servant("The Chaste",
    ["./assets/chasteFull.png"],
    ["moderation","chastity","temperance","restraint"],
    ["Is there anything you really want to do that you might be better off not doing?"],
    ["Sometimes, abstaining is the more effective action to take."]),
    Servant("The Conductor",
    ["./assets/conductorFull.png"],
    ["planning","orchestration","organization","taking charge",],
    ["Are you following a plan that you created, or are you drifting?"],
    ["Whether or not you steer the boat, the current moves you."]),
    Servant("The Contemplator",
    ["./assets/contemplatorFull.png"],
    ["the unconscious mind", "meditation","rumination","introspection",],
    ["Have you really carefully considered what you want?"],
    ["Many dishes taste better if they spend a little time on the back burner."]),
    Servant("The Dancer",
    ["./assets/dancerFull.png"],
    ["a routine", "gratitude in the face of adversity", "resilience", "hope for the future"],
    ["Do you recognize the good in the world when things look bleak?"],
    ["If you can smile about the bad times, you'll enjoy the good times even more."]),
    Servant("The Dead",
    ["./assets/deadFull.png"],
    ["the end of a cycle", "death", "a finale", "something that is stopping"],
    ["Are you ready to accept that this, too, shall pass?"],
    ["Everything comes to an end eventually."]),
    Servant("The Depleted",
    ["./assets/depletedFull.png"],
    ["loss", "depletion", "depression", "emptiness"],
    ["Do any areas of your life feel like they're hollow?"],
    ["Make sure you don't completely burn yourself out."]),
    Servant("The Desperate",
    ["./assets/desperateFull.png"],
    ["pain", "desperation", "anxiety", "chaos"],
    ["Is there something that you're having trouble handling?"],
    ["When the worst is happening, it is soon to be over."]),
    Servant("The Devil",
    ["./assets/devilFull.png"],
    ["personal limitations", "addiction", "the chains that bind you", "your dark side"],
    ["Do you feel that some parts of you are holding the rest of you back?"],
    ["Sometimes you might find you can be your own worst enemy."]),
    Servant("The Explorer",
    ["./assets/explorerFull.png"],
    ["discovery", "personal development", "potential", "hidden talent"],
    ["Are you willing to go into uncharted territory?"],
    ["The greatest peaks and valleys you can explore are in your own head."]),
    Servant("The Eye",
    ["./assets/eyeFull.png"],
    ["the divine plan", "omniscience", "destiny", "fate"],
    ["Do you recognize how everything came together to bring you here?"],
    ["Everything is going according to plan."]),
    Servant("The Father",
    ["./assets/fatherFull.png"],
    ["tough love", "guidance", "learning lessons", "facing challenges"],
    ["Are you willing to push through discomfort?"],
    ["Hard times make stronger people."]),
    Servant("The Fixer",
    ["./assets/fixerFull.png"],
    ["dedication", "solving problems no matter the cost", "persisting through adversity", "dirty work"],
    ["Are you certain that you're willing to pay the price to get what you want?"],
    ["You can have anything you want, but not for free."]),
    Servant("The Fortunate",
    ["./assets/fortunateFull.png"],
    ["bounty", "good luck", "happiness", "the good life"],
    ["Do you recognize the great treasures you may have reaped since starting your journey?"],
    ["Good things are likely headed your way."]),
    Servant("The Gatekeeper",
    ["./assets/gatekeeperFull.png"],
    ["blocked entry", "delay", "feeling locked out", "finding a way in"],
    ["Is there something blocking you from reaching your goal?"],
    ["There's always a way to get what you want."]),
    Servant("The Giver",
    ["./assets/giverFull.png"],
    ["gifts", "generosity", "charity", "gratitude"],
    ["Last time you were involved in a gift exchange, were you the giver, or the receiver?"],
    ["You receive gifts every day--you just have to look for them."]),
    Servant("The Guru",
    ["./assets/guruFull.png"],
    ["self-mastery", "putting lessons into practice", "self-discipline", "practicality"],
    ["Do you notice a difference between what you think you should do and what you end up doing?"],
    ["Without action, planning serves no purpose."]),
    Servant("The Healer",
    ["./assets/healerFull.png"],
    ["health", "restoration", "medicine", "caring for others"],
    ["Are there any areas of your life that need healing?"],
    ["Not all sickness is immediately obvious."]),
    Servant("The Idea",
    ["./assets/ideaFull.png"],
    ["inventiveness", "new ideas", "creativity", "inspiration" ],
    ["If you had to, could you think of a uniquely creative way to solve your problem?"],
    ["If an idea is just an idea for too long, it disappears."]),
    Servant("The Levitator",
    ["./assets/levitatorFull.png"],
    ["new perspectives", "detachment", "rising up", "aloofness"],
    ["If you were watching your actions from above, how would you feel about them?"],
    ["Try not to let yourself get too rooted in problems."]),
    Servant("The Librarian", 
    ["./assets/librarianFull.png"],
    ["knowledge", "theory", "studying", "information"],
    ["Is your repository of knowledge sufficient?"],
    ["Knowledge is power."]),
    Servant("The Lovers", 
    ["./assets/loversFull.png"],
    ["commitment", "attachment", "deep connections", "relationships"],\
    ["Are you prepared to stay committed to your journey?"],
    ["Devotion is extremely powerful."]),
    Servant("The Master", 
    ["./assets/masterFull.png"],
    ["your highest possible self", "a savior", "making good choices", "acting out of love"],\
    ["What would your Highest Self do?"],
    ["The best version of you, is still you."]),
    Servant("The Media", 
    ["./assets/mediaFull.png"],
    ["getting the word out", "advertisement", "propaganda", "interpretation"],\
    ["Is there something you would like to tell the world?"],
    ["Not everything is always as it seems."]),
    Servant("The Messenger", 
    ["./assets/messengerFull.png"],
    ["communication", "receptiveness", "being open to the world's messages", "receiving a message"],\
    ["Is there perhaps a piece of correspondence in transit?"],
    ["Someone may be trying to tell you something."]),
    Servant("The Monk", 
    ["./assets/monkFull.png"],
    ["simplicity", "decluttering", "minimalism", "quiet elegance"],\
    ["Have any parts of your journey become too complicated?"],
    ["Most plans are best kept simple."]),
    Servant("The Moon", 
    ["./assets/moonFull.png"],
    ["illusions", "lies", "self-deception", "that which is hidden"],\
    ["Have you considered the fact that something may be hidden from you right now?"],
    ["There's something about the situation that you don't know."]),
    Servant("The Mother", 
    ["./assets/motherFull.png"],
    ["nurturing", "fertility", "new steps in life", "taking care of oneself"],\
    ["Are you taking good care of yourself?"],
    ["The universe loves you and wants you to be happy."]),
    Servant("The Opposer", 
    ["./assets/opposerFull.png"],
    ["restrictions", "outside intervention", "an enemy or enemies", "obstacles"],\
    ["Do you feel that someone or something is trying to hinder your progress?"],
    ["Not everyone out there wants to help you."]),
    Servant("The Planet",
    ["./assets/planetFull.png"],
    ["our place in creation", "the universe's beauty", "the world around you", "Earth"],\
    ["Do you feel that you're not certain of your place in the world?"],
    ["For some reason or another, you do belong here."]),
    Servant("The Protector", 
    ["./assets/protectorFull.png"],
    ["safety", "security", "protecting ourselves", "a guardian"],\
    ["Is there something that you feel is endangering you?"],
    ["Don't be paranoid, but don't be reckless."]),
    Servant("The Protester",
    ["./assets/protesterFull.png"],
    ["fighting for what is right", "speaking out", "justice", "righteous passion"],
    ["Do you know what you are willing to stand for?"],
    ["You will be heard, if you choose to speak."]),
    Servant("The Road Opener", 
    ["./assets/roadopenerFull.png"],
    ["opportunities", "open doors", "removal of obstacles", "seeing the path"],\
    ["Do you see the numerous opportunities that present themselves every day?"],
    ["The future might take you to some exciting places."]),
    Servant("The Saint", 
    ["./assets/saintFull.png"],
    ["asking for help", "outside assistance", "an expert", "intervention"],\
    ["Might you simply need to ask an expert or mentor for guidance?"],
    ["The best person for a job is someone who knows how it's done."]),
    Servant("The Seer",
    ["./assets/seerFull.png"],
    ["intuition", "inner guidance", "gut feelings", "the subconscious"],\
    ["Has your gut been telling you that you're doing something right?"],
    ["Sometimes you can feel the truth without actually learning it."]),
    Servant("The Sun", 
    ["./assets/sunFull.png"],
    ["radiance", "energy", "light", "a source of power"],\
    ["Do you feel the energy that is coursing through you?"],
    ["The light shines on us all."]),
    Servant("The Thinker", 
    ["./assets/thinkerFull.png"],
    ["the conscious mind", "rational thought", "logic", "analysis"],\
    ["Have you spent enough time considering your next move?"],
    ["You may wish to take the most intelligent step next."]),
    Servant("The Witch", 
    ["./assets/witchFull.png"],
    ["magic", "mystery", "sorcery", "the spiritual world"],\
    ["Do you believe in magic?"],
    ["Something special is in the works."])
]



# Functions
def openForty():
    global fortyWindow
    fortyWindow = tk.Toplevel(root)
    fortyWindow.title("Forty Servants")
    window_width = 700
    window_height = 850
    screen_width = fortyWindow.winfo_screenwidth()
    screen_height = fortyWindow.winfo_screenheight()
    center_x = int((3*screen_width/4) - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    fortyWindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    fortyWindow.resizable(True,True)

    def newFortune():
        choice = random.choice(servants)
        choice.sayName()
        time.sleep(random.randint(1,2))
        choice.sayMean()
        time.sleep(random.randint(2,3))
        choice.sayQues()
        time.sleep(random.randint(2,3))
        choice.sayComm()
        time.sleep(1)

    def show_fortune():
        card = random.choice(servants)

        fortune = card.compose_fortune()

        frame = tk.Frame(fortyWindow)
        tk.Label(frame, text="".join(fortune)).pack()
        frame.pack()

    def startFortune():
        card = random.choice(servants)

        part1 = card.sayName()

        nameFrame = tk.Frame(fortyWindow)
        tk.Label(nameFrame, text="".join(part1)).pack()
        nameFrame.pack()

        part2 = card.sayMean()

        meanFrame = tk.Frame(fortyWindow)
        tk.Label(meanFrame, text="".join(part2)).pack()
        meanFrame.pack()

        part3 = card.sayQues()

        quesFrame = tk.Frame(fortyWindow)
        tk.Label(quesFrame, text="".join(part3)).pack()
        quesFrame.pack()

        part4 = card.sayComm()

        commFrame = tk.Frame(fortyWindow)
        tk.Label(commFrame, text="".join(part4)).pack()
        commFrame.pack()

    tk.Button(fortyWindow, text="Draw a Card", command=newFortune).pack()

def openEightball():
    global eightballWindow
    eightballWindow = tk.Toplevel(root)
    eightballWindow.title("Magic 8 Ball")
    window_width = 400
    window_height = 250
    screen_width = eightballWindow.winfo_screenwidth()
    screen_height = eightballWindow.winfo_screenheight()
    center_x = int((3*screen_width/4) - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    eightballWindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    eightballWindow.resizable(False, False)

    bg_label = tk.Label(eightballWindow)
    bg_label.place(bordermode="inside",relheight=1,relwidth=1)

    def shakeBall():
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes, definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better to not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook no so good.",
            "Very doubtful."
        ]
        response = random.choice(responses)

        respLabel = tk.Label(bg_label, text="Shaking...", background="blue", foreground="white")
        respLabel.place(relheight=1, relwidth=1)
        respLabel.update()
        time.sleep(1.5)
        respLabel = tk.Label(bg_label, text="".join(response), background="blue", foreground="white")
        respLabel.place(relheight=1, relwidth=1)
        respLabel.update()

    ballButtonFrame = tk.Frame(eightballWindow)
    ballButtonFrame.pack(
        side=tk.BOTTOM
    )
    shakeButton = ttk.Button(
        ballButtonFrame,
        text="Shake",
        command=shakeBall
    )
    shakeButton.pack(
        ipadx=5,
        ipady=5,
    )

    eightball_quit_button = ttk.Button(
        ballButtonFrame,
        text="Quit",
        command= lambda: eightballWindow.destroy()
    )
    eightball_quit_button.pack(
        ipadx=5,
        ipady=5
    )

    eightballWindow.mainloop()


# Root Window


# Root Window Components
# Title and Explanation

titleFrame = tk.Frame(
    root
)
titleFrame.pack(
    side="top",
    anchor=tk.N,
    fill="x"
)
title = ttk.Label(
    titleFrame,
    font=("Arial", 32),
    foreground=('#702048'),
    text= "Good Fortune \nA Fortune-Telling Python Program",
    justify=('center')
)
title.pack(
    side="top",
    anchor=tk.N
)

imageFrame = tk.Frame(
    root,
    width=820,
    height=405
)
imageFrame.pack(
    anchor=tk.CENTER
)

forty_image = ImageTk.PhotoImage(Image.open("./assets/fortyMenu.png"))
eight_image = ImageTk.PhotoImage(Image.open("./assets/magicMenu.png"))
fortyLabel = tk.Button(
    imageFrame,
    image= forty_image,
    command=openForty
).pack(
    side="left"
)
eightLabel = tk.Button(
    imageFrame,
    image=eight_image,
    command=openEightball
).pack(
    side="right"
)
# Buttons

buttonFrame = tk.Frame(
    root,
    height=50,
    width=700,
)

buttonFrame.pack(
    side="bottom",
    fill="x"
)


# Button for Forty Servants
    # Place on the left and expand, background should be image of cards
forty_button = ttk.Button(
    buttonFrame,
    text= "Forty Servants",
    command= openForty
)
forty_button.pack(
    side="left",
    ipadx=80,
    fill="x"
)

# Button for Eight-Ball
    # Place on the right and expand, background should be image of eight-ball
eight_button = ttk.Button(
    buttonFrame,
    text= "Magic Eight-Ball",
    command= openEightball
)

eight_button.pack(
    side="right",
    ipadx=80,
    fill="x"
)

# Quit Button
    # Place between the two other buttons
quit_button = ttk.Button(
    buttonFrame,
    text="Quit",
    command= lambda: quit() # was root.quit() but that didn't work properly for some reason
)

quit_button.pack(
    side="bottom",
    ipadx=20,
    fill="x"
)

# Custom Icon(s)
root.iconbitmap('./assets/appIcon.ico')

# Main loop
root.mainloop()