# Define the dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary by concatenating the existing ones
result = {**dic1, **dic2, **dic3}

# Print the result
print("Expected Result :", result)


'''
Output:
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

'''
