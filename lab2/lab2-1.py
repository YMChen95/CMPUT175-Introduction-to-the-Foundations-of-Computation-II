
isProgram = True
try:
    infile=open("accounts.txt","r")
except IOError:
    print('File does not exist')
    isProgram = False
if isProgram == True:
    myDic={}
    for line in infile:
        name, money=line.split(":")
        myDic[name]=money
    #print(myDic)
    userinput=""
    while userinput!="Stop":
        userinput=input("Enter account name, or 'Stop' to exit: ")
        try:
            useroutput=float(myDic[userinput])
            myDic[userinput]=useroutput
        except ValueError:
            print("Account for",userinput,"not added: illegal value for balance")
            continue
        except KeyError:
            if userinput!="Stop":
                print("Account does not exist, transaction canceled")
                continue
            else:
                continue
        try:
            inputMoney=float(input("Enter transaction amount: "))
        except ValueError:
            print("llegal value for transaction, transaction canceled ")
            continue
        myDic[userinput]=myDic[userinput]+inputMoney
        print("New balance for account ",userinput,"%0.2f"%myDic[userinput])