print("It's late, the library is eerily quiet, and you, a diligent student, are the last one left, surrounded by towering stacks of forgotten tales. You were just about to pack up your books when you heard it, a faint, metallic clink from the restricted 'Ancient Manuscripts' section. Your heart pounds. This isn't just a quiet night of studying anymore; it's a Mystery at the Library waiting to unfold...")
print("What would you like to do?")
print("Type 'a' if you would like to enter the Ancient Manuscripts section")
print("Type 'b' if you would like to go home")
print("Type 'c' if you would like to stay and study")

proceed=False
enter=False
study=False
while proceed==False:
    proceed=True
    choice=input()
    if(choice=="a"): #Enter manuscripts section
        print("You walk slowly into the dusty section of the library, the books on the shelves leaking age and smelling of mystery.")
        enter=True
        print("What would you like to do?")
        print("Type 'a' if you would like to take a book from the shelves.")
        print("Type 'b' if you would like to continue deeper into the restricted section")
    elif(choice=="b"):#Go Home
        print("You decide not to enter. It's late after all, and that area is restricted anyway. You walk home through the quiet night, reaching your home and opening the door to the warm comfort of everyday life.")
        print("Ending 0:Hometime")
    elif(choice=="c"): #Stay and Study
        print("You decide to continue your studying. The adrenaline rush from the sudden noise having spurred you on with your work. As you continue studying, your pen scratching quietly on the paper, you hear another loud sound. A bang, then a creak of old wood. Someone or something is coming from the Ancient Manuscripts section.")
        study=True
        print("What would you like to do?")
        print("Type 'a' if you would like to run.")
        print("Type 'b' if you would like to investigate.")
        print("Type 'c' if you would like to continue working.")
    else:
        print("Please enter one of the following.")
        print("Type 'a' if you would like to enter the Ancient Manuscripts section")
        print("Type 'b' if you would like to go home")
        print("Type 'c' if you would like to stay and study")
        proceed=False

book=False
proceed=False
if(enter==True):
    while(proceed==False):
        proceed=True
        choice=input()
        if choice=="a": #Take Book
            print("You pick a book at random from the shelves. It has a brown cover, though you can tell it was once a vibrant red. Opening the leather cover, you begin reading and find.. secret truths of reality! They are almost impossible to understand but you can tell straight away that these are revoloutionary ideas.")
            print("What would you like to do?")
            print("Type 'a' if you would like to leave.")
            print("Type 'b' if you would like to steal the book.")
            print("Type 'c' if you would like to read more.")
            book=True
        elif choice=="b": #Deeper into corridor
            print("You slowly step down the corridor into the darkness. The floorboards creak at every step, echoing through the strange space. Eventually, you stop, confused. Was this section always this big? Looking behind you, your eyes widen as you see the familiar walls of the library, old and sturdy. You begin to panic. There is no way back, only a way deeper into the corridor. Not knowing what else to do, you continue down the corridor, however every time you look back, the wall is right behind you. This is it. Trapped forever...")
            print("Ending 4:Unending Corridor")
        else:
            print("Please enter one of the following.")
            print("Type 'a' if you would like to take a book from the shelves.")
            print("Type 'b' if you would like to continue deeper into the restricted section")
            proceed=False

proceed=False
if(book==True):
    while(proceed==False):
        proceed=True
        choice=input()
        if(choice=="a"): #Leave
            print("You decide that leaving is the best idea. This place is clearly somewhere you shouldn't be and deals with matters far greater than your place. Finding your way back into the main area of the library, you make your way home throught the dark night. Although you continue your normal, happy life, your mind always wanders back to what you could have known should you have taken a different course.")
            print("Ending 2:Regret")
        elif(choice=="b"): #Steal book
            print("You decide this book contains secrets that the world should know. Maybe you could become rich or famous from revealing this knowledge! You walk back out to the main section of the library, holding the ancient book. However the door is locked. You cannot find a way to open it, so you search for other ways outside. You go to a window but before you can think about climbing through, you notice the world outside seems.. wrong. The nice garden that can usually be seen is overgrown and messy, full of strangely-coloured greenery. The sky is dark and clear, yet it seems to swirl above you threateningly. You don't know where this is, but it's clearly not your hometown. And who knows if you'll ever find a way back.")
            print("Ending 3:Homesick")
        elif(choice=="c"): #Further Reading
            print("You decide to continue reading, wanting to know of great matters beyond what you could once comprehend. Before you realise it, there's a stack of books beside you that you have read, and so many more shelves to go. The knowledge draws you in, trapping you with it's objective truths. Many hours pass and your body eventually collapses, halting your ability to keep reading. At this moment, a creature, shrouded in darkness approaches you.")
            print("'Become the new librarian and you can continue reading.'")
            print("Desperate for more knowledge, you muster a nod and it reaches down to press a limb to your head. A desolate darkness covers your vision completely and you close your eyes so as not to overwhelm yourself with the darker than black colour. When you open them again, the creature is gone and you have forever changed. Your body is impossibly dark and your limbs are formless. Your existence does not make sense, yet you understand your purpose perfectly. Read, keep reading, hoard all the knowledge you can into your brain. And when you've taken everything in, open the section once again to find a new librarian. Once this task is done, you will disappear, all the time you spent rendered meaningless as the cycle repeats.")
            print("Ending 7:Knowledge Addiction")
        else:
            print("Please enter one of the following.")
            print("Type 'a' if you would like to leave.")
            print("Type 'b' if you would like to steal the book.")
            print("Type 'c' if you would like to read more.")

