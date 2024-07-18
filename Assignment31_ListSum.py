def sum_of_list(lst):
    """
    This function takes a list of numbers as input
    and returns the sum of all the items in the list.
    """
    return sum(lst)  # Use the built-in sum function to calculate the total sum

# Example usage
numbers = [1, 2, 3, 4, 5]  # Define a list of numbers
total = sum_of_list(numbers)  # Call the function and store the result in 'total'
print("The sum of the list is:", total)  # Print the result
