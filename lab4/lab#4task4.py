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
    
def main():
    running=True
    try:
        filename = input("Enter the file name:")
        infile = open(filename,'r')
    except:
        print('The file does not exist')
        running = False
        
    if running == True:
        s = Stack()
        one = 0    #()
        two = 0    #{}
        three = 0  #[]
        small_l = 0
        small_r = 0
        mid_l = 0
        mid_r = 0
        large_l = 0
        large_r =0
        for line in infile:
            line = line.strip('\r\n')
            for word in line:
                if word in '{[(':
                    s.push(word)
                try:
                    peek = s.peek()
                except:
                    peek = s.is_empty()
                if word == ')':
                    small_r += 1
                    if '(' == peek:
                        small_l += 1
                        one += 1
                        s.pop()
                if word == '}':
                    mid_r += 1
                    if '{' == peek:
                        mid_l += 1
                        two += 1
                        s.pop()
                if word == ']':
                    large_r += 1
                    if '[' == peek:
                        large_l += 1
                        three += 1
                        s.pop()
        print('() pairs:',one)
        print('{} pairs:',two)
        print('[] pairs:',three)
        
        if (small_l+small_r)%2 == 0:
            print("All () matched.")
        else:
            print("Not all () matched.")
        if (mid_l+mid_r)%2 == 0:
            print("All {} matched.")
        else:
            print("Not all {} matched.")
        if (large_l+large_r)%2 == 0:
            print("All [] matched.")
        else:
            print("Not all [] matched.")
main()