# CMPUT 175 Winter 2013 Lab 4 Exercise 3
# A Stack implementation

class Stack:
    
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        
    def pop(self):
        return self.__items.pop()
    
    def peek(self):
        return self.__items[len(self.__items)-1]
    
    def is_empty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)

    
reverse=Stack()
alist=[]
sentence=str(input("Enter a String to reverse: "))
for i in range(0,len(sentence)):
    reverse.push(sentence[i])
for i in range(0,len(sentence)):
    alist.append(reverse.pop())
print("The reversed String is:"+"".join(alist))