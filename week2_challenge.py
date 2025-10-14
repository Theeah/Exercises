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
    if(choice=="a"):
        print("You walk slowly into the dusty section of the library, the books on the shelves leaking age and smelling of mystery.")
        enter=True #done.
        print("What would you like to do?")
        print("Type 'a' if you would like to take a book from the shelves.")
        print("Type 'b' if you would like to continue deeper into the restricted section")
    elif(choice=="b"):
        print("You decide not to enter. It's late after all, and that area is restricted anyway. You walk home through the quiet night, reaching your home and opening the door to the warm comfort of everyday life.")
        print("Ending 0:Hometime")
    elif(choice=="c"):
        print("You decide to continue your studying. The adrenaline rush from the sudden noise having spurred you on with your work. As you continue studying, your pen scratching quietly on the paper, you hear another loud sound. A bang, then a creak of old wood. Someone or something is coming from the Ancient Manuscripts section.")
        study=True #Not done
        print("What would you like to do?")
        print("Type 'a' if you would like to run.") #Good end.
        print("Type 'b' if you would like to investigate.") #Interesting bad end.
        print("Type 'c' if you would like to continue working.") #Stubbornly refuse to stop, bad end.
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
        if choice=="a":
            print("You pick a book at random from the shelves. It has a brown cover, though you can tell it was once a vibrant red. Opening the leather cover, you begin reading and find.. secret truths of reality! They are almost impossible to understand but you can tell straight away that these are revoloutionary ideas.")
            print("What would you like to do?")
            print("Type 'a' if you would like to leave.")
            print("Type 'b' if you would like to steal the book.")
            print("Type 'c' if you would like to read more.")
            book=True
        elif choice=="b":
            print("You slowly step down the corridor into the darkness. The floorboards creak at every step, echoing through the strange space. Eventually, you stop, confused. Was this section always this big? Looking behind you, your eyes widen as you see the familiar walls of the library, old and sturdy. You begin to panic. There is no way back, only a way deeper into the corridor. Not knowing what else to do, you continue down the corridor, however every time you look back, the wall is right behind you. This is it. Trapped forever...")
            print("Ending 2:Unending Corridor")
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
        if(choice=="a"):
            print("You decide that leaving is the best idea. This place is clearly somewhere you shouldn't be and deals with matters far greater than your place. Finding your way back into the main area of the library, you make your way home throught the dark night. Although you continue your normal, happy life, your mind always wanders back to what you could have known should you have taken a different course.")
            print("Ending 1:Regret")
        elif(choice=="b"):
            print("You decide this book contains secrets that the world should know. Maybe you could become rich or famous from revealing this knowledge! You walk back out to the main section of the library, holding the ancient book. However the door is locked. You cannot find a way to open it, so you search for other ways outside. You go to a window but before you can think about climbing through, you notice the world outside seems.. wrong. The nice garden that can usually be seen is overgrown and messy, full of strangely-coloured greenery. The sky is dark and clear, yet it seems to swirl above you threateningly. You don't know where this is, but it's clearly not your hometown. And who knows if you'll ever find a way back.")
            print("Ending 3:Homesick")
        elif(choice=="c"):
            print("You decide to continue reading, wanting to know of great matters beyond what you could once comprehend. Before you realise it, there's a stack of books beside you that you have read, and so many more shelves to go. The knowledge draws you in, trapping you with it's objective truths. Many hours pass and your body eventually collapses, halting your ability to keep reading. At this moment, a creature, shrouded in darkness approaches you. 'Become the new librarian and you can continue reading.' Desperate for more knowledge, you muster a nod and it reaches down to press a limb to your head. A desolate darkness covers your vision completely and you close your eyes so as not to overwhelm yourself with the darker than black colour. When you open them again, the creature is gone and you have forever changed. Your body is impossibly dark and your limbs are formless. Your existence does not make sense, yet you understand your purpose perfectly. Read, keep reading, hoard all the knowledge you can into your brain. And when you've taken everything in, open the section once again to find a new librarian. Once this task is done, you will disappear, all the time you spent rendered meaningless as the cycle repeats.")
            print("Ending 4:Knowledge Addiction")
        else:
            print("Please enter one of the following.")
            print("Type 'a' if you would like to leave.")
            print("Type 'b' if you would like to steal the book.")
            print("Type 'c' if you would like to read more.")