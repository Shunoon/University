class Node:
    def __init__(self, value=None, next=None):
        self.value = value # head is the node from which your are pointing towards next node
        self.next = next # next is the next node where pointer is pointing

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, element):
        node = Node(element, self.head)
        self.head = node
        
    def insert_at_end(self, element):
        if self.head is None:
            node = Node(element, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(element, None)

    def print(self):
        itr = self.head
        linked_list = ''
        while itr:
            linked_list += str(itr.value) + " "
            itr = itr.next
        print(linked_list)
        
    def length(self):
        itr = self.head
        count = 0  
        while itr:
            count += 1  
            itr = itr.next
        return count
        
    def value_at(self, index):
        itr = self.head
        count = 0
        value = ''  
        while itr:
            if count == index:
                value = itr.value
            count += 1
            itr = itr.next
        return value
        
    def replace_at(self, index, element):
        if self.head is None:
            print("linked list is empty")
            return
        if index > (self.length()-1):
            print("index is out of range")
            return
        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.value = element
                break
            itr = itr.next
            count += 1

# Declaring the quanitity as 0 of the island A storages at the beginning.
islandA = LinkedList()
islandA.insert_at_end(0)
islandA.insert_at_end(0)
islandA.insert_at_end(0)
islandA.insert_at_end(0)
islandA.insert_at_end(0)
islandA.insert_at_end(0)

# Declaring the quanitity as 0 of the island B storages at the beginning.
islandB = LinkedList()
islandB.insert_at_end(0)
islandB.insert_at_end(0)
islandB.insert_at_end(0)
islandB.insert_at_end(0)
islandB.insert_at_end(0)
islandB.insert_at_end(0)

# Declaring the quanitity as 0 of the island C storages at the beginning.
islandC = LinkedList()
islandC.insert_at_end(0)
islandC.insert_at_end(0)
islandC.insert_at_end(0)
islandC.insert_at_end(0)
islandC.insert_at_end(0)
islandC.insert_at_end(0)

# Declaring the quanitity as 0 of the island D storages at the beginning.
islandD = LinkedList()
islandD.insert_at_end(0)
islandD.insert_at_end(0)
islandD.insert_at_end(0)
islandD.insert_at_end(0)
islandD.insert_at_end(0)
islandD.insert_at_end(0)

# Declaring the quanitity as 0 of the dhoani storages at the beginning.
dhoani = LinkedList()
dhoani.insert_at_end(0)
dhoani.insert_at_end(0)
dhoani.insert_at_end(0)
dhoani.insert_at_end(0)

# Declaring the total capacity of the storages in island A
islandAcapacity = LinkedList()
islandAcapacity.insert_at_end(1500)
islandAcapacity.insert_at_end(40)
islandAcapacity.insert_at_end(50)
islandAcapacity.insert_at_end(100)
islandAcapacity.insert_at_end(10000)
islandAcapacity.insert_at_end("Unlimited")

# Declaring the total capacity of the storages in island B
islandBcapacity = LinkedList()
islandBcapacity.insert_at_end(2000)
islandBcapacity.insert_at_end(40)
islandBcapacity.insert_at_end(50)
islandBcapacity.insert_at_end(90)
islandBcapacity.insert_at_end(11000)
islandBcapacity.insert_at_end("Unlimited")

# Declaring the total capacity of the storages in island C
islandCcapacity = LinkedList()
islandCcapacity.insert_at_end(1000)
islandCcapacity.insert_at_end(40)
islandCcapacity.insert_at_end(50)
islandCcapacity.insert_at_end(110)
islandCcapacity.insert_at_end(9000)
islandCcapacity.insert_at_end("Unlimited")

# Declaring the total capacity of the storages in island D
islandDcapacity = LinkedList()
islandDcapacity.insert_at_end(1000)
islandDcapacity.insert_at_end(40)
islandDcapacity.insert_at_end(50)
islandDcapacity.insert_at_end(80)
islandDcapacity.insert_at_end(9000)
islandDcapacity.insert_at_end("Unlimited")

# Declaring the total capacity of the storages in island A
dhoanicapacity = LinkedList()
dhoanicapacity.insert_at_end(4000)
dhoanicapacity.insert_at_end(40)
dhoanicapacity.insert_at_end(50)
dhoanicapacity.insert_at_end(28000)

exceed1 = ("\nAmount exceeds storage capacity of the island A or dhoani does not have that amount, please try again.\n")
exceed2 = ("\nAmount exceeds storage capacity of the island B or dhoani does not have that amount, please try again.\n")
exceed3 = ("\nAmount exceeds storage capacity of the island C or dhoani does not have that amount, please try again.\n")
exceed4 = ("\nAmount exceeds storage capacity of the island D or dhoani does not have that amount, please try again.\n")
exceed5 = ("\nAmount exceeds storage capacity of the dhoani, please try again.\n")

exceed6 = ("\nAmount exceeds storage capacity of the dhoani or island A does not have that amount, please try again.\n")
exceed7 = ("\nAmount exceeds storage capacity of the dhoani or island B does not have that amount, please try again.\n")
exceed8 = ("\nAmount exceeds storage capacity of the dhoani or island C does not have that amount, please try again.\n")
exceed9 = ("\nAmount exceeds storage capacity of the dhoani or island D does not have that amount, please try again.\n")

def mainMenu():
    print("\n", "***** WELCOME TO THE PROGRAM *****", "\n")

    print("[1] Check the storage capacities of islands and dhoani", "\n")

    print("[2] Current quantity in storage of islands and dhoani", "\n")

    print("[3] Add items in island A")
    print("[4] remove items in island A", "\n")

    print("[5] Add items in island B")
    print("[6] remove items in island B", "\n")

    print("[7] Add items in island C")
    print("[8] remove items in island C", "\n")

    print("[9] Add items in island D")
    print("[10] remove items in island D", "\n")

    print("[11] Add items in Dhoani", "\n")

    print("[12] Timings of islands", "\n")

    print("[0] Exit the program.")
    while True:
            print("")
            option = int(input("Enter your option "))
            if option == 1:
                menu1()
                break
            if option == 2:
                menu2()
                break
            elif option == 3:
                addIslandA()
                break
            elif option == 4:
                removeIslandA()
                break
            elif option == 5:
                addIslandB()
                break
            elif option == 6:
                removeIslandB()
                break
            elif option == 7:
                addIslandC()
                break
            elif option == 8:
                removeIslandC()
                break
            elif option == 9:
                addIslandD()
                break
            elif option == 10:
                removeIslandD()
                break
            elif option == 11:
                dhoani_properties()
                break
            elif option == 12:
                timings()
                break
            elif option == 0:
                print("You have exited the program !")
                break
            else:
                print("Inavlid choice. Enter between 0 - 9")
                mainMenu()
            print("Inavlid choice. Enter between 0 - 9")
    exit

# Function which shows the user all the storage capacities
def menu1():
    print("")
    print("---- STORAGE CAPACITY AT ISLAND A ----")
    print("Diesel = ", (1500))
    print("Frozen food = ", (40))
    print("Low temp food = ", (50))
    print("Other food = ", (100))
    print("Protected material = ", (10000))
    print("Unprotected material = ", "Unlimited", "\n")

    print("---- STORAGE CAPACITY AT ISLAND B ----")
    print("Diesel = ", (2000))
    print("Frozen food = ", (40))
    print("Low temp food = ", (50))
    print("Other food = ", (90))
    print("Protected material = ", (11000))
    print("Unprotected material = ", "Unlimited", "\n")

    print("---- STORAGE CAPACITY AT ISLAND C ----")
    print("Diesel = ", (1000))
    print("Frozen food = ", (40))
    print("Low temp food = ", (50))
    print("Other food = ", (110))
    print("Protected material = ", (9000))
    print("Unprotected material = ", ("Unlimited"), "\n")

    print("---- STORAGE CAPACITY AT ISLAND D ----")
    print("Diesel = ", (1000))
    print("Frozen food = ", (40))
    print("Low temp food = ", (50))
    print("Other food = ", (80))
    print("Protected material = ", (9000))
    print("Unprotected material = ", ("Unlimited"), "\n")

    print("---- STORAGE CAPACITY OF DHOANI ----")
    print("Diesel = ", (4000))
    print("Frozen food = ", (40))
    print("Low temp food = ", (50))
    print("Other food, Protected  material and Unprotected material = ", (28000), "\n")

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

# Function which shows the user the current quantities in islands and dhoani
def menu2():
    print(" ")
    print("---- Current quantity in storage in island A ----", "\n")
    print("Diesel = ", islandA.value_at(0))
    print("Frozen food = ", islandA.value_at(1))
    print("Low temp food = ", islandA.value_at(2))
    print("Other food = ", islandA.value_at(3))
    print("Protected material = ", islandA.value_at(4))
    print("Unprotected material = ", islandA.value_at(5), "\n")

    if islandA.value_at(0) == islandAcapacity.value_at(0) and islandA.value_at(1) == islandAcapacity.value_at(1) and islandA.value_at(2) == islandAcapacity.value_at(2) and islandA.value_at(3) == islandAcapacity.value_at(3) and islandA.value_at(4) == islandAcapacity.value_at(4):
        print("---- ISLAND A CAPACITY IS FULL ----")
    else:
        print("---- Island A still has extra capacity ----")

    print(" ")
    print("---- Current quantity in storage in island B ----", "\n")
    print("Diesel = ", islandB.value_at(0))
    print("Frozen food = ", islandB.value_at(1))
    print("Low temp food = ", islandB.value_at(2))
    print("Other food = ", islandB.value_at(3))
    print("Protected material = ", islandB.value_at(4))
    print("Unprotected material = ", islandB.value_at(5), "\n")

    if islandB.value_at(0) == islandBcapacity.value_at(0) and islandB.value_at(1) == islandBcapacity.value_at(1) and islandB.value_at(2) == islandBcapacity.value_at(2) and islandB.value_at(3) == islandBcapacity.value_at(3) and islandB.value_at(4) == islandBcapacity.value_at(4):
        print("---- ISLAND B CAPACITY IS FULL ----")
    else:
        print("---- Island B still has extra capacity ----")

    print(" ")
    print("---- Current quantity in storage in island C ----", "\n")
    print("Diesel = ", islandC.value_at(0))
    print("Frozen food = ", islandC.value_at(1))
    print("Low temp food = ", islandC.value_at(2))
    print("Other food = ", islandC.value_at(3))
    print("Protected material = ", islandC.value_at(4))
    print("Unprotected material = ", islandC.value_at(5), "\n")

    if islandC.value_at(0) == islandCcapacity.value_at(0) and islandC.value_at(1) == islandCcapacity.value_at(1) and islandC.value_at(2) == islandCcapacity.value_at(2) and islandC.value_at(3) == islandCcapacity.value_at(3) and islandC.value_at(4) == islandCcapacity.value_at(4):
        print("---- ISLAND C CAPACITY IS FULL ----")
    else:
        print("---- Island C still has extra capacity ----")

    print(" ")
    print("---- Current quantity in storage in island D ----", "\n")
    print("Diesel = ", islandD.value_at(0))
    print("Frozen food = ", islandD.value_at(1))
    print("Low temp food = ", islandD.value_at(2))
    print("Other food = ", islandD.value_at(3))
    print("Protected material = ", islandD.value_at(4))
    print("Unprotected material = ", islandD.value_at(5), "\n")

    if islandD.value_at(0) == islandDcapacity.value_at(0) and islandD.value_at(1) == islandDcapacity.value_at(1) and islandD.value_at(2) == islandDcapacity.value_at(2) and islandD.value_at(3) == islandDcapacity.value_at(3) and islandD.value_at(4) == islandDcapacity.value_at(4):
        print("---- ISLAND D CAPACITY IS FULL ----")
    else:
        print("---- Island D still has extra capacity ----")

    print(" ")
    print("---- Current quantity in storage in dhoani ----", "\n")
    print("Diesel = ", dhoani.value_at(0))
    print("Frozen food = ", dhoani.value_at(1))
    print("Low temp food = ", dhoani.value_at(2))
    print("Other food, Protected material and Unprotected material = ", dhoani.value_at(3), "\n")

    if dhoani.value_at(0) == dhoanicapacity.value_at(0) and dhoani.value_at(1) == dhoanicapacity.value_at(1) and dhoani.value_at(2) == dhoanicapacity.value_at(2) and dhoani.value_at(3) == dhoanicapacity.value_at(3):
        print("---- DHOANI CAPACITY IS FULL ----")
    else:
        print("---- Dhoani still has extra capacity ----")

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

# __________ ISLAND A _________
    
def addIslandA():

# add diesel to island A
    while True:
        data = int(input("How many kilos of diesel do you want to unload from dhoani to island A? "))
        total = data + islandA.value_at(0)
        if total <= islandAcapacity.value_at(0) and data <= dhoani.value_at(0):
            islandA.replace_at(0, total)
            dhoani.replace_at(0, dhoani.value_at(0) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add frozen food to island A
    while True:
        data = int(input("How many kilos of frozen food such as meat would you like unload to Island A? : "))
        total = data + islandA.value_at(1)
        if total <= islandAcapacity.value_at(1) and data <= dhoani.value_at(1):
            islandA.replace_at(1, total)
            dhoani.replace_at(1, dhoani.value_at(1) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add low temp foods to island A
    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like unload to Island A? : "))
        total = data + islandA.value_at(2)
        if total <= islandAcapacity.value_at(2) and data <= dhoani.value_at(2):
            islandA.replace_at(2, total)
            dhoani.replace_at(2, dhoani.value_at(2) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add other food items to island A
    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like unload to Island A? : "))
        total = data + islandA.value_at(3)
        if total <= islandAcapacity.value_at(3) and data <= dhoani.value_at(3):
            islandA.replace_at(3, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add protected materials to island A
    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like unload to Island A? : "))
        total = data + islandA.value_at(4)
        if total <= islandAcapacity.value_at(4) and data <= dhoani.value_at(3):
            islandA.replace_at(4, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)
            
# add unprotected materials to island A
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like unload to Island A? : "))
        total = data + islandA.value_at(5)
        if type(data) == int and data <= dhoani.value_at(3):
            islandA.replace_at(5, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print("Amount is invalid. Try again.")

    print(" ")
    print("Total kilos in island A")
    print("Diesel = ", islandA.value_at(0))
    print("Frozen food = ", islandA.value_at(1))
    print("Low temp food = ", islandA.value_at(2))
    print("Other food = ", islandA.value_at(3))
    print("Protected material = ", islandA.value_at(4))
    print("Unprotected material = ", islandA.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

def removeIslandA():

# remove and swap diesel in island A
    while True:
        data = int(input("How many kilos of diesel do you want to remove from island A and put it in dhoani? "))
        total = islandA.value_at(0) - data
        if data <= islandA.value_at(0) and data <= dhoanicapacity.value_at(0):
            islandA.replace_at(0, total)
            dhoani.replace_at(0, dhoani.value_at(0) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap diesel in island A
    while True:
        data = int(input("How many kilos of frozen food such as meat would you like to remove from Island A and put it in dhoani?"))
        total = islandA.value_at(1) - data
        if data <= islandA.value_at(1) and data <= dhoanicapacity.value_at(1):
            islandA.replace_at(1, total)
            dhoani.replace_at(1, dhoani.value_at(1) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap low temp foods in island A
    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like to remove from Island A and put it in dhoani?"))
        total = islandA.value_at(2) - data
        if data <= islandA.value_at(2) and data <= dhoanicapacity.value_at(2):
            islandA.replace_at(2, total)
            dhoani.replace_at(2, dhoani.value_at(2) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap other foods in island A
    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like to remove from Island A and put it in dhoani?"))
        total = islandA.value_at(3) - data
        if data <= islandA.value_at(3) and data <= dhoanicapacity.value_at(3):
            islandA.replace_at(3, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap protected materials in island A
    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like to remove from Island A and put it in dhoani?"))
        total = islandA.value_at(4) - data
        if data <= islandA.value_at(4) and data <= dhoanicapacity.value_at(3):
            islandA.replace_at(4, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap unprotected materials
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like to remove from Island A and put it in dhoani?"))
        total = islandA.value_at(5) - data
        if data <= islandA.value_at(5) and data <= dhoanicapacity.value_at(3):
            islandA.replace_at(5, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

    print(" ")
    print("Total kilos in island A")
    print("Diesel = ", islandA.value_at(0))
    print("Frozen food = ", islandA.value_at(1))
    print("Low temp food = ", islandA.value_at(2))
    print("Other food = ", islandA.value_at(3))
    print("Protected material = ", islandA.value_at(4))
    print("Unprotected material = ", islandA.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

# ___________ ISLAND B ____________

def addIslandB():

# add diesel to island B
    while True:
        data = int(input("How many kilos of diesel do you want to unload from dhoani to island B? "))
        total = data + islandB.value_at(0)
        if total <= islandBcapacity.value_at(0) and data <= dhoani.value_at(0):
            islandB.replace_at(0, total)
            dhoani.replace_at(0, dhoani.value_at(0) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add frozen food to island B
    while True:
        data = int(input("How many kilos of frozen food such as meat would you like unload to Island B? : "))
        total = data + islandB.value_at(1)
        if total <= islandBcapacity.value_at(1) and data <= dhoani.value_at(1):
            islandB.replace_at(1, total)
            dhoani.replace_at(1, dhoani.value_at(1) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add low temp foods to island B
    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like unload to Island B? : "))
        total = data + islandB.value_at(2)
        if total <= islandBcapacity.value_at(2) and data <= dhoani.value_at(2):
            islandB.replace_at(2, total)
            dhoani.replace_at(2, dhoani.value_at(2) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add other food items to island B
    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like unload to Island B? : "))
        total = data + islandB.value_at(3)
        if total <= islandBcapacity.value_at(3) and data <= dhoani.value_at(3):
            islandB.replace_at(3, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add protected materials to island B
    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like unload to Island B? : "))
        total = data + islandB.value_at(4)
        if total <= islandBcapacity.value_at(4) and data <= dhoani.value_at(3):
            islandB.replace_at(4, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)
            
# add unprotected materials to island B
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like unload to Island B? : "))
        total = data + islandB.value_at(5)
        if type(data) == int and data <= dhoani.value_at(3):
            islandB.replace_at(5, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print("Amount is invalid. Try again.")

    print(" ")
    print("Total kilos in island B")
    print("Diesel = ", islandB.value_at(0))
    print("Frozen food = ", islandB.value_at(1))
    print("Low temp food = ", islandB.value_at(2))
    print("Other food = ", islandB.value_at(3))
    print("Protected material = ", islandB.value_at(4))
    print("Unprotected material = ", islandB.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

def removeIslandB():

# remove and swap diesel in island B
    while True:
        data = int(input("How many kilos of diesel do you want to remove from island B and put it in dhoani? "))
        total = islandB.value_at(0) - data
        if data <= islandB.value_at(0) and data <= dhoanicapacity.value_at(0):
            islandB.replace_at(0, total)
            dhoani.replace_at(0, dhoani.value_at(0) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap diesel in island B
    while True:
        data = int(input("How many kilos of frozen food such as meat would you like to remove from Island B and put it in dhoani?"))
        total = islandB.value_at(1) - data
        if data <= islandB.value_at(1) and data <= dhoanicapacity.value_at(1):
            islandB.replace_at(1, total)
            dhoani.replace_at(1, dhoani.value_at(1) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap low temp foods in island B
    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like to remove from Island B and put it in dhoani?"))
        total = islandB.value_at(2) - data
        if data <= islandB.value_at(2) and data <= dhoanicapacity.value_at(2):
            islandB.replace_at(2, total)
            dhoani.replace_at(2, dhoani.value_at(2) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap other foods in island B
    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like to remove from Island B and put it in dhoani?"))
        total = islandB.value_at(3) - data
        if data <= islandB.value_at(3) and data <= dhoanicapacity.value_at(3):
            islandB.replace_at(3, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap protected materials in island B
    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like to remove from Island B and put it in dhoani?"))
        total = islandB.value_at(4) - data
        if data <= islandB.value_at(4) and data <= dhoanicapacity.value_at(3):
            islandB.replace_at(4, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap unprotected materials in island B
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like to remove from Island B and put it in dhoani?"))
        total = islandB.value_at(5) - data
        if data <= islandB.value_at(5) and data <= dhoanicapacity.value_at(3):
            islandB.replace_at(5, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

    print(" ")
    print("Total kilos in island B")
    print("Diesel = ", islandB.value_at(0))
    print("Frozen food = ", islandB.value_at(1))
    print("Low temp food = ", islandB.value_at(2))
    print("Other food = ", islandB.value_at(3))
    print("Protected material = ", islandB.value_at(4))
    print("Unprotected material = ", islandB.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()
# ___________ ISLAND C ____________

def addIslandC():

# add diesel to island C
    while True:
        data = int(input("How many kilos of diesel do you want to unload from dhoani to island C? "))
        total = data + islandC.value_at(0)
        if total <= islandCcapacity.value_at(0) and data <= dhoani.value_at(0):
            islandC.replace_at(0, total)
            dhoani.replace_at(0, dhoani.value_at(0) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add frozen food to island C
    while True:
        data = int(input("How many kilos of frozen food such as meat would you like unload to Island C? : "))
        total = data + islandC.value_at(1)
        if total <= islandCcapacity.value_at(1) and data <= dhoani.value_at(1):
            islandC.replace_at(1, total)
            dhoani.replace_at(1, dhoani.value_at(1) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add low temp foods to island C
    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like unload to Island C? : "))
        total = data + islandC.value_at(2)
        if total <= islandCcapacity.value_at(2) and data <= dhoani.value_at(2):
            islandC.replace_at(2, total)
            dhoani.replace_at(2, dhoani.value_at(2) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add other food items to island C
    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like unload to Island C? : "))
        total = data + islandC.value_at(3)
        if total <= islandCcapacity.value_at(3) and data <= dhoani.value_at(3):
            islandC.replace_at(3, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add protected materials to island C
    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like unload to Island C? : "))
        total = data + islandC.value_at(4)
        if total <= islandCcapacity.value_at(4) and data <= dhoani.value_at(3):
            islandC.replace_at(4, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)
            
# add unprotected materials to island C
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like unload to Island C? : "))
        total = data + islandC.value_at(5)
        if type(data) == int and data <= dhoani.value_at(3):
            islandC.replace_at(5, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print("Amount is invalid. Try again.")

    print(" ")
    print("Total kilos in island C")
    print("Diesel = ", islandC.value_at(0))
    print("Frozen food = ", islandC.value_at(1))
    print("Low temp food = ", islandC.value_at(2))
    print("Other food = ", islandC.value_at(3))
    print("Protected material = ", islandC.value_at(4))
    print("Unprotected material = ", islandC.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

def removeIslandC():

# remove and swap diesel in island C
    while True:
        data = int(input("How many kilos of diesel do you want to remove from island C and put it in dhoani? "))
        total = islandC.value_at(0) - data
        if data <= islandC.value_at(0) and data <= dhoanicapacity.value_at(0):
            islandC.replace_at(0, total)
            dhoani.replace_at(0, dhoani.value_at(0) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap diesel in island C
    while True:
        data = int(input("How many kilos of frozen food such as meat would you like to remove from Island C and put it in dhoani?"))
        total = islandC.value_at(1) - data
        if data <= islandC.value_at(1) and data <= dhoanicapacity.value_at(1):
            islandC.replace_at(1, total)
            dhoani.replace_at(1, dhoani.value_at(1) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap low temp foods in island C
    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like to remove from Island C and put it in dhoani?"))
        total = islandC.value_at(2) - data
        if data <= islandC.value_at(2) and data <= dhoanicapacity.value_at(2):
            islandC.replace_at(2, total)
            dhoani.replace_at(2, dhoani.value_at(2) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap other foods in island C
    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like to remove from Island C and put it in dhoani?"))
        total = islandC.value_at(3) - data
        if data <= islandC.value_at(3) and data <= dhoanicapacity.value_at(3):
            islandC.replace_at(3, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap protected materials in island C
    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like to remove from Island C and put it in dhoani?"))
        total = islandC.value_at(4) - data
        if data <= islandC.value_at(4) and data <= dhoanicapacity.value_at(3):
            islandC.replace_at(4, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap unprotected materials in island C
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like to remove from Island C and put it in dhoani?"))
        total = islandC.value_at(5) - data
        if data <= islandC.value_at(5) and data <= dhoanicapacity.value_at(3):
            islandC.replace_at(5, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

    print(" ")
    print("Total kilos in island C")
    print("Diesel = ", islandC.value_at(0))
    print("Frozen food = ", islandC.value_at(1))
    print("Low temp food = ", islandC.value_at(2))
    print("Other food = ", islandC.value_at(3))
    print("Protected material = ", islandC.value_at(4))
    print("Unprotected material = ", islandC.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

# ___________ ISLAND D ____________

def addIslandD():

# add diesel to island D
    while True:
        data = int(input("How many kilos of diesel do you want to unload from dhoani to island D? "))
        total = data + islandD.value_at(0)
        if total <= islandDcapacity.value_at(0) and data <= dhoani.value_at(0):
            islandD.replace_at(0, total)
            dhoani.replace_at(0, dhoani.value_at(0) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add frozen food to island D
    while True:
        data = int(input("How many kilos of frozen food such as meat would you like unload to Island D? : "))
        total = data + islandD.value_at(1)
        if total <= islandDcapacity.value_at(1) and data <= dhoani.value_at(1):
            islandD.replace_at(1, total)
            dhoani.replace_at(1, dhoani.value_at(1) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add low temp foods to island D
    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like unload to Island D? : "))
        total = data + islandD.value_at(2)
        if total <= islandDcapacity.value_at(2) and data <= dhoani.value_at(2):
            islandD.replace_at(2, total)
            dhoani.replace_at(2, dhoani.value_at(2) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add other food items to island D
    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like unload to Island D? : "))
        total = data + islandD.value_at(3)
        if total <= islandDcapacity.value_at(3) and data <= dhoani.value_at(3):
            islandD.replace_at(3, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

# add protected materials to island D
    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like unload to Island D? : "))
        total = data + islandD.value_at(4)
        if total <= islandDcapacity.value_at(4) and data <= dhoani.value_at(3):
            islandD.replace_at(4, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print(exceed1)
            
# add unprotected materials to island D
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like unload to Island D? : "))
        total = data + islandD.value_at(5)
        if type(data) == int and data <= dhoani.value_at(3):
            islandD.replace_at(5, total)
            dhoani.replace_at(3, dhoani.value_at(3) - data)
            print("Amount is valid")
            break
        else:
            print("Amount is invalid. Try again.")

    print(" ")
    print("Total kilos in island D")
    print("Diesel = ", islandD.value_at(0))
    print("Frozen food = ", islandD.value_at(1))
    print("Low temp food = ", islandD.value_at(2))
    print("Other food = ", islandD.value_at(3))
    print("Protected material = ", islandD.value_at(4))
    print("Unprotected material = ", islandD.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

def removeIslandD():

# remove and swap diesel in island D
    while True:
        data = int(input("How many kilos of diesel do you want to remove from island D and put it in dhoani? "))
        total = islandD.value_at(0) - data
        if data <= islandD.value_at(0) and data <= dhoanicapacity.value_at(0):
            islandD.replace_at(0, total)
            dhoani.replace_at(0, dhoani.value_at(0) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap diesel in island D
    while True:
        data = int(input("How many kilos of frozen food such as meat would you like to remove from Island D and put it in dhoani?"))
        total = islandD.value_at(1) - data
        if data <= islandD.value_at(1) and data <= dhoanicapacity.value_at(1):
            islandD.replace_at(1, total)
            dhoani.replace_at(1, dhoani.value_at(1) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap low temp foods in island D
    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like to remove from Island D and put it in dhoani?"))
        total = islandD.value_at(2) - data
        if data <= islandD.value_at(2) and data <= dhoanicapacity.value_at(2):
            islandD.replace_at(2, total)
            dhoani.replace_at(2, dhoani.value_at(2) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap other foods in island D
    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like to remove from Island D and put it in dhoani?"))
        total = islandD.value_at(3) - data
        if data <= islandD.value_at(3) and data <= dhoanicapacity.value_at(3):
            islandD.replace_at(3, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap protected materials in island D
    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like to remove from Island D and put it in dhoani?"))
        total = islandD.value_at(4) - data
        if data <= islandD.value_at(4) and data <= dhoanicapacity.value_at(3):
            islandD.replace_at(4, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

# remove and swap unprotected materials in island D
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like to remove from Island D and put it in dhoani?"))
        total = islandD.value_at(5) - data
        if data <= islandD.value_at(5) and data <= dhoanicapacity.value_at(3):
            islandD.replace_at(5, total)
            dhoani.replace_at(3, dhoani.value_at(3) + data) 
            print("Amount is valid")
            break
        else:
            print(exceed6)

    print(" ")
    print("Total kilos in island D")
    print("Diesel = ", islandD.value_at(0))
    print("Frozen food = ", islandD.value_at(1))
    print("Low temp food = ", islandD.value_at(2))
    print("Other food = ", islandD.value_at(3))
    print("Protected material = ", islandD.value_at(4))
    print("Unprotected material = ", islandD.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

# ___________ DHOANI ____________

def dhoani_properties():

    while True:
        data = int(input("How many kilos of diesel do you want to load to Dhoani? "))
        total = data + dhoani.value_at(0)
        if total <= dhoanicapacity.value_at(0):
            dhoani.replace_at(0, total)
            print("Amount is valid")
            break
        else:
            print(exceed5)

    while True:
        data = int(input("How many kilos of frozen food such as meat would you like to load to Dhoani? : "))
        total = data + dhoani.value_at(1)
        if total <= dhoanicapacity.value_at(1):
            dhoani.replace_at(1, total)
            print("Amount is valid")
            break
        else:
            print(exceed5)

    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like load to Dhoani? : "))
        total = data + dhoani.value_at(2)
        if total <= dhoanicapacity.value_at(2):
            dhoani.replace_at(2, total)
            print("Amount is valid")
            break
        else:
            print(exceed5)

    while True:
        data1 = int(input("How many kilos of other food items such as grains and spices would you like to load to Dhoani? : "))
        data2 = int(input("How many kilos of construction materials such as cement and chemical would you like to load to Dhoani? : "))
        data3 = int(input("How many kilos of items such as steel, brick and sand would you like to load to Dhoani? : "))
        all = (data1 + data2 + data3)
        total = all + dhoani.value_at(3)
        if total <= dhoanicapacity.value_at(3):
            dhoani.replace_at(3, total)
            print("Amount is valid")
            break
        else:
            print(exceed5)

    while True:
        total = (dhoani.value_at(0)+dhoani.value_at(1)+dhoani.value_at(2)+dhoani.value_at(3))
        if total <= 30000:
            print("\n","The total amount is less than or equal to 30,000kgs.")
            break
        else:
            print("\n","The total amount exceeds the safety value of 30,000kgs. Hence enter valid amounts again.")
            dhoani_properties()

    print(" ")
    print("Kilos to be loaded at Dhoani")
    print("Diesel = ", dhoani.value_at(0))
    print("Frozen food = ", dhoani.value_at(1))
    print("Low temp food = ", dhoani.value_at(2))
    print("Other food, Protected material and Unprotected material = ", dhoani.value_at(3))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

def timings():
    time1 = (50/25) * 60
    time2 = (80/25) * 60
    time3 = (60/25) * 60
    time4 = (40/25) * 60
    time5 = (70/25) * 60

    print("\n" "ROUND 1")
    print("Island A -> Island B -> Island C -> Island D")
    print("\n" "The time from supplier's island 1 to reach island A =", int(time1), "minutes.")
    print("The time from island A to reach island B =", int(time2), "minutes.")
    print("The time from island B to reach island C =", int(time3), "minutes.")
    print("The time from island C to reach island D =", int(time4), "minutes.")
    print("The time from island D to reach supplier's island 2 =", int(time5), "minutes.")

    print("\n" "ROUND 2")
    print("Island D -> Island C -> Island B -> Island A")
    print("\n" "The time from supplier's island 2 to reach island D =", int(time5), "minutes.")
    print("The time from island D to reach island C =", int(time4), "minutes.")
    print("The time from island C to reach island B =", int(time3), "minutes.")
    print("The time from island B to reach island A =", int(time2), "minutes.")
    print("The time from island A to reach supplier's island 1 =", int(time1), "minutes.")

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

mainMenu()

