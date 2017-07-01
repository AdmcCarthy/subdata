import os
from subdata import digfiles


def main():

    datadir = os.path.dirname(os.path.realpath(__file__))
    datafile = "geochem_example_no_header.csv"

    datafile = os.path.join(datadir, datafile)

    digfiles.parse_csv(datafile)


if __name__ == '__main__':
    main()
