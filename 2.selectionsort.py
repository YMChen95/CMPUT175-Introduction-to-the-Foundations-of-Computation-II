def selectionSort(data):
# Sort the given Array with selection sort method
#(Ascending order)
    for index in range(len(data)):
        smallIndex = index
        for i in range(index,len(data)):    # finding smallest
            if(data[i]<data[smallIndex]):
                smallIndex=i

        temp=data[index]                      # swapping
        data[index]=data[smallIndex]
        data[smallIndex]=temp
    return data

my_list=[5,2,4,3,1,0]
my_list2=selectionSort(my_list)
print(my_list2)