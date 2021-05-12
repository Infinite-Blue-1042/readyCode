# readyCode package module source code by Aarin Dave.

# Email aarindave@gmail.com for questions, bugs, complaints, and suggestions for the
# readyCode module.

# WARNING! DO NOT TOUCH OR MODIFY ANYTHING IN THE SOURCE CODE! PLEASE EMAIL THE ABOVE EMAIL ADDRESS TO
# REPORT A BUG!

# Variables

ascii_chars = "".join(chr(char) for char in range(32, 127))
phi = (1 + 5 ** 0.5) / 2

# Classes

class var:
    def __init__(type, content, name):
        self.type = null
        self.content = null
        self.name = null
    
    def rename(name_3):
        self.name = name
    
    def retype(type_2):
        self.type = type
     
    def renter(content_1):
        self.content = content

# Functions


def close_files(*files):
    """
    close_files() closes all the given files

    Syntax:
    close_files(file1, file2, file3, ...)

    Example usage:

    from readyCode package import close_files

    file1 = open("file1.txt")
    file2 = open("file2.txt")

    close_files(file1, file2)  # Closes both files

    Possible errors:
    If given a file that does not exist, it will raise an error.
    """
    try:
        for file in files:
            with open(file):
                pass
    except FileNotFoundError:
        exit("Error: File does not exist")


def get_keys(dictionary: dict, value):
    """
    get_keys() collects all the keys that share a value

    Syntax:
    get_keys(dictionary, value)

    Example usage:

    from readyCode package import get_keys

    d = {"Alice": 45, "Bob": 25, "Charlie": 45, "Doug": 15, "Ellie": 75}

    keys_with_45 = get_keys(d, 45)
    print(keys_with_45)  # Prints ["Alice", "Charlie"]

    Possible errors:
    If the given iterable is not a dictionary or 2D list, it will raise an error.
    """
    dictionary = dict(dictionary)
    if type(dictionary) != dict:
        exit("Error: not given a dictionary")
    return [key for key in dictionary if dictionary[key] == value]


# def file_exists(f, iterable):
#     """
#     file_exists() searches if a given file exists
#
#     Syntax:
#     file_exists(file)
#     """
#     from os import listdir, path
#     files = sorted(
#         [f"{folder}/{file}" for folder in iterable if path.isdir(folder) for file in listdir(folder) if file[0] != "."])
#     if any(f in file for file in files):
#         return True
#     elif not files:
#         return False
#     else:
#         return file_exists(f, files)


def inputs(*strings):
    """
    inputs() asks the user for multiple inputs

    Syntax:
    inputs(input1, input2, input3, ...)

    Example usage:

    name, age, gender = inputs("What is your name? ", "What is your age? ", "What is your gender? ")
    # Assume the user typed in John, 30, and male respectively.
    print(name)  # Prints "John"
    print(age)  # Prints 30
    print(gender)  # Prints "male"

    Possible errors:
    No errors spotted
    """
    responses = [input(string) for string in strings]
    return responses


# def open_files(**files):
#     pass


def random_string(lower_limit=None, upper_limit=None, step=None):
    """
    random_string() returns a random string

    Syntax:
    random_string(shortest_length, longest_length, step)

    Example usage:

    from readyCode package import random_string

    print(random_string())  # This gives a random string with a length between 50 and 100, inclusive
    print(random_string(1, 100))  # Returns a random string with a length between 1 and 100, inclusive
    print(random_string(10, 20, 2))  # Returns a random string with an even length between 10 and 20, inclusive

    Possible errors:
    If the values given are not numerical strings or integers, it will raise an error.
    """
    from secrets import choice

    specs = list(map(lambda x: int(x), filter(None, [lower_limit, upper_limit, step])))

    if not specs:
        specs = [50, 100]
    elif specs.count(specs[0]) == len(specs):
        specs = specs[:2]
        specs[1] += 1
    return "".join(choice(ascii_chars) for _ in range(choice(range(*specs))))


def remove_duplicates(iterable):
    """
    remove_duplicates() returns a random string

    Syntax:
    remove_duplicates(iterable)

    Example usage:

    from readyCode package import remove_duplicates

    print(remove_duplicates("readyCode package"))  # Returns "readyCo" because "d" and "e" are duplicates
    print(remove_duplicates(["1", "1", "2", "3", "3", "3"]))  # Returns ["1", "2", "3"]

    Possible errors:
    If given a list with at least one integer, it will return an error.
    """
    if type(iterable) == int:
        iterable = str(iterable)

    filtered_list = []
    for char in iterable:
        if char not in filtered_list:
            filtered_list.append(char)

    if type(iterable) == str:
        return "".join(filtered_list)
    else:
        return filtered_list


def remove_line(file, line):
    """
    remove_line() removes a given line in a given file

    Syntax:
    remove_line(filename, line_number or line_string)

    Example usage:

    from readyCode package import remove_line

    file1 = open("file1.txt")  # The file has ten lines.

    remove_line(file1, 5)  # This removes the sixth line.
    remove_line(file1, -1)  # This removes the last line.
    remove_line(file1, 0) # This removes the first line.

    for line in file1:
        if line.strip() == "readyCode package":
            remove_line(file1, line)  # You can also provide a string.

    Possible errors:
    If the given line number is larger than the amount of lines in a file, it will remove the last line.
    """
    file = file.name
    lines = open(file).readlines()
    if type(line) == int:
        lines.pop(line if line < len(lines) else -1)
    elif type(line) == str:
        lines.remove(line)
    with open(file, "w") as f:
        for line_ in lines:
            f.write(line_)


def int_input(message):
    return int(input(message))


def sort_dict(dictionary, key=True, reverse=False):
    return dict(sorted(dictionary.items, key=lambda x: x[1-key], reverse=reverse))
