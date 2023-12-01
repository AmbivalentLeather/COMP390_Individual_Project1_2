"""Filename: user_input.py
Author: Nicholas Young
Date: October 2023"""


def quit_program_gracefully():
    """
    Exits the program with quit(), after printing a goodbye string
    :return:
    """
    print("\nThe program is now exiting... GOODBYE")
    quit()


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
    user_file_input = input("Enter a valid file name (ex. \"file_name.txt\") with its file extension (if applicable) "
                            "|or| \nEnter \">q\" or \">Q\" to quit:\t")
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
    user_option_input = input("What mode would you like to open the file with?\n"
                              "\"r\" - open for reading (default)\n"
                              "\"W\" - open for writing, truncating the file first\n"
                              "\"X\" - open for exclusive creation, failing if the file already exists\n"
                              "\"a\" - open for writing, appending to the end of file if it exists\n"
                              "\"b\" - binary mode\n"
                              "\"t\" - text mode (default)\n"
                              "\"+\" - open for updating (reading and writing)\n"
                              "Enter \">q\" or \">Q\" to quit\n"
                              "Mode ->\t")
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