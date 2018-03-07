def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            result += left[i:]
            result += right[j:]
    return result
def mergeSort(data):# Sort myself using a merge sort.
    if len(data) <=1:
        return data
    
    middle = len(data)//2 
    left=mergeSort(data[:middle])
    right=mergeSort(data[middle:])
    
    return merge(left,right)
my_list=[5,2,4,3,1,0]
my_list2=mergeSort(my_list)
print(my_list2)