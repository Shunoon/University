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