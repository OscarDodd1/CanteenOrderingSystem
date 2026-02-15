#Variables
firstName = None
lastName = None
askedName = False
userOrder = []

statOrder = "https://deepwoken.co/builder?31=XZtuNnE3 45 Agility ( get swift rebound, evasive expert, risky moves then finally ghost and speed demon ) | 40 Strength ( get Precise swing, Spinecutter, Steady nerves, Bulldozer and unwavering resolve ) | 55 Charisma ( get charmcaster first which will allow you to obtain tough love then chaotic charm and lasting  charisma ) | 4 Fortitude, 1 Willpower, 1 medium weapons (this will allow shrine of order to put stats into these points, also 4 fort because gremor) 𝖲𝖧𝖱𝖨𝖭𝖤 𝖮𝖥 𝖮𝖱𝖣𝖤𝖱 (Use shrine of blasphemy first if missing ghost or any important talents) 40 willpower ( for exhaustion strike mantra and neuroplasticity ) | 50 Fortitude ( Most important things in are: exoskeleton, to the finish, battle tendency, braced collapse, moving fortress and perserverance ) | 50 Gale (3 star gale mantras) | 90 Fortitude ( Reinforced armour ) | 75 Galebreath (max gale until uncapped) | 40 medium weapons (For curved blade of winds requirement) | Kill a boss then get 88 Galebreath (88 not 80 because of remaining points)"

menu = {
    "Item1" : 5.00,
    "Item2" : 3.50,
    "Item3" : 2.00
}

menuList = list(menu.keys())

discountThreshold = 10
discountAmount = 1.1

#Functions
def Ask_Name():
    
    global askedName

    while askedName != True:
        firstName = input("First Name: ")
        lastName = input("Last Name: ")

        correct = input("Your name is " + firstName + " " + lastName + ", Correct? (y/n): ")

        if correct.lower() == "y":
            askedName = True
        else:
            askedName = False

def Order_Items():
    global firstName
    global lastName
    global userOrder

    completedOrder = False

    print("\n-----Menu-----")
    for i, item in enumerate(menu):
        print(f"{i + 1} - {item} (${menu[item]})")
    print("--------------")

    while completedOrder == False:
        newItem = input("Input item number (input nothing to complete order): ")

        if newItem == "":
            cost = 0

            print("\n-----Order-----")
            for ii, uItem in enumerate(userOrder):
                print(f"-{uItem} (${menu[uItem]})")
                cost += menu[uItem]
            print("---------------")
            print(f"Total Cost: ${cost}")
            print("---------------")

            orderCheck = input("Is this order correct (y/n): ")

            if orderCheck.lower() == "y":
                completedOrder = True
            else:
                userOrder = []
                print("Removed all items from cart")
        else:
            uCost = 0

            try:
                menuItem = menuList[int(newItem) - 1]

                userOrder.insert(0, menuItem)
                print("\n-----Order-----")
                for iii, uuItem in enumerate(userOrder):
                    print(f"-{uuItem} (${menu[uuItem]})")
                    uCost += menu[uuItem]
                print("---------------")
                print(f"Total Cost: ${uCost}")
                print("---------------")
            except:
                print("\n---Unknown item---\n")

#Main
Ask_Name()
Order_Items()