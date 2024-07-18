def find_largest_and_smallest(numbers):
    """
    This function takes a list of numbers as input
    and returns the largest and smallest numbers in the list.
    """
    if not numbers:
        return None, None  # Return None if the list is empty
    
    largest = numbers[0]  # Initialize largest with the first element
    smallest = numbers[0]  # Initialize smallest with the first element
    
    for num in numbers:
        if num > largest:
            largest = num  # Update largest if current number is greater
        if num < smallest:
            smallest = num  # Update smallest if current number is smaller
    
    return largest, smallest

# Taking input from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Finding the largest and smallest numbers
largest, smallest = find_largest_and_smallest(numbers)

print("The largest number is:", largest)
print("The smallest number is:", smallest)
