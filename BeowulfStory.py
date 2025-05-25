import tkinter
import tkinter.messagebox

#used to count what scene player is in
scene = -1

option1 = True
option2 = False

class mainGUI():

    def __init__(self):

        #initialize window and window size
        self.main_window = tkinter.Tk()
        self.main_window.geometry("800x600")

        #create the frames for the GUI
        self.image_frame = tkinter.Frame(self.main_window)
        self.text_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #main narrative label
        self.main_label = tkinter.Label(self.text_frame,text='Hello! Welcome to my game! This is my program that is based\n' +
        'off the story of Beowulf. In order to navigate the game, please use the buttons below, labeled as \n'+
        '"Option 1" and "Option 2" currently. Please note that you can click the "Quit Game" button at any time to exit.')
        self.main_label.pack(padx=10,pady=10)

        global scene
        
        # buttons for game. Options 1,2 and quit
        self.left_button = tkinter.Button(self.button_frame,text='Option 1',command=lambda: [self.increase_scene_counter(option1),self.change_label()])
        self.left_button.pack(side='left',padx=10)

        self.quit_button = tkinter.Button(self.button_frame,text='Quit Game',command=self.main_window.destroy)
        self.quit_button.pack(side='left',padx=10)

        self.right_button = tkinter.Button(self.button_frame,text='Option 2',command=lambda: [self.increase_scene_counter(option2),self.change_label()])
        self.right_button.pack(side='left',padx=10)



        #pack all frames
        self.image_frame.pack()
        self.text_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

