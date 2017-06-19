import os
from subdata import digfiles


def main():

    datadir = os.path.dirname(os.path.realpath(__file__))
    datafile = "geochem_example_no_header.csv"

    datafile = os.path.join(datadir, datafile)

    digfiles.parse_csv(datafile)


def test():
    
    root = get_root(article_file)
    data = get_authors(root)


if __name__ == '__main__':
    test()
