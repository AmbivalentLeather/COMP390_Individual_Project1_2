"""Filename: user_input.py
Author: Nicholas Young
Date: October 2023"""
import os.path

from export_class import text_file, terminal, excel_export


def quit_program_gracefully():
    """
    Exits the program with quit(), after printing a goodbye string
    :return:
    """
    print("\nThe program is now exiting... GOODBYE")
    quit()


def file_printer(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())


def bound_finder(upper_or_lower):
    """
        Prints a string, takes an input, quits if Q or q
        Functionally the same as previously used upper/lower_bound finder

        :param upper_or_lower:
        :return:
        """
    input_bound = input("Enter the " + upper_or_lower + " limit (inclusive) for the meteor's MASS (g) ('Q' to QUIT):\t")
    if input_bound == "Q":
        quit_program_gracefully()
    elif input_bound == "q":
        quit_program_gracefully()

    return input_bound


def welcome_text():
    print("Welcome to the meteorite filtering program, where we filter your meteorites according to mass OR year "
          "(given some input)")
    print("Developed by Nick Young")
    print("Released in October of 2023\n")


def file_prompter():
    """
    Prompts the user for the name of a file to parse through
    :return:
    """

    truth_tester = True
    while truth_tester:
        try:
            user_file_input = input(
                "Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) "
                "|or| \nEnter \">q\" or \">Q\" to quit:\t")
            # Attempt to open the file (this will raise FileNotFoundError if the file doesn't exist)
            with open(user_file_input):
                pass
            truth_tester = False
        except FileNotFoundError:
            print(f"Error: '{user_file_input}' does not exist.")

    if user_file_input == ">q":
        quit_program_gracefully()
    elif user_file_input == ">Q":
        quit_program_gracefully()
    else:
        print("\n" + '\033[92m' + "Target File: " + user_file_input + '\033[0m' + "\n")
        return user_file_input


def open_option_prompter():
    """
    Prints request for which mode to open a file with, takes user input()
    :return:
    """
    file_printer("file_open_options.txt")
    user_option_input = input("Mode >> ")

    if user_option_input == ">q":
        quit_program_gracefully()
    elif user_option_input == ">Q":
        quit_program_gracefully()

    print("\n" + '\033[92m' + "File mode: " + user_option_input + '\033[0m' + "\n")
    return user_option_input


def filter_prompter():
    """
    Prints request for which column of the file to sort for, takes user input()
    :return:
    """
    user_filter_input = input("What attribute would you like to filter the data on?\n"
                              "1. meteor MASS (g)\n"
                              "2. The YEAR the meteor fell to Earth\n"
                              "3. QUIT\n"
                              ">>\t")
    if user_filter_input == "1":
        return 'mass'
    elif user_filter_input == "2":
        return 'year'
    elif user_filter_input == "3":
        quit_program_gracefully()
    else:
        print('Invalid option')


def output_handler(list_sort, data_value_list):
    """Prints request for which type of output the program should provide, takes user input()"""
    user_output_selection = input("How would you like to output the filter results?\n"
                                  "1. On screen (in terminal)\n"
                                  "2. To a TEXT file\n"
                                  "3. To an EXCEL file\n"
                                  "4. QUIT\n>> ")
    if user_output_selection == "1":
        terminal(list_sort, data_value_list)
    elif user_output_selection == "2":
        text_file(data_value_list)
    elif user_output_selection == "3":
        excel_export(data_value_list)
    elif user_output_selection == "4":
        quit_program_gracefully()
