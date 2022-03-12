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

exceed1 = ("\nAmount exceeds storage capacity of the island A, please try again.\n")
exceed2 = ("\nAmount exceeds storage capacity of the island B, please try again.\n")
exceed3 = ("\nAmount exceeds storage capacity of the island C, please try again.\n")
exceed4 = ("\nAmount exceeds storage capacity of the island D, please try again.\n")
exceed5 = ("\nAmount exceeds storage capacity of the dhoani, please try again.\n")

# __________ ISLAND A _________
    
def islandA_properties():

    while True:
        data = int(input("How many kilos of diesel do you want to unload at island A? "))
        if data <= islandAcapacity.value_at(0):
            islandA.replace_at(0, data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

    while True:
        data = int(input("How many kilos of frozen food such as meat would you like unload to Island A? : "))
        if data <= islandAcapacity.value_at(1):
            islandA.replace_at(1, data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like unload to Island A? : "))
        if data <= islandAcapacity.value_at(2):
            islandA.replace_at(2, data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like unload to Island A? : "))
        if data <= islandAcapacity.value_at(3):
            islandA.replace_at(3, data)
            print("Amount is valid")
            break
        else:
            print(exceed1)


    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like unload to Island A? : "))
        if data <= islandAcapacity.value_at(4):
            islandA.replace_at(4, data)
            print("Amount is valid")
            break
        else:
            print(exceed1)
            
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like unload to Island A? : "))
        if type(data) == int:
            islandA.replace_at(5, data)
            print("Amount is valid")
            break
        else:
            print(exceed1)

    print(" ")
    print("Kilos to be unloaded at island A")
    print("Diesel = ", islandA.value_at(0))
    print("Frozen food = ", islandA.value_at(1))
    print("Low temp food = ", islandA.value_at(2))
    print("Other food = ", islandA.value_at(3))
    print("Protected material = ", islandA.value_at(4))
    print("Unprotected material = ", islandA.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

# ___________ ISLAND B ____________

def islandB_properties():

    while True:
        data = int(input("How many kilos of diesel do you want to unload at island B? "))
        if data <= islandBcapacity.value_at(0):
            islandB.replace_at(0, data)
            print("Amount is valid")
            break
        else:
            print(exceed2)

    while True:
        data = int(input("How many kilos of frozen food such as meat would you like unload to Island B? : "))
        if data <= islandBcapacity.value_at(1):
            islandB.replace_at(1, data)
            print("Amount is valid")
            break
        else:
            print(exceed2)

    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like unload to Island B? : "))
        if data <= islandBcapacity.value_at(2):
            islandB.replace_at(2, data)
            print("Amount is valid")
            break
        else:
            print(exceed2)

    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like unload to Island B? : "))
        if data <= islandBcapacity.value_at(3):
            islandB.replace_at(3, data)
            print("Amount is valid")
            break
        else:
            print(exceed2)


    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like unload to Island B? : "))
        if data <= islandBcapacity.value_at(4):
            islandB.replace_at(4, data)
            print("Amount is valid")
            break
        else:
            print(exceed2)
            
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like unload to Island B? : "))
        if type(data) == int:
            islandB.replace_at(5, data)
            print("Amount is valid")
            break
        else:
            print(exceed2)

    print(" ")
    print("Kilos to be unloaded at island B")
    print("Diesel = ", islandB.value_at(0))
    print("Frozen food = ", islandB.value_at(1))
    print("Low temp food = ", islandB.value_at(2))
    print("Other food = ", islandB.value_at(3))
    print("Protected material = ", islandB.value_at(4))
    print("Unprotected material = ", islandB.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

# ___________ ISLAND C ____________

def islandC_properties():

    while True:
        data = int(input("How many kilos of diesel do you want to unload at island C? "))
        if data <= islandCcapacity.value_at(0):
            islandC.replace_at(0, data)
            print("Amount is valid")
            break
        else:
            print(exceed3)

    while True:
        data = int(input("How many kilos of frozen food such as meat would you like unload to Island C? : "))
        if data <= islandCcapacity.value_at(1):
            islandC.replace_at(1, data)
            print("Amount is valid")
            break
        else:
            print(exceed3)

    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like unload to Island C? : "))
        if data <= islandCcapacity.value_at(2):
            islandC.replace_at(2, data)
            print("Amount is valid")
            break
        else:
            print(exceed3)

    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like unload to Island C? : "))
        if data <= islandCcapacity.value_at(3):
            islandC.replace_at(3, data)
            print("Amount is valid")
            break
        else:
            print(exceed3)


    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like unload to Island C? : "))
        if data <= islandCcapacity.value_at(4):
            islandC.replace_at(4, data)
            print("Amount is valid")
            break
        else:
            print(exceed3)
            
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like unload to Island C? : "))
        if type(data) == int:
            islandC.replace_at(5, data)
            print("Amount is valid")
            break
        else:
            print(exceed3)

    print(" ")
    print("Kilos to be unloaded at island C")
    print("Diesel = ", islandC.value_at(0))
    print("Frozen food = ", islandC.value_at(1))
    print("Low temp food = ", islandC.value_at(2))
    print("Other food = ", islandC.value_at(3))
    print("Protected material = ", islandC.value_at(4))
    print("Unprotected material = ", islandC.value_at(5))

    anykey = input("Enter anything to return to Main menu")
    mainMenu()

# ___________ ISLAND D ____________

def islandD_properties():

    while True:
        data = int(input("How many kilos of diesel do you want to unload at island D? "))
        if data <= islandDcapacity.value_at(0):
            islandD.replace_at(0, data)
            print("Amount is valid")
            break
        else:
            print(exceed4)

    while True:
        data = int(input("How many kilos of frozen food such as meat would you like unload to Island D? : "))
        if data <= islandDcapacity.value_at(1):
            islandD.replace_at(1, data)
            print("Amount is valid")
            break
        else:
            print(exceed4)

    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like unload to Island D? : "))
        if data <= islandDcapacity.value_at(2):
            islandD.replace_at(2, data)
            print("Amount is valid")
            break
        else:
            print(exceed4)

    while True:
        data = int(input("How many kilos of other food items such as grains and spices would you like unload to Island D? : "))
        if data <= islandDcapacity.value_at(3):
            islandD.replace_at(3, data)
            print("Amount is valid")
            break
        else:
            print(exceed4)


    while True:
        data = int(input("How many kilos of construction materials such as cement and chemical would you like unload to Island D? : "))
        if data <= islandDcapacity.value_at(4):
            islandD.replace_at(4, data)
            print("Amount is valid")
            break
        else:
            print(exceed4)
            
    while True:
        data = int(input("How many kilos of items such as steel, brick and sand would you like unload to Island D? : "))
        if type(data) == int:
            islandD.replace_at(5, data)
            print("Amount is valid")
            break
        else:
            print(exceed4)

    print(" ")
    print("Kilos to be unloaded at island D")
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
        data = int(input("How many kilos of diesel do you want to load at Dhoani? "))
        if data <= dhoanicapacity.value_at(0):
            dhoani.replace_at(0, data)
            print("Amount is valid")
            break
        else:
            print(exceed5)

    while True:
        data = int(input("How many kilos of frozen food such as meat would you like load to Dhoani? : "))
        if data <= dhoanicapacity.value_at(1):
            dhoani.replace_at(1, data)
            print("Amount is valid")
            break
        else:
            print(exceed5)

    while True:
        data = int(input("How many kilos of food items requiring low temperature such as fruits and vegetables would you like load to Dhoani? : "))
        if data <= dhoanicapacity.value_at(2):
            dhoani.replace_at(2, data)
            print("Amount is valid")
            break
        else:
            print(exceed5)

    while True:
        data1 = int(input("How many kilos of other food items such as grains and spices would you like load to Dhoani? : "))
        data2 = int(input("How many kilos of construction materials such as cement and chemical would you like load to Dhoani? : "))
        data3 = int(input("How many kilos of items such as steel, brick and sand would you like load to Dhoani? : "))
        total = (data1 + data2 + data3)
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