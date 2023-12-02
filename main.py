from meteor_data_class import meteor_object_creator, meteor_value_check, which_meteorite_element
from user_input import (bound_finder, welcome_text, file_prompter, open_option_prompter,
                        filter_prompter, output_handler, fill_user_input)

"""
Written by Nicholas Young
Written in December 2023
"""


def main():
    """Filters through user input file and prints a table of meteorites matching specific conditions"""
    welcome_text()

    # Put all the user inputs into variables to then put in a 'user_input' object
    file_name, file_option, meteorite_filter, lower_bound, upper_bound = get_user_input()
    user_input = fill_user_input(file_name, file_option, meteorite_filter, lower_bound, upper_bound)

    meteor_list = filter_meteorite_data(user_input)
    output_handler(meteorite_filter, meteor_list)


def get_user_input():
    file_name = file_prompter()
    file_option = open_option_prompter()
    meteorite_filter = filter_prompter()
    lower_bound = bound_finder("LOWER", meteorite_filter)
    upper_bound = bound_finder("UPPER", meteorite_filter)
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
    if meteor_value_check(data_list, user_input):
        new_meteorite = meteor_object_creator(data_list)
        meteor_list.append(new_meteorite)


if __name__ == "__main__":
    main()
