class Node:
    def __init__(self, value=None, next=None):
        self.value = value # head is the node from which your are pointing towards next node
        self.next = next # next is the next node where pointer is pointing

class LinkedList:
    def __init__(self, name=None):
        self.head = None
        self._name = name
        
    def insert_at_end(self, element):
        if self.head is None:
            node = Node(element, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(element, None)
        
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
        # if index > (self.length()-1):
        #     print("index is out of range")
        #     return
        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.value = element
                break
            itr = itr.next
            count += 1
    
    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.value
            itr = itr.next

    def __str__ (self):
        return self._name
        
def initList(*args, **kwargs):
    records = LinkedList(kwargs.get("name", None))
    for item in args:
        records.insert_at_end(item)
    return records

def printCapacities(title, headers, values):
    print(f"{title}")
    for i, x in enumerate(headers):
        print(f"{x} = {values.value_at(i)}")
    print("")

def printCheckCapacity(title, limits, values):
    if all(limits.value_at(i) == values.value_at(i) for i, _ in enumerate(limits)):
        print(f"{title} IS FULL" "\n")
        return True
    else:
        print(f"{title} HAS CAPACITY" "\n")
        return False
    print("")

def checkCapacity(title, limits, values):
    if all(limits.value_at(i) == values.value_at(i) for i, _ in enumerate(limits)):
        return True
    else:
        return False
    print("")


# Declaring the initial capacity of the storages for islands and dhoani
islandA = initList(0,0,0,0,0,0, name="islandA")
islandB = initList(0,0,0,0,0,0, name="islandB")
islandC = initList(0,0,0,0,0,0, name="islandC")
islandD = initList(0,0,0,0,0,0, name="islandD")
dhoani = initList(0,0,0,0, name="dhoani")

# Declaring the total capacity of the storages for islands and dhoani
islandAcapacity = initList(1500, 40, 50, 100, 10000, float("inf"), name="islandAcapacity")
islandBcapacity = initList(2000, 40, 50, 90, 11000, float("inf"), name="islandBcapacity")
islandCcapacity = initList(1000, 40, 50, 110, 9000, float("inf"), name="islandCcapacity")
islandDcapacity = initList(1000, 40, 50, 80, 9000, float("inf"), name="islandDcapacity")
dhoaniCapacity = initList(4000, 40, 50, 28000, name="dhoaniCapacity")

# Declaring the headers of the storages for islands and dhoani
islandHeaders = initList("Diesel", "Frozen Food", "Low temp food", "Other food", "Protected material", "Unprotected material")
dhoaniHeaders = initList("Diesel", "Frozen Food", "Low temp food", "Other food, Protected material, Unprotected material")

# Declaring the journey routes for dhoani
routes = initList("Supplier", islandA, islandB, islandC, islandD, name="route1")  
routes2 = initList("Supplier", islandD, islandC, islandB, islandA, name="route2")

# Declaring the capacities for islands and dhoani
capacities = initList(dhoaniCapacity, islandAcapacity, islandBcapacity, islandCcapacity, islandDcapacity)

# Initializing reverse and current route
global reverse
reverse = False
global currentRoute
currentRoute = routes

# Function which shows the user all the storage capacities by passing through island and dhoani headers and capacities
def outputStorage():
    printCapacities("STORAGE CAPACITY AT ISLAND A ", islandHeaders, islandAcapacity)
    printCapacities("STORAGE CAPACITY AT ISLAND B ", islandHeaders, islandBcapacity)
    printCapacities("STORAGE CAPACITY AT ISLAND C ", islandHeaders, islandCcapacity)
    printCapacities("STORAGE CAPACITY AT ISLAND D ", islandHeaders, islandDcapacity)
    printCapacities("STORAGE CAPACITY AT DHOANI ", dhoaniHeaders, dhoaniCapacity)
    input("Enter anything to return to Main menu")
    mainMenu()

# Function which shows the user the current quantities in islands and dhoani
# ALso shows whether the capacity is full or not
def outputCapacity():
    printCapacities("CURRENT CAPACITY AT ISLAND A ", islandHeaders, islandA)
    printCheckCapacity("ISLAND A", islandAcapacity, islandA)

    printCapacities("CURRENT CAPACITY AT ISLAND B ", islandHeaders, islandB)
    printCheckCapacity("ISLAND B", islandBcapacity, islandB)

    printCapacities("CURRENT CAPACITY AT ISLAND C ", islandHeaders, islandC)
    printCheckCapacity("ISLAND C", islandCcapacity, islandC)

    printCapacities("CURRENT CAPACITY AT ISLAND D ", islandHeaders, islandD)
    printCheckCapacity("ISLAND D", islandDcapacity, islandD)

    printCapacities("CURRENT CAPACITY AT DHOANI ", dhoaniHeaders, dhoani)
    printCheckCapacity("DHOANI", dhoaniCapacity, dhoani)

    input("Enter anything to return to Main menu")
    mainMenu()

# Function which is used to add the items into dhoani
# Checks which product group the header is in
def addDhoani(header, values, capacity):
    dhoaniLimit = 0
    for i, x in enumerate(header):

        # Prompts the user to enter amount to store in dhoani for each product group
        # Validates the user input 
        # whether the total amount of the product group is less than or equal to the capacity of the product group
        # whether the total value of kgs entered is less than 30,000kgs which is the limit
        # Prompts the user to amount again if it exceeds capacity
        while True:
            try:
                amount = int (input(f"Enter amount of {x} to store in dhoani: "))
                total = amount + values.value_at(i)
                dhoaniLimit = values.value_at(0) + values.value_at(1) + values.value_at(2) + values.value_at(3) + amount

                if total <= capacity.value_at(i) and (dhoaniLimit) < 30000:
                    values.replace_at(i, values.value_at(i)+int(amount))
                    print("Amount valid" "\n")
                    break
                else:
                    print("Amount exceeds dhoani capacity. Enter amount again.\n")
            except:
                print("Error" "\n")

    # shows the user the total kgs in dhoani and lets them know dhoani values have been entered
    print(f"Total kgs in dhoani = {dhoaniLimit}")
    print("=== You have entered dhoani values ===")
    return

# function which is used to add items to islands from dhoani
# Checks which product group the header is in and which island the dhoani is in
# Checks whether the the island is full or not 
def addIsland(headers, currentRoute, capacity):     
    for i, x in enumerate(headers):
        if checkCapacity("", currentRoute, capacity):
            continue

        # intializing if index is greater than 3 index is always 3 so that the last 3 product group constraint is 28000
        dhoaniStockIndex = i if i < 3 else 3

        # Prompts the user to enter amount of kgs of the product group to unload to the current island
        # Validates the user input 
        # whether the total amount of the product group is less than or equal to the capacity of the product group
        # whether the user input kilos is available inside the dhoani or not
        # Prompts the user to amount again if it exceeds capacity
        while True:
            try:
                amount = int (input (f"How much {x} do you want to unload to {currentRoute} ? : "))
                addTotal = amount + currentRoute.value_at(i)

                if addTotal <= capacity.value_at(i) and amount <= dhoani.value_at(dhoaniStockIndex):
                    dhoani.replace_at(dhoaniStockIndex, dhoani.value_at(dhoaniStockIndex)- amount)
                    currentRoute.replace_at(i, addTotal)
                    print("Amount valid")
                    break
                else:
                    print("Amount invalid. Please try again.")
            except:    
                print("Error")

    # Asks the user to enter amounts to take from islands to back to dhoani
    print("\n" "Enter the values you would like to put back in dhoani" "\n")

# function which is used to remove items from islands and put them in dhoani
# Checks which product group the header is in and which island the dhoani is in
# Checks whether the the island is full or not 

def removeIsland(headers, currentRoute, values): 
    for i, x in enumerate(headers):

        # intializing if index is greater than 3 index is always 3 so that the last 3 product group constraint is 28000
        dhoaniStockIndex = i if i < 3 else 3

        # Prompts the user to enter amount of kgs of the product group to unload to the dhoani from current island
        # Validates the user input 
        # whether the amount entered of the product group is available in the current island
        # whether the dhoani has capacity to store the amount in product group capacity
        # whether the dhoani kilos exceed 30000 kgs or not
        # Prompts the user to amount again if it exceeds capacity
        while True:
            try:
                remove = int (input (f"How much {x} do you want to unload to dhoani from {currentRoute} ? : "))
                removeTotal = currentRoute.value_at(i) - remove
                dhoaniLimit = values.value_at(0) + values.value_at(1) + values.value_at(2) + values.value_at(3) + remove

                if remove <= currentRoute.value_at(i) and remove <= dhoaniCapacity.value_at(dhoaniStockIndex)and (dhoaniLimit) < 30000:
                   dhoani.replace_at(dhoaniStockIndex, dhoani.value_at(dhoaniStockIndex)+ remove)
                   currentRoute.replace_at(i, removeTotal)
                   print("Amount valid")
                   break
                else:
                    print("Amount invalid. Please try again.")
            except:    
                print("Error")

# function which calculates and shows the user the time remaining to reach the islands ahead
# checks which island the dhoani is currently at and shows the user the next destination and time to reach there
def timings(currentRoute):

    # Calculates the time to reach islands
    time1 = int(50/25) * 60
    time2 = int(80/25) * 60
    time3 = int(60/25) * 60
    time4 = int(40/25) * 60
    time5 = int(70/25) * 60

    # if the routes is not reverse meaning route is island A to B to C to D proceed
    if not reverse: 
        if currentRoute == "Supplier":
            print("\nYour journey is: Supplier's island -> Island A -> Island B -> Island C -> Island D -> Supplier's island")
            print(f"\nYou are at supplier's island.\nIt will take {time1} minutes to reach island A \n")
        elif currentRoute == islandA:
            print(f"\nYou have reached island A.\nIt will take {time2} minutes to reach island B\n")
        elif currentRoute == islandB:
            print(f"\nYou have reached island B.\nIt will take {time3} minutes to reach island C\n")
        elif currentRoute == islandC:
            print(f"\nYou have reached island C.\nIt will take {time4} minutes to reach island D\n")
        elif currentRoute == islandD:
            print(f"\nYou have reached island D.\nIt will take {time5} minutes to reach island Supplier's island \n")
    # else if the routes is reversed meaning route is now island D to C to B to A proceed
    else:
        if currentRoute == "Supplier":
            print("\nYour journey is: Supplier's island -> Island D -> Island C -> Island B -> Island A -> Supplier's island")
            print(f"\nYou are at supplier's island.\n It will take {time5} minutes to reach island D \n")
        elif currentRoute == islandA:
            print(f"\nYou have reached island D.\nIt will take {time4} minutes to reach island C \n")
        elif currentRoute == islandB:
            print(f"\nYou have reached island C.\nIt will take {time3} minutes to reach island B \n")
        elif currentRoute == islandC:
            print(f"\nYou have reached island B.\nIt will take {time2} minutes to reach island A \n")
        elif currentRoute == islandD:
            print(f"\nYou have reached island A.\nIt will take {time1} minutes to reach island Supplier's island \n")

# function which starts the journey of the dhoani
def journey(routes):
    for i, route in enumerate(routes):
        timings(route)
        if (route == "Supplier"):
            addDhoani(dhoaniHeaders, dhoani, dhoaniCapacity)
        else:
            addIsland(islandHeaders, route, capacities.value_at(i))
            removeIsland(islandHeaders, route, dhoani)
    print("\n" "**** You have finished your journey. You are now at the main menu **** ")
    global currentRoute
    global reverse
    if reverse:
        reverse = False
        currentRoute = routes
    else:
        reverse = True
        currentRoute = routes2
    mainMenu()

# Function for the main menu for the user interface
def mainMenu():
    # Shows the options to choose from to the user
    print("\n", "***** WELCOME TO THE PROGRAM *****", "\n")
    print("[1] Check the storage capacities of islands and dhoani", "\n")
    print("[2] Current quantity in storage of islands and dhoani", "\n")
    print("[3] Start your journey \n")

    # Prompts the user to enter an option
    # Validates the user input and prompts the user to try again if incorrect
    while True:
        try:
            option = int(input("Enter your option "))
            if option == 1:
                outputStorage()
                break
            if option == 2:
                outputCapacity()
                break
            if option == 3:
                journey(currentRoute)
                break
        except:
            print("Wrong option. Please try again !")

# executing the mainMenu function
mainMenu()



