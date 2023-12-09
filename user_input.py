"""Manage all user input. This file contains functions and a user_input object
Filename: user_input.py
Author: Nicholas Young
Date: December 2023"""

from export_class import terminal, text_file_export, excel_export
from pathlib import Path


def quit_program_gracefully():
    """After printing a "goodbye" string, exits the program with quit().

    This function should be called at every opportunity a user has to input.
    :return:
    """
    print("\nThe program is now exiting... GOODBYE")
    quit()


def file_printer(filename):
    """Print the contents of a file to the terminal

    :param filename: The name of the file to be printed
    :return:
    """
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())


def bound_finder(upper_or_lower, mass_or_year):
    """Return the user input "input_bound" if it is an integer.

    The inputs upper_or_lower and mass_or_year only effect the appearance of the string printed for the user.


    :param upper_or_lower: Either "LOWER" or "UPPER"
    :param mass_or_year: Either the integer 4, or the integer 6
    :return:
    """
    column = 'MASS (g)' if mass_or_year == 4 else 'YEAR'
    input_bound = input("Enter the " + upper_or_lower + " limit (inclusive) for the meteor's " +
                        column + " ('Q' to QUIT):\t")
    quit_program_gracefully() if input_bound == "Q" else None
    return is_integer(input_bound)


def is_integer(input_bound):
    """Return the input parameter if it is an integer, raises a TypeError otherwise

    :param input_bound:
    :return:
    """
    if input_bound.isdigit():
        return input_bound
    else:
        raise TypeError(f"Error: Invalid range limit '{input_bound}'")


def file_prompter():
    """Prompts the user for the name of a file to parse through

    :return:
    """

    user_file_input = input("Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) "
                            "|or| \nEnter \">q\" or \">Q\" to quit:\t")

    quit_program_gracefully() if user_file_input.lower() == ">q" else None
    file_presence_tester(user_file_input)

    print("\n" + '\033[92m' + "Target File: " + user_file_input + '\033[0m' + "\n")
    return user_file_input


def file_presence_tester(user_file_input):
    """Does nothing if a file (passed as a parameter) exists. Raises FileNotFoundError if it doesn't.

    :param user_file_input:
    :return: Hopefully, nothing.
    """
    if not user_file_input:
        raise FileNotFoundError(f"Error: The file '{user_file_input}' does not exist")

    file_path = Path(user_file_input)
    if file_path.exists():
        pass
    else:
        raise FileNotFoundError(f"Error: The file '{user_file_input}' does not exist")


def open_option_prompter():
    """Prints request for which mode to open a file with, takes user input()

    :return: If valid, the user input is returned as given
    """
    file_printer("file_open_options.txt")
    user_option_input = input("Mode >> ")

    quit_program_gracefully() if user_option_input.lower() == ">q" else None

    if (user_option_input.lower() != "r" and user_option_input.lower() != "w" and
            user_option_input.lower() != "x" and user_option_input.lower() != "a"):
        raise ValueError(f"Error: Invalid input '{user_option_input}'")

    print("\n" + '\033[92m' + "File mode: " + user_option_input + '\033[0m' + "\n")
    return user_option_input


def filter_prompter():
    """Prints request for which column of the file to sort for, takes user input

    :return: The meteor list item that the user selected
    """
    file_printer("filter_prompt_text.txt")
    user_filter_input = input(">>\t")
    if user_filter_input == "1":
        return 4
    elif user_filter_input == "2":
        return 6
    elif user_filter_input == "3":
        quit_program_gracefully()
    else:
        raise ValueError(f"Error: Invalid option '{user_filter_input}'")


def output_handler(data_value_list):
    """
    Prints request for which type of output the program should provide, takes user input(). Then passes
    that selection into selected_output()

    :param data_value_list: The list of data that will be sent to selected_output
    :return:
    """
    file_printer("output_selection_text.txt")
    user_output_selection = input(">>\t")
    selected_output(user_output_selection, data_value_list)


def selected_output(user_output_selection, data_value_list):
    """
    Based on the user input (passed as a parameter), this function either sends the output to the terminal, a text
    file, or an Excel spreadsheet (with an option to quit the program entirely). If none of the above, the function
     raises a ValueError

    :param user_output_selection: The user selection to determine which output to chose
    :param data_value_list: The list to be output
    :return:
    """
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
    """ Fills the UserInput object

    :param name:
    :param option:
    :param file_filter:
    :param lower:
    :param upper:
    :return:
    """
    user_input = UserInput(name, option, file_filter, lower, upper)
    return user_input


class UserInput(object):
    """An object to store the input of users in a more portable way"""

    def __init__(self, name, option, file_filter, lower, upper):
        """Instantiates the UserInput object

        :param name: The name of the file the user chooses
        :param option: The option to open the file
        :param file_filter: Which column to sort for, either MASS or YEAR in this case
        :param lower: The lower bound of the column sort
        :param upper: The upper bound of the column sort
        """
        self.name = name
        self.option = option
        self.filter = file_filter
        self.lower = lower
        self.upper = upper
