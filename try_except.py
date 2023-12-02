from meteor_data_class import *
from user_input import *


def try_filter():
    testval = True
    while testval:
        try:
            output = filter_prompter()
            testval = False
            return output
        except ValueError:
            print("\n" + '\033[91m' + "Error: Invalid option" + '\033[0m' + "\n")


def try_file():
    testval = True
    while testval:
        try:
            output = file_prompter()
            testval = False
            return output
        except FileNotFoundError:
            print("\n" + '\033[91m' + "Error: Invalid file" + '\033[0m' + "\n")


def try_option():
    testval = True
    while testval:
        try:
            output = open_option_prompter()
            testval = False
            return output
        except ValueError:
            print("\n" + '\033[91m' + "Error: Invalid option" + '\033[0m' + "\n")


def try_bound(bound_string, filter_name):
    testval = True
    while testval:
        try:
            output = bound_finder(bound_string, filter_name)
            testval = False
            return output
        except ValueError:
            print("\n" + '\033[91m' + "Error: Input is not an integer" + '\033[0m' + "\n")