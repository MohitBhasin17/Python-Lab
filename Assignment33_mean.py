# Define the dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

def calculate_mean(dictionary):
    """
    This function takes a dictionary of values as input
    and returns the mean of the values.
    """
    total = 0
    count = 0
    
    for value in dictionary.values():
        total += value  # Add each value to the total
        count += 1  # Increment the count of values
    
    mean = total / count  # Calculate the mean
    return mean

# Calculate the mean of the dictionary values
mean_value = calculate_mean(test_dict)

# Print the result
print("The mean of the dictionary values is:", mean_value)
