from meteor_data_class import (meteor_object_creator, meteor_value_check, meteor_print_table, which_meteorite_element)
from user_input import (bound_finder, welcome_text, file_prompter, open_option_prompter, filter_prompter)

"""
Written by Nicholas Young
Written in October 2023
"""


def main():
    """Filters through user input file and prints a table of meteorites matching specific conditions"""
    welcome_text()
    file_name, file_option, meteorite_filter, lower_bound, upper_bound = get_user_inputs()
    meteor_list = filter_meteorite_data(file_name, file_option, meteorite_filter, lower_bound, upper_bound)
    print_meteor_table(meteorite_filter, meteor_list)


def get_user_inputs():
    file_name = file_prompter()
    file_option = open_option_prompter()
    meteorite_filter = filter_prompter()
    lower_bound = bound_finder("LOWER")
    upper_bound = bound_finder("UPPER")
    return file_name, file_option, meteorite_filter, lower_bound, upper_bound


def filter_meteorite_data(file_name, file_option, meteorite_filter, lower_bound, upper_bound):
    meteor_list = []

    with open(file_name, file_option) as meteorite_landings_data_file:
        next(meteorite_landings_data_file)

        for current_line in meteorite_landings_data_file:
            data_field_value_list = current_line.strip("\n").split("\t")

            if should_include_meteorite(data_field_value_list, meteorite_filter, lower_bound, upper_bound):
                meteor_object_creator(data_field_value_list, meteor_list)

    return meteor_list


def should_include_meteorite(data_field_value_list, meteorite_filter, lower_bound, upper_bound):
    meteor_value = which_meteorite_element(meteorite_filter)
    return meteor_value_check(data_field_value_list, meteor_value, lower_bound, upper_bound)


def print_meteor_table(meteorite_filter, meteor_list):
    column_name = 'MASS (g)' if meteorite_filter == 'mass' else 'YEAR'
    meteor_print_table(column_name, meteor_list)


if __name__ == "__main__":
    main()
