#!/usr/bin/env python
# coding: utf-8

# Copyright 2022 by Leipzig University Library, http://ub.uni-leipzig.de
#                   JP Kanter, <kanter@ub.uni-leipzig.de>
#
# This file is part of the Spcht.
#
# This program is free software: you can redistribute
# it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Spcht.  If not, see <http://www.gnu.org/licenses/>.
#
# @license GPL-3.0-only <https://www.gnu.org/licenses/gpl-3.0.en.html>

import os
import sys
import inspect
import logging
import json
import re
from rdflib import Graph, Literal, URIRef

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from Spcht.Core.SpchtCore import Spcht
from Spcht.Utils.local_tools import load_from_json
import Spcht.Core.SpchtUtility as SpchtUtility

"""
This only tests if the actual processing is still working and actually takes place, it does not replace an actual
testing suit that test every function for itself. The featuretest.spcht.json is just featurecomplete und should utilize 
every single datafield that is around which makes it useful to find faults in the programming but is not fit for 
deeper diagnostics or if the data actually processed the right way."""

TEST_DATA = "thetestset.json"
#TEST_DATA = "./../folio_extract.json"
try:
    os.remove("./test_processing.log")
except FileNotFoundError:
    print("No previous log file")
logging.basicConfig(filename='test_processing.log', format='[%(asctime)s] %(levelname)s:%(message)s', level=logging.DEBUG)


def quadro_console_out(quadro_list: list):
    previous = ""
    previous_length = 0
    len_map = {}
    for each in quadro_list:
        if str(each[0]) not in len_map:
            len_map[str(each[0])] = len(str(each[1]))
        if len(str(each[1])) > len_map[str(each[0])]:
            len_map[str(each[0])] = len(str(each[1]))+3
    for each in quadro_list:
        this_line = ""
        if str(each[0]) != previous:
            previous = f"{str(each[0])}"  # tuples cannot be changed
            previous_length = len(previous)
            this_line += f"{previous} "
        else:
            this_line += f"{' '*previous_length} "
        tmp = f"{str(each[1])}"
        this_line += f"{tmp:{len_map[str(each[0])]}}"
        this_line += f"{str(each[2])}"
        print(this_line)


if __name__ == "__main__":
    spcht_path = "featuretest.spcht.json"
    #spcht_path = "./../folio.spcht.json"
    NormalBird = Spcht(spcht_path, schema_path="./../Spcht/SpchtSchema.json", debug=True, log_debug=False)
    my_data = load_from_json(TEST_DATA)
    if not my_data:
        print("Test failed while loading testdata")
        exit(1)
    lines = []
    for every in my_data:
        lines.extend(NormalBird.process_data(every, "https://ressources.info/"))

    quadro_console_out(lines)
    export = SpchtUtility.process2RDF(lines, export=False)
    with open("processing_turtle.ttl", "w") as turtle_file:
        turtle_file.write(export.serialize(format="turtle"))