investigate=False
proceed=False
if(study==True):
    while(proceed==False):
        proceed=True
        choice=input()
        if(choice=="a"): #Run from noise
            print("The strange sounds finally freak you out enough to decide it's better to fail the upcoming test and run now. You flee the library, coming out onto the familiar empty moonlit street and run home.")
            print("Ending 1:Past Hometime")
        elif(choice=="b"): #Investigate noise
            print("You decide you can't focus with these noises and investigate what causes them. Approaching the Ancient Manuscripts section, you come across a dark being in the shadows. It has clearly noticed you, but it does not advance.")
            print("What would you like to do?")
            print("Type 'a' if you would like to run.")
            print("Type 'b' if you would like to attempt to talk to the creature")
            print("Type 'c' if you would like to stare at the creature.")
            investigate=True
        elif(choice=='c'): #Continue studying
            print("You stubbornly refuse to be distracted by the unsettling noise. Your heart beats hard as you focus on the paper in front of you, doing your best to block out your feelings with your pen. The creaking gets louder. A tapping sound starts. The sound of a page turns. And you can no longer study, for you are enclosed in an empty darkness, never to see the light again.")
            print("Ending 5:Void")
        else:
            print("Please enter one of the following.")
            print("Type 'a' if you would like to run.")
            print("Type 'b' if you would like to investigate.")
            print("Type 'c' if you would like to continue working.")
            proceed=False

proceed=False
if(investigate==True):
    while(proceed==False):
        proceed=True
        choice=input()
        if(choice=="a"): #Run from creature
            print("Your fight or flight kicks in and you run as fast as your legs can take you. That creature is unnatural and you know you need to get away. Focused solely on escape, you reach the door to the library and yank it open. But all that awaits you on the other side of the threshold is the creature you fled from. You weren't supposed to be here this late and it isn't about to let you leave so easily. The price must be paid, and paying it leaves you changed forever. At some point you find yourself walking back home, but you feel numb, both body and mind. Are you still you?")
            print("Ending 6:Price Paid")
        elif(choice=='b'): #Talk to creature
            print("You open your mouth to speak to the creature but your words do not come out. Instead, your breath is stolen and you can almost hear a voice in your mind: 'Quiet in the library'. Your eyes refocus on the creature in front of you as it's unformed limb pats you on the head with a crushing gravity. It then leads deeper into the library and you are seemingly forced by your own mind to follow it. It takes you deep inside the restricted section, where it hands you a book from the shelves. You begin to read and are soon engulfed by an unshakable thirst for the knowledge it provides. Before you know it, you have finished the book and are silently begging the creature for more knowledge. It makes an offer you are incapable of refusing: ")
            print("'Become the new librarian and you can continue reading.'")
            print("Desperate for more knowledge, you nod and it presses a limb to your head once again. However this time, a desolate darkness covers your vision completely and you close your eyes so as not to overwhelm yourself with the darker than black colour. When you open them again, the creature is gone and you have forever changed. Your body is impossibly dark and your limbs are formless. Your existence does not make sense, yet you understand your purpose perfectly. Read, keep reading, hoard all the knowledge you can into your brain. And when you've taken everything in, open the section once again to find a new librarian. Once this task is done, you will disappear, all the time you spent rendered meaningless as the cycle repeats.")
            print("Ending 8:Unbidden Knowledge Addiction")
        elif(choice=='c'): #Stare at creature
            print("You stare at the creature. If it won't advance on you, why would you need to do anything else? You stay unblinking for as long as you can, but eventually, your watery eyes close for a short time. The creature is still there in front of you, unmoving. You take deep breaths to calm your heart; if it doesn't matter whether you blink or not, you can relax. The more time you spend looking at the creature, the more relaxed you feel. You begin to get bored after minutes of staring in silence. To stave off said boredom, you start to trace the creature's dark outline to understand it's form, but the more you watch, the more confused you are. Your brain cannot parse the information you are attempting to take in and you quickly get a headache. The creature places one of it's impossible limbs on your head, as if to calm you but it only makes your brain try harder to understand, making the headache worse. You close your eyes, trying to stop thinking about it, but once you've started, you cannot stop. The creature's pure existence is too much for you and your consciousness fades.")
            print("Ending 9:Feeble Mind")
        else:
            print("Please enter one of the following.")
            print("Type 'a' if you would like to run.")
            print("Type 'b' if you would like to attempt to talk to the creature")
            print("Type 'c' if you would like to stare at the creature.")