#!/usr/bin/env python

import xml.etree.ElementTree as ET
import pprint
import os


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_wells(root):
    wells = []
    for well in root.findall('./entries/entry/'):
        data = {
                "wlbFacilityTypeDrilling": None,
                "wlbAgeAtTd": None,
                "wlbDrillingDays": None
        }
        data["wlbFacilityTypeDrilling"] = well.find('./wlbFacilityTypeDrilling').text
        data["wlbAgeAtTd"] = well.find('./wlbAgeAtTd').text
        data["wlbDrillingOperator"] = well.find('./wlbDrillingOperator').text

        wells.append(data)

    return wells


datadir = os.path.dirname(os.path.realpath(__file__))
xml_file = "exploration.xml"
datafile = os.path.join(datadir, xml_file)


def test():

    root = get_root(xml_file)
    data = get_wells(root)

    pprint.pprint(data)


test()
