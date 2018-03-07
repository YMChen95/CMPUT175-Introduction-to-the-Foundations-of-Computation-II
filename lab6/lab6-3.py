from CircularQueue import CircularQueue
def main():
     normal=CircularQueue(3)
     vip=CircularQueue(3)
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