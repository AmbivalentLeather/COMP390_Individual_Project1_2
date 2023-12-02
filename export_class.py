from datetime import datetime
from xlwt import Workbook


def get_clean_datetime_string():
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str


def text_file(data_value_list):
    f = open(get_clean_datetime_string() + ".txt", "x")
    for index, meteor in enumerate(data_value_list, 1):
        f.write(f'{index}\t{meteor.name}\t{meteor.id}\t{meteor.nameType}\t{meteor.recordedClass}\t'
              f'{meteor.mass}\t{meteor.fall}\t{meteor.year}\t{meteor.recordedLatitude}\t'
              f'{meteor.recordedLongitude}\t{meteor.geolocation}\t{meteor.states}\t{meteor.counties}\n')


def terminal(value_label, data_value_list):
    """
    Prints meteor objects in given list

    :param value_label:
    :param data_value_list:
    :return:
    """
    # Print header names here
    print('=' * 315)
    for index, meteor in enumerate(data_value_list, 1):
        print(f'{index}\t{meteor.name:<24}\t{meteor.id:<24}\t{meteor.nameType:<24}\t{meteor.recordedClass:<24}\t'
              f'{meteor.mass:<24}\t{meteor.fall:<24}\t{meteor.year:<24}\t{meteor.recordedLatitude:<24}\t'
              f'{meteor.recordedLongitude:<24}\t{meteor.geolocation:<24}\t{meteor.states:<24}\t{meteor.counties:<24}')


def excel_export(data_value_list):
    pass

"""
def write_filtered_results_to_excel_file():
    # Workbook is created
    excel_workbook = Workbook()
    # add a sheet to the workbook
    filtered_data_sheet = excel_workbook.add_sheet('filteredMeteoriteData')

    # write the attribute titles to the top of the sheet
    index = 0
    for name in attribute name list [‘name’, ‘id’, ‘nametype’, …]:
        # write top row of the Excel output sheet -- __.write(row, column, value)
        filtered_data_sheet.write(0, index, name)
        index++

    # loop through all the filtered meteorite objects
    for index in range(len(filtered_meteorite_object_list):
        # get the current meteorite object
        current_meteorite_record_obj = filtered_meteorite_object_list[index]
        # get a Python list with all 12 of the current meteorite object's attributes
        # extract_data_from_meteorite_object() should return a list of 12 values
        attribute_list = extract_data_from_meteorite_object()
        # loop through the attribute strings in the attribute list
        for attr_index in range(len(attribute_list)):
            # write each row of the Excel output sheet -- __.write(row, column, value)
            filtered_data_sheet.write(index + 1, attr_index, attribute_list[attr_index])

    clean_timestamp_str = get_clean_datetime_string()
    excel_workbook.save(f'{clean_timestamp_str}.xls')
    # confirmation message
    print(f'\n\033[92mFiltered output sent to "{clean_timestamp_str}.xls"\033[0m')
"""