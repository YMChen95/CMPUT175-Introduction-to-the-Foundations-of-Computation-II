# CMPUT 175 Winter 2013 Lab 4 Exercise 1
# This file implements the Queue class and can be used to test the Queue.

class Queue:
    
    # Constructor, which creates a new empty queue:
    def __init__(self):
        # TODO: You must implement this constructor!
        self.items=[]
    # Adds a new item to the back of the queue, and returns nothing:
    def queue(self, item):
        # TODO: You must implement this method!
        self.items.append(item)
    # Removes and returns the front-most item in the queue.  
    # Returns nothing if the queue is empty.
    def dequeue(self):
        # TODO: You must implement this method!
        if len(self.items)!=0:
            return  self.items.pop()
        else:
            return None        
    # Returns the front-most item in the queue, and DOES NOT change the queue.  
    def peek(self):
        # TODO: You must implement this method!
        if len(self.items)!=0:
            return self.items[0]
        else:
            return None
    # Returns True if the queue is empty, and False otherwise:
    def is_empty(self):
        # TODO: You must implement this method!
        return len(self.items) == 0
    # Returns the number of items in the queue:
    def size(self):
        # TODO: You must implement this method!
        return len(self.items)
    # Removes all items from the queue, and sets the size to 0:
    def clear(self):
        # TODO: You must implement this method!
        while len(self.items)!=0:
            self.items.pop()
    # Returns a string representation of the queue:
    def __str__(self):
        # TODO: You must implement this method!
        return str(self.items)
# Main function, which can be used to test your queue implementation:

def main():
    lineup=Queue()
    Loop=True
    while Loop:
        ask=input("Add, Serve, or Exit:")
        if ask =="Add":
            if lineup.size() >= 3:
                print("You cannot add more people, the lineup is full!")
                #ask=input("Add, Serve, or Exit:")
                Loop=True
            else:
                name=input("Enter the name of the person to add: ")
                lineup.queue(name)
        elif ask=="Serve":
            if lineup.is_empty():
                print("The lineup is already empty.")
                Loop=True                
            else:
                print(lineup.dequeue(),"has been served.")
        elif ask=="Exit":
            break
        
main()