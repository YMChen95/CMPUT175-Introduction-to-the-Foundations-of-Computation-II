unsorted_list = [['a','b','c','@5','d'],['e','f','g','@3','h'],['i','j','k','@4','m']]

unsorted_list.sort(key=lambda x: int(x[3][1:]))

print(unsorted_list)
