"""Functions for the meteor_landings_data.txt file
Filename: meteor_data_class.py
Author: Nicholas Young
Date: October 2023"""

from pathlib import Path


def meteor_object_creator(data_value_list, output_list):
    """
    Creates and initializes a meteor object, appends it to output_list

    :param data_value_list:
    :param output_list:
    :return:
    """
    meteor_object = MeteorDataEntry(*data_value_list[:12])
    output_list.append(meteor_object)


def meteor_value_check(data_value_list, list_index, lower_bound, upper_bound):
    """
    Check if data_value_list has a value in the index at input_list_number, and return true if it does

    :param data_value_list:
    :param list_index:
    :param lower_bound:
    :param upper_bound:
    :return:
    """
    if data_value_list[list_index] == '':
        pass
    elif int(float(data_value_list[list_index])) >= int(float(lower_bound)):
        if int(float(data_value_list[list_index])) <= int(float(upper_bound)):
            return True
        return False


def which_meteorite_element(element):
    """Maps a provided element to its associated number."""
    element = element.lower()
    element_mapping = {
        'name': 0,
        'id': 1,
        'nametype': 2,
        'recclass': 3,
        'mass': 4,
        'fall': 5,
        'year': 6,
        'reclat': 7,
        'reclong': 8,
        'geolocation': 9,
        'states': 10,
        'counties': 11
    }

    element_index = element_mapping.get(element)
    if element_index is not None:
        return element_index

    print('No element provided')
    exit()


class MeteorDataEntry:
    """This class is used to initialize a meteor object"""

    def __init__(self, name, identifier, name_type, recorded_class, mass, fall, year,
                 recorded_latitude, recorded_longitude,
                 geolocation, states, counties):
        self.name = name
        self.id = identifier
        self.nameType = name_type
        self.recordedClass = recorded_class
        self.mass = mass
        self.fall = fall
        self.year = year
        self.recordedLatitude = recorded_latitude
        self.recordedLongitude = recorded_longitude
        self.geolocation = geolocation
        self.states = states
        self.counties = counties
