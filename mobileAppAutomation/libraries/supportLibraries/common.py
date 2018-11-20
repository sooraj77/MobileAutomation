import csv
import re

def getDataFromCSV(path_to_csv, sep = ','):
    """
    Function to get test data from CSV file
    """
    try:
        with open(path_to_csv) as csv_file:
            data = [line for line in csv.reader(csv_file, delimiter = sep)]
        return data
    except Exception as exp:
        print "Error reading data from CSV file: {}".format(exp)
        return False

