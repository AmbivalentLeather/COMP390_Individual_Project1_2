![Static Badge](https://img.shields.io/badge/project-Finished-green)
![Static Badge](https://img.shields.io/badge/units-Tested-green)
![Static Badge](https://img.shields.io/badge/hotel-Trivago-green)

# Project Information

Written By: Nicholas Young

COMP 390-002

This project takes user input in the terminal, and provides options for filtering a given data set, as well as options for output of the filtered information

[Github Repo Link](https://github.com/AmbivalentLeather/COMP390_Individual_Project1_2)

## Required libraries
os

path

xlwt

datetime

pytest

# User guide

To interact with this program run the main.py file in pycharm. There is a meteorite_landings_data.txt file included in the git repository that can be used to test this program.

__Note: Every prompt has a prompt-specific option to quit the program safely. Each prompt describes how to do this in the prompt__

The __first__ prompt expects the user to input the name of a file in the same directory as the main.py file OR the path to a file relative to the main.py file

The __second__ prompt expects the user to select an option to open the file with. Either (r)ead, (w)rite, e(x)clusively create, and (a)ppend. In this version of the program, the only option that is functional--or useful for that matter--for the user is (r)ead.

The __third__ prompt asks for the user to filter the provided data (from the first step) by either the MASS or YEAR column.

The __fourth & fifth__ prompts ask the user for the LOWER and UPPER limits to sort the data for. These limits are inclusive. 
For example, if a user enters 1000 for the LOWER limit while filtering for MASS, the smallest number the MASS column can contain is 1000.

The __final__ prompt asks the user to select a method of output for the filtered data.

Terminal -> Outputs to the terminal in formatted columns

TEXT file -> Outputs into a tab seperated (txt) file named with the ISO 8601 date and time

EXCEL file -> Outputs into an Excel (xls) file, also named with the ISO 8601 date and time

# Steps completed

All steps have been completed.
