"""The way main.py interacts with user_input.py is through this file
Filename: try_except.py
Author: Nicholas Young
Date: December 2023"""

from user_input import filter_prompter, file_prompter, open_option_prompter, bound_finder, output_handler
import os


def try_filter():
    """Try to run the filter_prompter, re-prompt endlessly until acceptable input is given

    :return:
    """
    while True:
        try:
            output = filter_prompter()
            return output
        except ValueError as e:
            print("\n" + '\033[91m' + f"{str(e)}" + '\033[0m' + "\n")


def try_file():
    """Try to run the file_prompter, re-prompt endlessly until acceptable input is given

    :return:
    """

    while True:
        try:
            output = file_prompter()
            return output
        except FileNotFoundError as e:
            print("\n" + '\033[91m' + f"{str(e)}" + '\033[0m' + "\n")


def try_option():
    """Try to run the open_option_prompter, re-prompt endlessly until acceptable input is given

    :return:
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
    :return:
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
    :return:
    """

    while True:
        try:
            output = output_handler(meteor_list)
            return output
        except ValueError as e:
            print("\n" + '\033[91m' + f"{str(e)}" + '\033[0m' + "\n")


class InvalidFileError(Exception):
    """Custom exception to handle invalid file errors"""

    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"Error: '{filename}' is not a file")