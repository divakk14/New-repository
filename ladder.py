def my_steps(number):
    if not (1 <= n <= 25):
        raise ValueError("Input number must be between 1 and 25, inclusive.")
    
    if number <= 2:
        return number
    else:
        # Init list - store the n of ways for every step
        ways = [0] * (number + 1)
        ways[1] = 1  #1 way to climb a 1-step ladder 
        ways[2] = 2  #2 ways to climb a 2-step ladder
        
        # Calculate n of ways - each step
        for i in range(3, number + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        
        return ways[number]

# # For testing
# if __name__ == "__main__":
#     # Test cases
#     input_number = 2
#     output_number = my_steps(input_number)
#     print(f"Input : {input_number}\nOutput: {output_number}")

#     input_number = 3
#     output_number = my_steps(input_number)
#     print(f"Input : {input_number}\nOutput: {output_number}")