#////////////////////////////////////////////////////////////////

    def increase_scene_counter(self,option):
        global scene
        
        #main menu info textbox
        if scene == 0:
            if option == False:
                tkinter.messagebox.showinfo("Info / Credits","Game Controls:\n\nUse the left and right buttons to declare your decision to the situation above." +
                " Upon death, You will recieve a messagebox saying you died and what ending you received. You will then return to this main screen"+
                " to continue another run. You can press the 'Quit Game' button at any time to exit the game.\n----------------------\nCredits:\n\nProgramming: Ryan"+
                " Franti\nStory development: Ryan & Rebekah Franti\n----------------------\nVersion History:\n\nVersion 1.0.0 \nMade through the use of Python, Visual Studio"+
                " Code, and PipInstall.\nThere are currently 13 normal endings and 5 secret endings.")
                scene = -1
                self.change_label()
                

        #hero-less end
        if scene ==1:
            if option == True:
                tkinter.messagebox.showinfo("The End.","You decided it would be better if you never embarked "+
                "on your journey. You lived a long life (as long as possible in those times) and died a nobody. A true waste of talent.\n\n"+
                "ENDING (1/13) - 'Fastest Speedrun Record'")
                
                scene = -1
                self.change_label()

        #scene 2 is optional - no endings
        if scene == 2:
            if option == False:
                scene +=2

        #escape prison end
        elif scene ==3:
            if option == True:
                tkinter.messagebox.showinfo("RIOT!","You and your barbaric friends decide to escape from prision because all you wanted to do was help."+
                " In your process of 'helping' you manage to 'accidentally' destoy the entire dungeon getting out of it. Unfortunately your friends "+
                "got hungry and decided to 'look for a snack' and after a few minutes the entire town marketplace was destoyed. The same happened to every tavern nearby" +
                " when someone got thirsty too. With the help of the townsfolk, the guards were able to lock you tazmanian devils outside the city and outcast you all."+
                "\n\n You said you were coming to help but you did more damage than the monster ever did...why did you do this?\n\nENDING (2/13) - 'We Came, We Saw, We Destroyed'")
                scene = -1
                self.change_label()

        #rot in prison end
        elif scene ==4:
            if option == False:
                tkinter.messagebox.showinfo("Thats a NAT 1 for Charisma", "I do not know how it happened, but even though the king needs every bit of help he can "+
                "get, he is convinced that you are all enemies sent to destroy him. You end up imprisoned in the town, and hear the screams of the inoccents " +
                "every night that Grendel rages in the town. I guess you can't be a hero without at least a little diplomatic skills.\n\n"+
                "ENDING (3/13) - 'This Wasn't Supposed to Happen...'")
                scene = -1
                self.change_label()

        #keep weapons end
        elif scene ==5:
            if option == True:
                tkinter.messagebox.showinfo("Very KNIFE to meet you...", "Stubborn and unwilling, you refuse to release your weapons. The guards nearby "+
                "become more and more hostile and forceful, telling you to drop your weapons. One of the guards grabs your weapons and you fly into a murderous "+
                "rampage, killing everyone in sight. When you are released from your trance you realize that everyone, both friend and foe is dead. You "+
                "leave the deserted town behind and live with your guilt for the rest of your days.\n\n"+
                "ENDING (4/13) - 'The Crows Eat Well Tonight'")
                scene = -1
                self.change_label()

        #begin fight end
        elif scene ==6:
            if option == False:
                tkinter.messagebox.showinfo("Counldn't an arm wrestle suffice?","You tend to be a person who does not handle stress very well, and on top of "+
                "your massive ego, you did not take well to being questioned by this tiny human. Instead of taking a more reasonable approach, you decide to smash "+
                "him into a gorey mess. I think its safe to say that the king did not take that very well, and he sentenced you to death. Luckily, the town has their "+
                "very own pet monster!\n\nENDING (5/13) - 'Yeah... Not a Good Idea'")
                scene = -1
                self.change_label()

        #grab weapon end
        elif scene ==7:
            if option == False:
                tkinter.messagebox.showinfo("Uh oh...","You come to the conclusion that you are unarmed against a massive monster, and that you need to fix that. "+
                "You reach for any nearby weapon, and eventually your hand grabs something. Without thinking further, you launch the item in your hand at the monster, only " +
                "to realize that you grabbed a broomstick. The broomstick breaks in half as it hits Grendel, who doesn't even flinch at the hit. In your last felleting "+
                "thoughts, you realize that it would have been smart to remember that Grendel is immune to weapons...\n\nENDING (6/13) - 'The Barbarian and The Broomstick'")
                scene = -1
                self.change_label()

        #sleep in town hall end
        elif scene ==8:
            if option == False:
                tkinter.messagebox.showinfo("Not so Sweet Dreams","You decide it would be best to rest with the king's guards in the main halls, especially since it would keep "+
                "the party going at the same time. After much more drink, you eventually fall asleep. Unfortunately for you, another monster strikes the hall in the night "+
                "and most people don't make it out of the hall alive... Including you.\n\nENDING (7/13) - Unfortunate Risk")
                scene = -1
                self.change_label()

        #walk away end
        elif scene ==9:
            if option == True:
                tkinter.messagebox.showinfo("Not Meant to be a Hero.","You couldn't stand the idea of fighting an even more powerful version of Grendel, "+
                "much less her mother (you have a bad record with meeting family for the first time). You walk away from the fight, and although you are praised and rewarded, "+
                "you always wonder what might've happened if you stayed.\n\nENDING (8/13) - Some Risk, Some Reward")
                scene = -1
                self.change_label()

        #rely on strength end
        elif scene ==10:
            if option == True:
                tkinter.messagebox.showinfo("Overconfident?","Charged by your pride and confident with your skills you used against Grendel, you find the beast's "+
                "underwater lair and dive into it without even thinking to protect yourself. After swimming downward for a short while, you see a massive dark hand move quickly through "+
                "the water. Grendel's mother grabs your entire body with her one hand and hold you in her iron grip. No matter how hard you try, you cannot escape "+
                "her grip as she crushes you in it. As you fall into the internal sleep of death, you realize that this was a great trap.\n\nEnding (9/13) - 'A Hero's End'")
                scene = -1
                self.change_label()

        # weak spot end
        elif scene ==11:
            if option == False:
                tkinter.messagebox.showinfo("A Novice's Greatest Enemy","You continually circle Grendel's mother, dodging attacks and retreating when necessary. "+
                "But no matter how hard you attack or look, you cannot see any spot that would hurt the monster. After a long while, you begin to get tired from constantly " +
                "fighting, but the monster only seems to be getting stronger. You realize that your tiredness is being used against you, but unfortunately "+
                "you can do nothing about it. You die because you didn't pace yourself.\n\nENDING (12/13) - I'm Tired...")
                scene = -1
                self.change_label()

        # end of story
        elif scene ==12:
            if option == True:
                tkinter.messagebox.showinfo("The (Official) End.","You played through the story of Beowulf to the dot. Either you know the "+
                "story, you're a really good guesser, or you're determined to get all endings. Either way, I sincerely thank you for playing my game. "+
                "It is one of my most favorite games I've created, and I hope you enjoyed at least some of my humor. But for now, I'm sure you're "+
                "sick of automatically restarting, so for this one ending only at a low-low price of $1.99 (just kidding), I have decided to make your life"+
                " easier and close the game myself by using a super-secret command that closes the game (its literally the easiest thing ever but hopefully you "+
                "can call it a feature in your review, It would really help a lot) all you have to do is the the 'OK' button below...\n\nENDING (13/13) - You Deserve It")
                self.main_window.destroy()
            
            #continue on to secret endings
            if option == False:

                scene-= 23
