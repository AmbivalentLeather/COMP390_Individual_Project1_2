"""Filename: try_except.py
Author: Nicholas Young
Date: December 2023"""

from user_input import *


def try_filter():
    """Try to run the filter_prompter, re-prompt endlessly until acceptable input is given"""
    testval = True
    while testval:
        try:
            output = filter_prompter()
            testval = False
            return output
        except ValueError:
            print("\n" + '\033[91m' + "Error: Invalid option" + '\033[0m' + "\n")


def try_file():
    """Try to run the file_prompter, re-prompt endlessly until acceptable input is given"""

    testval = True
    while testval:
        try:
            output = file_prompter()
            testval = False
            return output
        except FileNotFoundError:
            print("\n" + '\033[91m' + "Error: Invalid file" + '\033[0m' + "\n")


def try_option():
    """Try to run the open_option_prompter, re-prompt endlessly until acceptable input is given"""

    testval = True
    while testval:
        try:
            output = open_option_prompter()
            testval = False
            return output
        except ValueError:
            print("\n" + '\033[91m' + "Error: Invalid option" + '\033[0m' + "\n")


def try_bound(bound_string, filter_name):
    """Try to run bound_finder, re-prompt endlessly until acceptable input is given"""

    testval = True
    while testval:
        try:
            output = bound_finder(bound_string, filter_name)
            testval = False
            return output
        except ValueError:
            print("\n" + '\033[91m' + "Error: Input is not an integer" + '\033[0m' + "\n")