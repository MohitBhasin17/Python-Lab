# Define the sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

def concatenate_dictionaries(*dicts):
    """
    This function takes multiple dictionaries as input
    and returns a new dictionary that concatenates all of them.
    """
    result = {}
    
    for dictionary in dicts:
        result.update(dictionary)  # Add each dictionary's items to the result
    
    return result

# Concatenate the dictionaries
concatenated_dict = concatenate_dictionaries(dic1, dic2, dic3)

# Print the result
print("The concatenated dictionary is:", concatenated_dict)
