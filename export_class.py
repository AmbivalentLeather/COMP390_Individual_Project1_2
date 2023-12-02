"""Filename: export_class.py
Author: Nicholas Young
Date: December 2023"""

from datetime import datetime
from xlwt import Workbook


def get_clean_datetime_string():
    """Returns the current year, month, day, hour, minute, second, and microsecond as a string"""
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str


def terminal(data_list):
    """
    Print the filtered data to the terminal

    :param data_list:
    :return:
    """
    column_headers = ["Name", "Id", "Name Type", "Recorded Class", "Mass", "Fall", "Year", "Rec Lat", "Rec Long",
                      "Geolocation", "States", "Counties"]
    formatted_string = ("\t{:<24}\t{:<24}\t{:<24}\t{:<24}\t{:<24}\t{:<24}\t{:<24}\t{:<24}\t{:<24}\t{:<24}\t{:<24}\t{"
                        ":<24}").format(*column_headers)
    print(formatted_string)
    print('=' * 325)
    for index, meteor in enumerate(data_list, 1):
        print(f'{index}\t{meteor.name:<24}\t{meteor.id:<24}\t{meteor.nameType:<24}\t{meteor.recordedClass:<24}\t'
              f'{meteor.mass:<24}\t{meteor.fall:<24}\t{meteor.year:<24}\t{meteor.recordedLatitude:<24}\t'
              f'{meteor.recordedLongitude:<24}\t{meteor.geolocation:<24}\t{meteor.states:<24}\t{meteor.counties:<24}')


def text_file(data_list):
    """Output the filtered data to a txt file"""
    file = open(get_clean_datetime_string() + ".txt", "x")

    file.write("Name\tId\tName Type\tRecorded Class\tMass\tFall\tYear\tRec Lat"
               "\tRec Long\tGeolocation\tStates\tCounties\n")
    for index, meteor in enumerate(data_list, 1):
        file.write(f'{index}\t{meteor.name}\t{meteor.id}\t{meteor.nameType}\t{meteor.recordedClass}\t'
              f'{meteor.mass}\t{meteor.fall}\t{meteor.year}\t{meteor.recordedLatitude}\t'
              f'{meteor.recordedLongitude}\t{meteor.geolocation}\t{meteor.states}\t{meteor.counties}\n')


def excel_export(meteor_list):
    """Output the filtered data to an xls file"""
    excel_workbook = Workbook()
    filtered_data_sheet = excel_workbook.add_sheet('filteredMeteoriteData')

    append_header(filtered_data_sheet)
    append_meteorites(filtered_data_sheet, meteor_list)

    clean_timestamp_str = get_clean_datetime_string()
    excel_workbook.save(f'{clean_timestamp_str}.xls')
    # confirmation message
    print(f'\n\033[92mFiltered output sent to "{clean_timestamp_str}.xls"\033[0m')


def append_meteorites(filtered_data_sheet, meteor_list):
    """Append to the filtered_data_sheet every object in the meteor_list"""
    for filtered_index in range(len(meteor_list)):
        current_meteorite_record_obj = meteor_list[filtered_index]

        attribute_list = current_meteorite_record_obj.get_values()
        for attr_index in range(len(attribute_list)):
            filtered_data_sheet.write(filtered_index + 1, attr_index, attribute_list[attr_index])


def append_header(filtered_data_sheet):
    """Append the column headers/titles to the filtered_data_sheet. It may be called append but it appends to the
    firs row only"""
    column_headers = ["Name", "Id", "Name Type", "Recorded Class", "Mass", "Fall", "Year", "Rec Lat", "Rec Long",
                      "Geolocation", "States", "Counties"]
    index = 0
    for name in column_headers:
        filtered_data_sheet.write(0, index, name)
        index += 1