"""
Filename: main.py
Author: Nicholas Young
Date: December 2023"""

from meteor_data_class import meteor_object_creator, meteor_value_check
from user_input import output_handler, fill_user_input
from try_except import try_filter, try_file, try_option, try_bound


def main():
    """Filters through user input file and prints a table of meteorites matching specific conditions"""
    welcome_text()

    # Put all the user inputs into variables to then put in a 'user_input' object
    file_name, file_option, meteorite_filter, lower_bound, upper_bound = get_user_input()
    user_input = fill_user_input(file_name, file_option, meteorite_filter, lower_bound, upper_bound)

    meteor_list = filter_meteorite_data(user_input)
    output_handler(meteor_list)


def welcome_text():
    """Prints the welcome text to the terminal"""
    print("Welcome to the meteorite filtering program, where we filter your meteorites according to mass OR year "
          "(given some input)")
    print("Developed by Nick Young")
    print("Released in December of 2023\n")


def get_user_input():
    """Runs all other functions that involve user input"""
    file_name = try_file()
    file_option = try_option()
    meteorite_filter = try_filter()
    lower_bound = try_bound("LOWER", meteorite_filter)
    upper_bound = try_bound("UPPER", meteorite_filter)
    return file_name, file_option, meteorite_filter, lower_bound, upper_bound


def filter_meteorite_data(user_input):
    """Filters through the data provided in the meteorite data file"""
    meteor_list = []

    with open(user_input.name, user_input.option) as meteorite_landings_data_file:
        next(meteorite_landings_data_file)
        for current_line in meteorite_landings_data_file:
            current_line = current_line.strip("\n").split("\t")
            list_filler(current_line, meteor_list, user_input)
            
    return meteor_list


def list_filler(data_list, meteor_list, user_input):
    """Fills the meteor_list with meteor objects that fit user specified requirements"""
    if meteor_value_check(data_list, user_input):
        new_meteorite = meteor_object_creator(data_list)
        meteor_list.append(new_meteorite)


if __name__ == "__main__":
    main()
