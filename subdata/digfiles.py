import os
import csv
import pprint

def parse_csv(datafile, lines=10):
    """Parse through a csv file
    and convert the rows to dictionaries.abs
    """

    data = []
    counter = 0

    with open(datafile, 'rt') as sd:
        r = csv.DictReader(sd)
        for line in r:
            if counter == lines:
                break

            data.append(line)
            counter += 1

    pprint.pprint(data)
    return data

