

def count_words_in_file(file_path):
    """
    This function counts and displays the total number of words
    in the specified text file.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            print(f"The total number of words in the file is: {word_count}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

# Call the function with the file path
count_words_in_file("C:/Users/Admin/Desktop/ABC.txt")

# Example output (assuming the content of ABC.txt is):
# The total number of words in the file is: 20