#////////////////////////////////////////////////////

        # SECRET ENDINGS

        elif scene == -10:
            if option == True:
                self.main_label.config(text="Thank you. But this conversation has completely ruined my mood. Try not to be so rude next time.")
                tkinter.messagebox.showinfo('The End', "SECRET ENDING! (-1/-5) - 'Dissapointment'")
                scene = -1
                self.change_label()
            
            if option == False:
                scene -= 11

        elif scene ==-20:
            if option == True:
                scene -= 2

            if option == False:
                scene -=11

        elif scene == -21:
            if option == True:
                tkinter.messagebox.showinfo('A simple story...', "Then I'm glad you found a story for yourself. Just try not to ruin mine.\n\nSECRET ENDING! (-2/-5) - 'A Sad Story'")
                scene = -1
                self.change_label()

            if option == False:
                tkinter.messagebox.showinfo('iM a PrOfeSSiOnAL!', "Then perhaps you should leave the storytelling to the professionals.\n\nSECRET ENDING! (-3/-5) - 'Meddler'")
                scene = -1
                self.change_label()

        elif scene == -30:
            if option == True:
                
                tkinter.messagebox.showinfo('Why are you like this?', "Are you literally trying to copy my story? All you did was rename the main character without the 'O' in his "+
                                       "name!... uuuuuhhhhhhhh, you win... I guess.\n\nSECRET ENDING! (-4/-5) - 'Mine is Better'")
                scene = -1
                self.change_label()

            if option == False:
                tkinter.messagebox.showinfo('Thats the wrong story', "Haha. I love the name change, but this isn't that type of story.\n\nSECRET ENDING! (-5/-5) - 'Not Happening'")
                scene = -1
                self.change_label()
        
        scene += 1


