from linkedList import LinkedList

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
        print(f"{title} IS FULL")
    else:
        print(f"{title} HAS CAPACITY")
    print("")


# Declaring the initial capacity of the storages for islands and dhoani
islandA = initList(0,0,0,0,0,0, name="islandA")
islandB = initList(0,0,0,0,0,0, name="islandB")
islandC = initList(0,0,0,0,0,0, name="islandC")
islandD = initList(0,0,0,0,0,0, name="islandD")
dhoani = initList(0,0,0,0, name="dhoani")

# Declaring the total capacity of the storages for islands and dhoani
islandAcapacity = initList(1500, 40, 50, 100, 10000, "Unlimited", name="islandAcapacity")
islandBcapacity = initList(2000, 40, 50, 90, 11000, "Unlimited", name="islandBcapacity")
islandCcapacity = initList(1000, 40, 50, 110, 9000, "Unlimited", name="islandCcapacity")
islandDcapacity = initList(1000, 40, 50, 80, 9000, "Unlimited", name="islandDcapacity")
dhoaniCapacity = initList(4000, 40, 50, 28000, name="dhoaniCapacity")

# Declaring the headers of the storages for islands and dhoani
islandHeaders = initList("Diesel", "Frozen Food", "Low temp food", "Other food", "Protected material", "Unprotected material")
dhoaniHeaders = initList("Diesel", "Frozen Food", "Low temp food", "Other food, Protected material, Unprotected material")

# Declaring the journey routes for dhoani
routes = initList("Supplier", islandA, islandB, islandC, islandD, "Supplier")
routesReversed = initList("Supplier", islandD, islandC, islandB, islandA, "Supplier")
current = initList("Supplier", 0)


def mainMenu():
    print("\n", "***** WELCOME TO THE PROGRAM *****", "\n")

    print("[1] Check the storage capacities of islands and dhoani", "\n")
    print("[2] Current quantity in storage of islands and dhoani", "\n")
    print("[3] Start journey", "\n")

    while True:
            print("")
            option = int(input("Enter your option "))
            if option == 1:
                outputStorage()
                break
            if option == 2:
                outputCapacity()
                break
            if option == 3:
                journey()
                break

    exit

# Function which shows the user all the storage capacities
def outputStorage():
    printCapacities("STORAGE CAPACITY AT ISLAND A ", islandHeaders, islandAcapacity)
    printCapacities("STORAGE CAPACITY AT ISLAND B ", islandHeaders, islandBcapacity)
    printCapacities("STORAGE CAPACITY AT ISLAND C ", islandHeaders, islandCcapacity)
    printCapacities("STORAGE CAPACITY AT ISLAND D ", islandHeaders, islandDcapacity)
    printCapacities("STORAGE CAPACITY AT DHOANI ", dhoaniHeaders, dhoaniCapacity)
    input("Enter anything to return to Main menu")
    mainMenu()

# Function which shows the user the current quantities in islands and dhoani
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

def addGoods(header, values):
    for i, x in enumerate(header):
        amount = input(f"Enter amount of {x} to store: ")
        values.replace_at(i, values.value_at(i)+int(amount))
    return


def addGoodsReversed():
    pass

def swap(headers, currentRoute):
    for i, x in enumerate(headers):
        amount = int (input (f"How much {x} do you want to unload to {currentRoute} ? : "))
        dhoaniStockIndex = i if i < 3 else 3
        dhoani.replace_at(dhoaniStockIndex, dhoani.value_at(dhoaniStockIndex)- amount)
        currentRoute.replace_at(i, currentRoute.value_at(i)+ amount)



def journey():
    for i, route in enumerate(routes):
        if (i == 0):
            addGoods(dhoaniHeaders, dhoani)
        elif (i == 5):
            addGoods(dhoaniHeaders, dhoani)
        else:
            swap(islandHeaders, route)
    mainMenu()

mainMenu()