def merge_list(input_1, input_2):
    merged_list = input_1 + input_2
    list_type_check(merged_list)
    return selection_sort(merged_list)

def list_type_check(list):
    for item in list:
        if not isinstance(item, int):
            raise TypeError("TypeError")

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list