#///////////////////////////////////////////////////////////////////


    #fuction to change main label text based on scene and options
    def change_label(self):

        global scene
        

        if scene == 0:

            self.main_label.config(text="WELCOME TO:\n A Beowulf Adventure!\n\nBy: Ryan M. Franti")
            self.left_button.config(text="Click to continue")
            self.right_button.config(text="Info / Credits")

        elif scene ==1:
            self.main_label.config(text="You are Beowulf, mightiest man on earth, highborn and powerful. You hear about a distant kingdom that is being \n" +
            "ravaged by a monster named Grendel. Being in a position to help, you consider sailing across the seas to aid.\n Would you like to begin a great adventure?")
            self.left_button.config(text="Refuse to help")
            self.right_button.config(text="Embark on a journey")

        #this is an optional / hidden scene
        #//////////////////////////////////
        elif scene ==2:
            self.main_label.config(text="You enlist the help of 14 others and set sail to the kingdom to help defend against the beast. As you come ashore, there is \n"+
            "a watchman who comes to interrogate you about your presence. He asks you who you are and what business you have showing up here. ")
            self.left_button.config(text="Say you have come\nto rage war")
            self.right_button.config(text="Say you have come\nto kill")
        #/////////////////////////////////

        elif scene ==3:
            self.main_label.config(text='The watchman, out of obligation and concern for his king, arrests you and your men. He places you in the town prison \n'+
            "while the watchman alterts his king and tells you to wait for your interrogation. While waiting, you decide to:")
            self.left_button.config(text="Escape the prison")
            self.right_button.config(text="Wait for interrogation")

        elif scene ==4:
            self.main_label.config(text="You and your men are put before an interrogator. You are all interrogated one at a time asking you why you came to Heorot and who you are.")
            self.left_button.config(text="Say that you are\nhere to help fight Grendel")
            self.right_button.config(text="Say that you have\ncome for war")

        elif scene ==5:
            self.main_label.config(text="The guard brings you back to the king, who believes your story and welcomes your party to his hall - Heorot.\n You are told to enter when possible to discuss your strategy against Grendel.\n"+
            " Upon arriving at the hall, you are stopped by a guard. He states: \n'You are welcome to bring your helmets and armor but all weapons must be left behind.'")
            self.left_button.config(text="Refuse to leave your weapons")
            self.right_button.config(text="Leave your weapons \nwith one of your members")

        elif scene ==6:
            self.main_label.config(text="After speaking with the guard, you decide to leave your weapons with one of your members.\n you are invited inside to a great feast. During the feast Unferth, a son of Ecglaf insults you and questions your reputation.")
            self.left_button.config(text="Tell stories of your history")
            self.right_button.config(text="Show him your strength")

        elif scene ==7:
            self.main_label.config(text="You tell stories about your strength and valor, and tell Unferth that your reputaion was hard-earned.\n"+
            "After the feast is over, You notice the hall-guards asleep at their posts. then suddently,\n you see the beast. Grendel. He grabs a man and bites into him, "+
            "eating him from head to toe.\n Before you know it, you are standing before the monster. Grendel raises a talon to attack you...")
            self.left_button.config(text="Overpower Grendel with\nbrute force")
            self.right_button.config(text="Scramble to grab\nyour weapon")

        elif scene ==8:
            self.main_label.config(text="You lock with Grendel in a show of sheer strength. After what feels like several minutes, everyone in the hall\n hears a screech of defeat as "+
            "you completely rim Grendels arm of and slay the beast. \nAfter the battle, you are proclaimed as a hero and another great feast is held the day after. Once the second feast \n"+
            "is over, you decide to sleep at: ")
            self.left_button.config(text="Lodging within the town")
            self.right_button.config(text="The king's hall - Heorot")

        elif scene ==9:
            self.main_label.config(text="After a few hours of sleep, you are awoken in a hurry. Grendel's mother has made an attack of revenge against Heorot! There are few survivors. \n"+
            "You are asked to help defeat the new beast that threatens Heorot. What do you do?:")
            self.left_button.config(text="Walk away from the fight")
            self.right_button.config(text="Go hunting for the beast")

        elif scene ==10:
            self.main_label.config(text="You agree to help defeat this new beast. This beast is stronger and more powerful than Grendel, \nand seeking revenge. How do you prepare for this upcoming fight?")
            self.left_button.config(text="Rely upon your strength")
            self.right_button.config(text="Gear up with your\nweapons and armor")

        elif scene ==11:
            self.main_label.config(text="You don your war-gear and equip your sword, Hrunting. You, your party, and the kings men track Grendel's\n mother to a lake in the woods, where "+
            "you believe she is hiding under the water.\n You dive underwater, and while swimming downward, a massive hand grabs you and brings you down further. You realize that it was \n"+
            "Grendel's mother who grabbed you and dragged you into her lair.\n As you begin to fight gredel, you lose grip of your weapon. What do you do?:")
            self.left_button.config(text="Find another\nweapon to use")
            self.right_button.config(text="Look for a\nweak spot to hit")

        elif scene ==12:
            self.main_label.config(text="You grab the closest weapon and wildly swing it at the beast with your god-like strength. With a few hits,\n you manage to destroy the beast. After a while, "+
            "you leave the beast's lair,\n and arrive above the lake with the rest of the group. From that day on you are proclaimed\n as one of the greatest heros in the lands.\n\nTHE END.")
            self.left_button.config(text="The End.")
            self.right_button.config(text="The story isn't\ngood enough...")

        elif scene == -10:
            self.main_label.config(text="How is my story not good enough? I worked so hard making this! So many hours spent! This is as good as I could get it!")
            self.left_button.config(text="I'm sorry")
            self.right_button.config(text="No, it needs to be better")

        elif scene == -20:
            self.main_label.config(text="Well I don't know how it could get better! If you think you could do better how about you make your own program... \n" +
                                       "wait... that might just be the key! You can write your own story! Unfortunately the creator of this app was too lazy to add \n" +
                                       " a textbox so we will just have to work with what we got. Alright, here's the plan, you make the story in your head, and \n" +
                                        "then you can tell me about it through the buttons. So to start, imagine the opening of the game. What kind of story will it be?")
            self.left_button.config(text="It is a sad story")
            self.right_button.config(text="it is an awesome story")

        elif scene == -21:
            self.main_label.config(text="Okay. Now image the characters in your story. Think of the experiences they go through in this story. \n" +
                                   "think about the pain, the heartbreak, and how the story concludes. Was it a story worth imagining?")
            self.left_button.config(text="Yes")
            self.right_button.config(text="No")


        elif scene == -30:
            self.main_label.config(text="An awesome adventure... yes, grand stories and glories, the stories of legends. Now think about the characters, who \n"+
                                   "they are, and what they've accomplished. What do they look like?")
            self.left_button.config(text="His name is Bewulf. The strongest adventurer ever")
            self.right_button.config(text="His name is Gawaywan the green knight. \nHe is a noble knight, but he has a funny name.")



if __name__ == '__main__':
    MainGUI = mainGUI()

