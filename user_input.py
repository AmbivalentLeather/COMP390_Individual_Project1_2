"""Manage user input
Filename: user_input.py
Author: Nicholas Young
Date: December 2023"""

from export_class import terminal, text_file_export, excel_export
from pathlib import Path


def quit_program_gracefully():
    """
    Exits the program with quit(), after printing a goodbye string
    :return:
    """
    print("\nThe program is now exiting... GOODBYE")
    quit()


def file_printer(filename):
    """Prints the contents of a file to the terminal
    Intended to be used for long user input strings"""
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())


def bound_finder(upper_or_lower, mass_or_year):
    """
        Prints a string, takes an input, quits if Q or q
        Functionally the same as previously used upper/lower_bound finder

        :param mass_or_year:
        :param upper_or_lower:
        :return:
        """
    column = 'MASS (g)' if mass_or_year == 4 else 'YEAR'
    input_bound = input("Enter the " + upper_or_lower + " limit (inclusive) for the meteor's " +
                        column + " ('Q' to QUIT):\t")
    quit_program_gracefully() if input_bound.lower() == "q" else None
    return is_integer(input_bound)


def is_integer(input_bound):
    if input_bound.isdigit():
        return input_bound
    else:
        raise TypeError(f"Error: '{input_bound}' is not an integer")


def file_prompter():
    """
    Prompts the user for the name of a file to parse through
    :return:
    """

    user_file_input = input("Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) "
                            "|or| \nEnter \">q\" or \">Q\" to quit:\t")

    quit_program_gracefully() if user_file_input.lower() == ">q" else None
    file_presence_tester(user_file_input)

    print("\n" + '\033[92m' + "Target File: " + user_file_input + '\033[0m' + "\n")
    return user_file_input


def file_presence_tester(user_file_input):
    # Attempt to open the file (this will raise FileNotFoundError if the file doesn't exist)
    if not user_file_input:
        raise FileNotFoundError(f"Error: The file '{user_file_input}' does not exist")

    file_path = Path(user_file_input)
    if file_path.exists():
        pass
    else:
        raise FileNotFoundError(f"Error: The file '{user_file_input}' does not exist")


def open_option_prompter():
    """
    Prints request for which mode to open a file with, takes user input()
    :return:
    """
    file_printer("file_open_options.txt")
    user_option_input = input("Mode >> ")

    if user_option_input.lower() == ">q":
        quit_program_gracefully()

    if (user_option_input.lower() != "r" and user_option_input.lower() != "w" and
            user_option_input.lower() != "x" and user_option_input.lower() != "a"):
        raise ValueError(f"Error: Invalid input '{user_option_input}'")

    print("\n" + '\033[92m' + "File mode: " + user_option_input + '\033[0m' + "\n")
    return user_option_input


def filter_prompter():
    """
    Prints request for which column of the file to sort for, takes user input
    :return:
    """
    user_filter_input = input("What attribute would you like to filter the data on?\n"
                              "1. meteor MASS (g)\n"
                              "2. The YEAR the meteor fell to Earth\n"
                              "3. QUIT\n"
                              ">>\t")
    while True:
        if user_filter_input == "1":
            return 4
        elif user_filter_input == "2":
            return 6
        elif user_filter_input == "3":
            quit_program_gracefully()
        else:
            raise ValueError(f"Error: Invalid option '{user_filter_input}'")


def output_handler(data_value_list):
    """Prints request for which type of output the program should provide, takes user input()"""
    user_output_selection = input("How would you like to output the filter results?\n"
                                  "1. On screen (in terminal)\n"
                                  "2. To a TEXT file\n"
                                  "3. To an EXCEL file\n"
                                  "4. QUIT\n>> ")
    if user_output_selection == "1":
        terminal(data_value_list)
    elif user_output_selection == "2":
        text_file_export(data_value_list)
    elif user_output_selection == "3":
        excel_export(data_value_list)
    elif user_output_selection == "4":
        quit_program_gracefully()
    else:
        raise ValueError(f"Error: Invalid option '{user_output_selection}'")


def fill_user_input(name, option, file_filter, lower, upper):
    """Fills the UserInput object"""
    user_input = UserInput(name, option, file_filter, lower, upper)
    return user_input


class UserInput(object):
    """An object to store the input of users more portably"""

    def __init__(self, name, option, file_filter, lower, upper):
        self.name = name
        self.option = option
        self.filter = file_filter
        self.lower = lower
        self.upper = upper
