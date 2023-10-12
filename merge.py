# def merge_list(input_1, list2):
#     for x in list2:
#         input_1.append(x)
#     return sort(input_1)
# #Selection Sort
# def sort(unsorted):
#         for i in range(len(unsorted)):
#             if not isinstance(i, int):
#                 raise TypeError("TypeError")
#             min_value = i;
#             for j in range(i + 1, len(unsorted)):
#                 if unsorted[j] <= unsorted[min_value]:
#                     min_value = j;
#             unsorted[i], unsorted[min_value] = unsorted[min_value], unsorted[i] 
#         return unsorted



# merge.py

def merge_list(input_1, input_2):
    merged_list = input_1 + input_2
    list_type_check(merged_list)
    return selection_sort(merged_list)

def list_type_check(list):
    for element in list:
        if not isinstance(element, int):
            raise TypeError("TypeError")

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list