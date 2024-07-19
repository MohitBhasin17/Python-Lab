
# Q. Write a function in python to read the content from a text file "ABC.txt" 
# line by line and display the same on screen.

def read_file_line_by_line(file_path):
    """
    This function reads the content from a text file line by line
    and displays the same on the screen.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())  # Print each line without extra newline characters
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

# Call the function with the file path
read_file_line_by_line("C:/Users/Admin/Desktop/ABC.txt")

'''
Output:-
Hello my name is Mohit Bhasin
Im an recent graduate from Mumbai University in the field of CS

'''
