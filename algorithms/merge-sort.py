def merge(list1,list2):
    '''merges two sorted lists into one sorted list'''
    combined = []
    i,j = 0,0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j+=1
    return combined
def merge_sort(my_list):
    '''divides the list till each element is a list of its own and then uses merge() on it'''
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left,right)

l1 = [10,100,40,90,50,30]
print(merge_sort(l1))



















































