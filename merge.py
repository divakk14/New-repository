def merge_list(list1, list2):
    for x in list2:
        list1.append(x)
    return sort(list1)
#Selection Sort
def sort(unsorted):
    try:
        for i in range(len(unsorted)):
            if not isinstance(i, int):
                raise TypeError
            min_value = i;
            for j in range(i + 1, len(unsorted)):
                if unsorted[j] <= unsorted[min_value]:
                    min_value = j;
            unsorted[i], unsorted[min_value] = unsorted[min_value], unsorted[i] 
        return unsorted
    except TypeError as e:
        return "TypeError"