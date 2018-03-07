class Stack:
    
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        
    def pop(self):
        return self.__items.pop()
    
    def peek(self):
        return self.__items[len(self.__items)-1]
    
    def isEmpty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)


def tokenize(string):
    separators = set(' ')
    operators = set('+-*/^&')
    parentheses = set('()')
    tokens = []# to store the tokens to return
    buff = []# to store and combine consecutive digits
    #string.split()
    for c in string: #examine 1 character at a time
        if c in separators or c in operators or c in parentheses:
            if len(buff)>0:
                tokens.append(float(''.join(buff)))
                buff = []
        if c in operators or c in parentheses:
            tokens.append(c)
        elif c not in separators: # digits and the decimal point
            buff.append(c)
    if len(buff)>0:
        tokens.append(float(''.join(buff)))
    return tokens

def infixToPostfix(tokenList):
  
    prec = {}
    prec["^"] = 4
    prec["&"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack =Stack()
    postfixList = [] 
    for token in tokenList:
        if isFloat(token):
                postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token ==')':
            if opStack.isEmpty():
                raise Exception('Unmatched parenthesis: )')
            topToken = opStack.pop()
            while topToken !='(':
                postfixList.append(topToken)
                if opStack.isEmpty():
                    raise Exception('Unmatched parenthesis: )')
                topToken = opStack.pop()
        else:
            while(not opStack.isEmpty())and\
                 (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        topToken=opStack.pop()
        if topToken == "(":
            raise Exception('Unmatched parenthesis: (')        
            
        postfixList.append(topToken)     
    return postfixList

def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def postfixEval(postfixExpr):
    operandStack =Stack()
    for token in postfixExpr:
        if isFloat(token):
            operandStack.push(token)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,int(operand1),int(operand2))
            operandStack.push(result)            
    result=operandStack.pop()
    if operandStack.isEmpty() == False:
        raise Exception("Unmatched operand")
    return  result

def doMath(op, op1, op2):
    if op =="*":
        return op1 * op2
    elif op =="/":
        return op1 / op2
    elif op =="+":
        return op1 + op2
    elif op =="-":
        return op1-op2
    elif op =="^":
        return op1**op2
    elif op =="&":
        return op2**(1.0/op1)
    else:
        raise Exception("Unknown Operator")
def assertion():
    assert isFloat(5),"it is not a float"
    assert tokenize("1+1"),"it is not a string"
    assert infixToPostfix([1.0, '+', 1.0]),"Unmatched parenthesis"
    assert postfixEval([1.0, 1.0, '+']),"Unmatched operand"
    assert doMath("+",1,1),"Unknown Operator"
    assert postfixEval(infixToPostfix(tokenize("50*2")))==100,"anwser not match"
def main():
    assertion()
    string=input("Enter: ")
    while string!="exit":
        try:
            tokenList= tokenize(string)
            postfixList=infixToPostfix(tokenList)
            result=postfixEval(postfixList)
            print('Result: %f'%result)                     
        except ValueError as inst:
            print('ValueError:', inst.args)
        except ZeroDivisionError as inst:
            print('ZeroDivisionError ',inst.args)
        except Exception as inst:
            print('Invalid request: ', inst.args)
        string =input('Enter: ')        
main()