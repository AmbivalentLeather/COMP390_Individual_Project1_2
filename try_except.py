"""The way main.py interacts with user_input.py is through this file
Filename: try_except.py
Author: Nicholas Young
Date: December 2023"""

from user_input import (filter_prompter, file_prompter, open_option_prompter, bound_finder, output_handler,
                        file_contents_tester, quit_program_gracefully)
import os


def try_filter():
    """Try to run the filter_prompter, re-prompt endlessly until acceptable input is given

    :return: The output of filter_prompter()
    """
    while True:
        try:
            output = filter_prompter()
            return output
        except ValueError as e:
            print("\n" + '\033[91m' + f"{str(e)}" + '\033[0m' + "\n")


def try_file():
    """Try to run the file_prompter, re-prompt endlessly until acceptable input is given

    :return: The output of file_prompter()
    """
    while True:
        try:
            output = file_prompter()
            return output
        except FileNotFoundError as e:
            print("\n" + '\033[91m' + f"{str(e)}" + '\033[0m' + "\n")


def try_file_contents(file_name):
    """Try to read the nextline of a file, re-prompt endlessly until a file with contents is given

    :return: The output of file_prompter()
    """
    try:
        output = file_contents_tester(file_name)
        return output
    except FileNotFoundError as e:
        print("\n" + '\033[91m' + f"{str(e)}" + '\033[0m' + "\n")
        quit_program_gracefully()


def try_option():
    """Try to run the open_option_prompter, re-prompt endlessly until acceptable input is given

    :return: The output of open_option_prompter()
    """
    while True:
        try:
            output = open_option_prompter()
            return output
        except ValueError as e:
            print("\n" + '\033[91m' + f"{str(e)}" + '\033[0m' + "\n")


def try_bound(bound_string, filter_name):
    """Try to run bound_finder, re-prompt endlessly until acceptable input is given

    :param bound_string:
    :param filter_name:
    :return: The output of bound_finder(bound_string, filter_name)
    """

    while True:
        try:
            output = bound_finder(bound_string, filter_name)
            return output
        except TypeError as e:
            print("\n" + '\033[91m' + f"{str(e)}" + '\033[0m' + "\n")


def try_output(meteor_list):
    """Try to run output_handler, re-prompt endlessly until acceptable input is given

    :param meteor_list:
    :return: The output of output_handler(meteor_list)
    """

    while True:
        try:
            output = output_handler(meteor_list)
            return output
        except ValueError as e:
            print("\n" + '\033[91m' + f"{str(e)}" + '\033[0m' + "\n")
