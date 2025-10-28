#Global Variables
foodList=[]

class food:
    def __init__(self,foodID,foodType,open,useBy,usagesLeft):
        self.ID=foodID
        self.type=foodType
        self.open=open
        self.useByDate=useBy
        self.usagesLeft=usagesLeft

def generateID(): #Generates a new ID based on the ID of the last item in the list
    id="-1"

    try:
        index=len(foodList)
        if(index==0):
            id="00"
        else:
            lastItem=foodList[index-1]
            lastItemList=lastItem.split(',')
            id=int(lastItemList[0])+1


            if(id<10):
                id=str(id)
                id=("0"+id)
            else:
                id=str(id)

    except:
        raise Exception

    print(id)
    return id

def inpUseDate(): #Used when adding an item. Gets the user to input the useByDate.
    print("What is the use by date of the food item?")
    useByDate=input() #Make sensible to input.
    #Validation
    return useByDate

def inpUsages(): #Used when adding an item. Gets the user to input the number of usages.
    print("How many meals will the item last?")
    usages=input()
    try:
        usages=int(usages)
    except:
        print("Please input a whole number.")
        usages=-1
    return usages

def inpType(): #Used when adding an item. Gets the user to choose which type of food the new item is.
    print("What type of item would you like to add?")
    print("[1] Protein")
    print("[2] Vegetables")
    print("[3] Cheese")
    choice=input()
    foodType=""
    if(choice=="1"):
        foodType="Protein"
    elif(choice=="2"):
        foodType="Vegetables"
    elif(choice=="3"):
        foodType="Cheese"
    else:
        print("Please input the number indicating the type of food.")
        foodType="fail"
    return foodType

def foodShoppingCalcChat(): #Calculates the number of full meals remaining and what is leftover after that number of meals has been consumed.
    protein=0
    cheese=0
    veg=0
    for foodItem in foodList:
        if(foodItem.type=="Protein"):
            protein=protein+foodItem.usages
        elif(foodItem.type=="Vegetables"):
            veg=veg+foodItem.usages
        else:
            cheese=cheese+foodItem.usages
    
    lowest=""
    if(protein<cheese):
        if(protein<veg):
            lowest=protein
        else:
            lowest=veg
    else:
        if(cheese<veg):
            lowest=cheese
        else:
            lowest=veg
    
    print(f"You have {lowest} full meals")
    if((protein-lowest)>0):
        print(f"You have {(protein-lowest)} meals worth of protein leftover.")
    if((veg-lowest)>0):
        print(f"You have {veg-lowest} meals worth of vegetables leftover.")
    if((cheese-lowest)>0):
        print(f"You have {cheese-lowest} meals worth of cheese leftover.")
    
    print("Good luck with your shopping trip!")

def addItemChat(): #Activates when the user decides to add a new food item.
    type=inpType()
    while(type=="fail"): #Repeat if they input a non-option
        type=inpType()
    
    useByDate=inpUseDate()

    usages=inpUsages() #Repeat if they input a non-integer
    while(usages==-1):
        usages=inpUsages()
    
    id=generateID()
    
    foodString=(id+","+type+",False,"+useByDate+","+str(usages))

    foodList.append(foodString)

def endChat(): #After an action is performed, will see if the user has finished with the foodTracker or not.
    print("Would you like to perform another action?")
    print("[1] Yes")
    print("[2] No")
    choice=input()
    if(choice=="1"):
        chatBotStart()
    elif(choice=="2"):
        print("Thank you for using foodTracker.")
    else:
        print("Command not found. Ending chat.")

def chatBotStart(): #'Main Menu' of the chat bot. Decide what action to take.
    print("---------------------------------------")
    print("What action would you like to take?")
    print("[1] Add a food item")
    print("[2] Decrease the usages on a food item")
    print("[3] Generate food shopping information")
    print("[4] Exit")
    print("---------------------------------------")
    
    option=input()
    if(option=="1"):
        addItemChat()
        endChat()
    elif(option=="3"):
        foodShoppingCalcChat()
        endChat()
    elif(option=="4"):
        print("Thank you for using foodTracker.") #Ends chat. endChat() is not called here because then it would double check if they want to exit.
    else:
        print("Sorry, command not found.")
        endChat()
    
    

#Start
chatBotStart()