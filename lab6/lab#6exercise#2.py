class CircularQueue1:
     # Constructor, which creates a new empty queue:
     def __init__(self, capacity):
          if type(capacity) != int or capacity<=0:
               raise Exception ("Capacity Error")
          
          self.__items = []
          self.__capacity = capacity
          self.__count=0
          self.__head=0
          self.__tail=0

     # Adds a new item to the back of the queue, and returns nothing:
     def enqueue(self, item):
          if self.__count== self.__capacity:
               raise Exception('Error: Queue is full')
          if len(self.__items) < self.__capacity:
               self.__items.append(item)
          else:
               self.__items[self.__tail]=item
          self.__count +=1
          self.__tail=(self.__tail +1) % self.__capacity
          
     # Removes and returns the front-most item in the queue.
     # Returns nothing if the queue is empty.
     def dequeue(self):
          if self.__count == 0:
               raise Exception('Error: Queue is empty')
          item= self.__items[self.__head]
          self.__items[self.__head]=None
          self.__count -=1
          self.__head=(self.__head+1) % self.__capacity
          return item
     
     # Returns the front-most item in the queue, and DOES NOT change the queue.
     def peek(self):
          if self.__count == 0:
               raise Exception('Error: Queue is empty')
          return self.__items[self.__head]
     
     # Returns True if the queue is empty, and False otherwise:
     def isEmpty(self):
          return self.__count == 0
 
     # Returns True if the queue is full, and False otherwise:
     def isFull(self):
          return self.__count == self.__capacity
 
     # Returns the number of items in the queue:
     def size(self):
          return self.__count
 
     # Returns the capacity of the queue:
     def capacity(self):
          return self.__capacity

     # Removes all items from the queue, and sets the size to 0
     # clear() should not change the capacity
     def clear(self):
          self.__items = []
          self.__count=0
          self.__head=0
          self.__tail=0
     # Returns a string representation of the queue:
     def __str__(self):
          str_exp = "["
          i=self.__head
          for j in range(self.__count):
               str_exp += str(self.__items[i]) + " "
               i=(i+1) % self.__capacity
          return str_exp + "]"

class CircularQueue2:
     # Constructor, which creates a new empty queue:
     def __init__(self, capacity):
          if type(capacity) != int or capacity<=0:
               raise Exception ("Capacity Error")
          
          self.__items = []
          self.__capacity = capacity
          self.__count=0
          self.__head=0
          self.__tail=0

     # Adds a new item to the back of the queue, and returns nothing:
     def enqueue(self, item):
          if self.__count== self.__capacity:
               raise Exception('Error: Queue is full')
          if len(self.__items) < self.__capacity:
               self.__items.append(item)
          else:
               self.__items[self.__tail]=item
          self.__count +=1
          self.__tail=(self.__tail +1) % self.__capacity
          
     # Removes and returns the front-most item in the queue.
     # Returns nothing if the queue is empty.
     def dequeue(self):
          if self.__count == 0:
               raise Exception('Error: Queue is empty')
          item= self.__items[self.__head]
          self.__items[self.__head]=None
          self.__count -=1
          self.__head=(self.__head+1) % self.__capacity
          return item
     
     # Returns the front-most item in the queue, and DOES NOT change the queue.
     def peek(self):
          if self.__count == 0:
               raise Exception('Error: Queue is empty')
          return self.__items[self.__head]
     
     # Returns True if the queue is empty, and False otherwise:
     def isEmpty(self):
          return self.__count == 0
 
     # Returns True if the queue is full, and False otherwise:
     def isFull(self):
          return self.__count == self.__capacity
 
     # Returns the number of items in the queue:
     def size(self):
          return self.__count
 
     # Returns the capacity of the queue:
     def capacity(self):
          return self.__capacity

     # Removes all items from the queue, and sets the size to 0
     # clear() should not change the capacity
     def clear(self):
          self.__items = []
          self.__count=0
          self.__head=0
          self.__tail=0
     # Returns a string representation of the queue:
     def __str__(self):
          str_exp = "["
          i=self.__head
          for j in range(self.__count):
               str_exp += str(self.__items[i]) + " "
               i=(i+1) % self.__capacity
          return str_exp + "]"

def main():
     normallist=[]
     Viplist=[]
     normal=CircularQueue1(3)
     vip=CircularQueue2(3)
     Loop=True
     while Loop:
          choose=input("Add, Serve, or Exit: ")
          if choose=="add":
               names=input("Enter the name of the person to add: ")
               types=input("Is the customer VIP? ")
               if types == "True":
                    if not vip.isFull():    
                         vip.enqueue(names)
                         print("add",names,"to VIP line.")
                    else:
                         print("Error: vip customer queue is full")
               elif types == "False":
                    if not normal.isFull():
                         normal.enqueue(names)
                         print("add",names,"to the line.")
                    else:
                         print("Error: Normal customer queue is full")
               else:
                    print("invild name input")
                         
               print("people in the line:",normal)
               print("VIP customers queue:",vip)
               Loop=True
          elif choose == "serve":
               if not vip.isEmpty():
                    print(vip.dequeue(),"has been served")
                      
               else:
                    if not normal.isEmpty():
                         normal.dequeue()
                    else:
                         print("Error: Queues are empty")
               print("people in the line:",normal)
               print("VIP customers queue:",vip)                         
          elif choose=="exit":
               print("Quitting")
               break
          else:
               Loop=True
               print("Invild input")
main()