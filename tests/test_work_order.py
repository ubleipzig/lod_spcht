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

import json
import os

import SpchtCore.WorkOrder as WorkOrder
import Utils.local_tools as local_tools


"""
I am not very sure if i really want to do this as unit test, especially cause half of those tests are only possible
if you actually have a running virtuoso server with the right credentials
"""

try:
    with open("work_order_sets.json", "r") as all_orders:
        ORDERS = json.load(all_orders)
except json.JSONDecodeError as e:
    print(e)
except OSError as osi:
    print(osi.errno, " - ", osi)

with open("temp_throwaway.json", "w") as temp_file:
    json.dump(ORDERS['status0'], temp_file)
WorkOrder.CheckWorkOrder("temp_throwaway.json")
os.remove("temp_throwaway.json")

