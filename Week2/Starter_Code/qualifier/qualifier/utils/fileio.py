# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        count = 0
        global header
        #next(csvreader)

        # Read the CSV data
        for row in csvreader:
            if count == 0:
                header = row
                count += 1
            else:
                data.append(row)
    return data


def save_csv(csvpath, data):
    """Writes the data to csv file
    """
    with open(csvpath, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        dlen = len(data)
        global header
        csvwriter.writerow(header)
        for i in range(0, dlen):
            csvwriter.writerow(data[i])

