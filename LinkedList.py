class Node: # this class creates a new Node tf if any method wants to create a new Node it will call on the Node class
    def __init__(self, value):
        self.value = value #the value gets passed to the specific instance of Node
        self.next = None

class LinkedList: #A
    def __init__(self, value): #we always pass a value in order to create the new Node
        new_node = Node(value) #this calls the Node class and we pass this value to the Node class and that creates the Node
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self): #C
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value): #B
        new_node = Node(value)
        if self.head is None: #if head is none (i.e linked list is empty) set head and tail equal to the new node
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node #this is where items are already in the linked list, tail.next(tail variable and the pointer) is equal to the new node
            self.tail = new_node #moving tail variable over to set it equal to the new node
        self.length += 1 #increase the length of the linked list by one
        return True
        

    def prepend(self, value): #adding an item to the beginning of the linked list #E
        new_node = Node(value)
        if self.length == 0: #list is empty
            self.head = new_node
            self.tail = new_node
        else: #list isn't empty
        new_node.next = self.head #points new node to the beginning of the list
        self.head = new_node #the head variable points to the new node
        self.length +=1 
        return True


    def insert(self, index, value):
        pass

    def pop(self): #D removing last item
        if self.length == 0: #list is empty
            return None

#two or more items in the list
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp #both pointing to the same node
            temp = temp.next #this moves the temp variable over to the next node on each iteration
        self.tail = pre #pre variable was on the second to last node and we've come to the end of the iteration tf the tail (end) now points to the end node which was the second to the last node
        self.tail.next = None #breaking the last node from the linked list
        self.length -= 1
        if self.length == 0    #only 1 node in the list
            self.head = None
            self.tail = None
        return temp #this returns the node we just removed

    def pop_first(self): #F removing first item
        if self.head is None:
            return None
        
        #2 or more items in the list
        temp = self.head #made a new temp variable
        self.head = self.head.next #moving head variable over to the next node
        temp.next = None #the first node's pointer is now equal to none, thereby removing it from the linked list
        self.length -= 1 #we decrement the length by one

        #only 1 item in the list
        if self.length == 0
            self.tail = None
        return temp #this is the item we removed 

    def get(self, index): #G
        if index < 0 or index >= self.length #this tests to see if the index is valid
            return None #bc we can't get a node at any of those indices

        temp = self.head
        for _ in range(index): 
            temp = temp.next #this moves temp along the linked list
        return temp
        
    def set_value(self, index, value): #H can't use set as a method name bc it's a keyword in python
        temp = self.get(index)

        if temp is not None:
            temp.value = value
            return True
        return False #if the get method returns None (meaning it's an invalid index) we return false





#A: my_linked_list = LinkedList(4) --> we call the LinkedList class and pass it a value (4).
#A: print(my_linked_list.head.value) --> output is 4

#B: my_linked_list.append(2)

#D: (2) Items - Returns 2 Nodes
#print(my_linked_list.pop())

#D: (1) Item - Returns 1 Node
#print(my_linked_list.pop())

#D: (0) Items - Returns None
#print(my_linked_list.pop())

#E: my_linked_list.prepend(1)

#F: (2) Items - Returns 2 Nodes
#print(my_linked_list.pop_first())

#F: (1) Item - Returns 1 Node
#print(my_linked_list.pop_first())

#F: (0) Items - Returns None
#print(my_linked_list.pop_first())

#G: first we can append some values then get the value that's at the index of 2 -> print(my_linked_list.get(2))

#H: first we can append some values then change the value at the index of 1 to 4 -> my_linked_list.set_value(1,4)

#C: my_linked_list.print_list()
