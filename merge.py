def merge_list(input_1, list2):
    for x in list2:
        input_1.append(x)
    return sort(input_1)
#Selection Sort
def sort(unsorted):
        for i in range(len(unsorted)):
            if not isinstance(i, int):
                raise TypeError("TypeError")
            min_value = i;
            for j in range(i + 1, len(unsorted)):
                if unsorted[j] <= unsorted[min_value]:
                    min_value = j;
            unsorted[i], unsorted[min_value] = unsorted[min_value], unsorted[i] 
        return unsorted