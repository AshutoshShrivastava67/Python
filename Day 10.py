#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen. 
def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # .strip() removes any extra newlines or spaces
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = "ABC.txt"
read_file_line_by_line(filename)


#Write a function in Python to count and display the total number of words in a text file “ABC.txt”
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            total_words = 0
            for line in file:
                words = line.split()  # Split the line into words
                total_words += len(words)  # Count the words in the current line

        print(f"Total number of words in '{filename}': {total_words}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = "ABC.txt"
count_words_in_file(filename)


# Write a function in Python to count uppercase character in a text file “ABC.txt”
def count_uppercase_characters(filename):
    try:
        with open(filename, 'r') as file:
            uppercase_count = 0
            for line in file:
                for char in line:
                    if char.isupper():
                        uppercase_count += 1

        print(f"Total number of uppercase characters in '{filename}': {uppercase_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = "ABC.txt"
count_uppercase_characters(filename)


#Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
def display_words(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()  # Split the line into words
                short_words = [word for word in words if len(word) < 4]
                if short_words:
                    print("Words less than 4 characters:")
                    for word in short_words:
                        print(word)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = "story.txt"
display_words(filename)

