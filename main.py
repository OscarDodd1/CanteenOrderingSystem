#Variables
firstName = None
lastName = None
askedName = False

menu = {
    "item1": 5.30,
    "item2": 2.99,
    "item3": 4.50
}

discountThreshold = 10
discountAmount = 1.1

#Functions
def Ask_Name():
    global askedName

    while askedName != True:
        firstName = input("First Name: ")
        lastName = input("Last Name: ")

        correct = input("Your name is " + firstName + " " + lastName + ", Correct? (y/n) ")

        if correct.lower() == "y":
            askedName = True
        else:
            askedName = False
#Main
Ask_Name()