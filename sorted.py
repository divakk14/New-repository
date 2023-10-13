def reverse_sort_dictionary(input_dict):
    # Check if the input is a dictionary
    if not isinstance(input_dict, dict):
        raise TypeError("Input must be any dictionary")

    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[0], reverse=True))

    res = [(name, data[0]) for name, data in sorted_dict.items()]

    return res

