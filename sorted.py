def reverse_sort_dictionary(input_dict):
    # Check if the input is a dictionary
    if not isinstance(input_dict, dict):
        raise TypeError("Input must be a dictionary")

    # Sort the dictionary by keys (names) in reverse order
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[0], reverse=True))

    # Create a list of tuples with names and phone numbers
    result = [(name, data[0]) for name, data in sorted_dict.items()]

    return result

# # Sample input dictionary
sample_input = {
    'Tom': (5464512, 24),'Sara': (5446987, 32),'Mary': (1557896, 20)
}

# Call the function with the sample input
result = reverse_sort_dictionary(sample_input)

# Print the result
print(result)
#output 
#[('Tom', 5464512), ('Sara', 5446987), ('Mary', 1557896)]