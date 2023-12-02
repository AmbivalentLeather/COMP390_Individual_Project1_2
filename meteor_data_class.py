"""Functions for the meteor_landings_data.txt file
Filename: meteor_data_class.py
Author: Nicholas Young
Date: December 2023"""


def meteor_object_creator(data_list):
    """
    Creates and initializes a meteor object, appends it to output_list

    :param data_list:
    :return:
    """
    meteor_object = MeteorDataEntry(*data_list[:12])
    return meteor_object


def meteor_value_check(data_list, user_input):
    """
    Check if a meteorite in data_list matches the requirements given by user_input

    :param data_list:
    :param user_input:
    :return:
    """
    if data_list[user_input.filter] == '':
        pass
    elif int(float(data_list[user_input.filter])) >= int(float(user_input.lower)):
        if int(float(data_list[user_input.filter])) <= int(float(user_input.upper)):
            return True
        return False


class MeteorDataEntry(object):
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
