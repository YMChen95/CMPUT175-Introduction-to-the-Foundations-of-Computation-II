from d_linked_node import d_linked_node

class d_linked_list:
    
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        

            
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # TODO: 
        temp =d_linked_node(item,self.__head,None)
        if self.__head!=None:
            self.__head.setPrevious(temp)
        else:
            self.__tail=temp
        self.__head= temp
        self.__size+= 1
    def remove(self, item):
        # TODO:
        current =self.__head
        previous=None    
        found= False
        while not found:
            if current.getData()==item:
                found =True
            else:
                previous= current
                current=current.getNext()
        if previous == None:
            self.__head =current.getNext()
        else:
            previous.setNext(current.getNext())
        if (current.getNext() !=None):
            current.getNext().setPrevious(previous)
        else:
            self.__tail=previous
        self.__size-=1           
    def append(self, item):
        # TODO:
        temp = d_linked_node(item,None,None )
        if(self.__head ==None):
            self.__head=temp
        else:
            self.__tail.setNext(temp)
            temp.setPrevious(self.__tail)
        self.__tail=temp
        self.__size +=1        
    def insert(self, pos, item):
        # TODO:
        s = 0;
        if pos > self.__size - 1 :
            raise Exception ("size to big")
        if pos == 0:
            self.add(item)
        elif pos == self.__size :
            self.append(item)
        else:
            current = self.__head
            while current:
                if s == pos:
                    pre = current.getPrevious()
                    a = d_linked_node(item, current, pre)
                    pre.setNext(a)
                    current.setPrevious(a)
                    self.__size += 1
                    break
                else:
                    current = current.getNext()
                    s += 1        
    def pop1(self):
        # TODO:
        if self.__tail == None:
            return None
        data = self.__tail.getData()
        self.__size -= 1
        if self.__size == 0:
            self.__tail = None
            self.__head = None
        else:
            self.__tail = self.__tail.getPrevious()
            self.__tail.setNext( None)       
        return data     
    def pop(self, pos):    
        data = None
        if pos > self.__size - 1 :
            raise Exception ("size to big")
        if self.__size == 0:
            return None
        if self.__size == 1:
            data = self.__head.getData()
            self.__size = 0
            self.__head = None
            self.__tail = None
            return data
        if pos == 0:
            a = self.__head
            data = a.getData()
            self.__head = a.getNext()
            self.__head.setPrevious(None)
            self.__size -= 1
        elif pos == self.__size - 1 :
            return self.pop1()
        else:
            current = self.__head
            while 1:
                if pos == 0:
                    pre = current.getPrevious()
                    nex = current.getNext()
                    data = current.getData()
                    pre.setNext(nex)
                    nex.setPrevious(pre)
                    break
                else:
                    current = current.getNext()
        return data       
    def search_larger(self, item):
        # TODO:
        pos = 0
        current = self.__head
        while current:
            if current.getData() > item:
                return pos
            else:
                current = current.getNext()
                pos += 1
        return -1        
    def get_size(self):
        # TODO:    
        return self.__size
    def get_item(self, pos):
        # TODO:   
        s = 0;
        if pos > self.__size - 1 :
            raise Exception ("size to big")
        if pos < 0:
            return self.get_item(self.__size + pos)
        if pos == 0:
            return self.__head.getData()
        if pos == self.__size - 1 :
            return self.__tail.getData()
        current = self.__head
        while current:
            if s == pos:
                return current.getData()
            else:
                current = current.getNext()
                s +=1        
    def __str__(self):
        # TODO:  
        current = self.__head
        my_list = []
        while current:
            my_list.append(str(current.getData()))
            current = current.getNext()
        return " ".join(my_list)        
        

def test():
                  
    linked_list = d_linked_list()
                    
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.get_item(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.get_item(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.get_item(0) == "Hello" and linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop1() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = d_linked_list()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.get_size() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = d_linked_list()
                    
    is_pass = (int_list.get_size() == 0)
    assert is_pass == True, "fail the test"
                    
        
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.get_size() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop1() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.search_larger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.search_larger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.get_item(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.get_item(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 1! ============")
                
if __name__ == '__main__':
    test()