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
arguments = {
        "CreateOrder":
            {
                "type": "str",
                "help": "Creates a blank order without executing it",
                "metavar": ["order_name", "fetch_method", "processing_type", "insert_method"],
                "nargs": 4
            },
        "CreateOrderPara":
            {
                "action": "store_true",
                "help": "Creates a blank order with executing it with provided variables: --order_name, --fetch, --process and --insert"
            },
        "order_name":
            {
                "type": "str",
                "help": "name for a new order"
            },
        "fetch":
            {
                "type": "str",
                "help": "Type of fetch mechanismn for data: 'solr' or 'file'"
            },
        "process":
            {
                "type": "str",
                "help": "Processing type, either 'insert' or 'update'"
            },
        "insert":
            {
                "type": "str",
                "help": "method of inserting into triplestore: 'isql', 'obdc' or 'sparql'"
            },
        "FetchSolrOrder":
            {
                "type": "str",
                "help": "Executes a fetch order provided, if the work order file has that current status",
                "metavar": ["work_file", "solr_url", "query", "total_rows", "chunk_size", "spcht_descriptor", "save_folder"],
                "nargs": 7
            },
        "FetchSolrOrderPara":
            {
                "action": "store_true",
                "help": "Executes a solr fetch work order, needs parameters --work_order_file, --solr_url, --query, --total_rows, --chunk_size, --spcht_descriptor, --save_folder"
            },
        "work_order_file":
            {
                "type": "str",
                "help": "Path to work order file"
            },
        "solr_url":
            {
                "type": "str",
                "help": "Url to a solr query endpoint"
            },
        "query":
            {
                "type": "str",
                "help": "Query for solr ['*' fetches everything]",
                "default": "*"
            },
        "total_rows":
            {
                "type": "int",
                "help": "Number of rows that are fetched in total from an external datasource",
                "default": 25000
            },
        "chunk_size":
            {
                "type": "int",
                "help": "Size of a single chunk, determines the number of queries",
                "default": 5000
            },
        "max_age":
            {
                "type": "int",
                "help": "Maximum age of a given entry in the source database, used for update operations as filter"
            },
        "spcht_descriptor":
            {
                "type": "str",
                "help": "Path to a spcht descriptor file, usually ends with '.spcht.json'"
            },
        "save_folder":
            {
                "type": "str",
                "help": "The folder were downloaded data is to be saved, will be referenced in work order",
                "default": "./"
            },
        "SpchtProcessing":
            {
                "type": "str",
                "help": "Processes the provided work order file",
                "metavar": ["work_file", "graph/subject", "spcht_descriptor"],
                "nargs": 3
            },
        "SpchtProcessingMulti":
            {
                "type": "str",
                "help": "Processes the provided work order file in multiple threads",
                "metavar": ["work_file", "graph/subject", "spcht_descriptor", "processes"],
                "nargs": 4
            },
        "SpchtProcessingPara":
            {
                "action": "store_true",
                "help": "Processes the given work_order file with parameters, needs: --work_order_file, --graph, --spcht_descriptor"
            },
        "SpchtProcessingMultiPara":
            {
                "action": "store_true",
                "help": "Procesesses the given order with multiple processes, needs: --work_order_file, --graph, --spcht_descriptor, --processes"
            },
        "subject":
            {
                "type": "str",
                "help": "URI of the subject part the graph gets mapped to in the <subject> <predicate> <object> triple"
            },
        "processes":
            {
                "type": "int",
                "help": "Number of parallel processes used, should be <= cpu_count",
                "default": 1
            },
        "InsertISQLOrder":
            {
                "type": "str",
                "help": "Inserts the given work order via the isql interface of virtuoso, copies files in a temporary folder where virtuoso has access, needs credentials",
                "metavar": ["work_file", "named_graph", "isql_path", "user", "password", "virt_folder"],
                "nargs": 6
            },
        "InsertISQLOrderPara":
            {
                "action": "store_true",
                "help": "Inserts the given order via the isql interace of virtuoso, copies files in a temporary folder, needs paramters: --isql_path, --user, --password, --named_graph, --virt_folder"
            },
        "named_graph":
            {
                "type": "str",
                "help": "In a quadstore this is the graph the processed triples are saved upon, might be different from the triple subject"
            },
        "isql_path":
            {
                "type": "str",
                "help": "File path to the OpenLink Virtuoso isql executable, usually 'isql-v' or 'isql-v.exe"
            },
        "virt_folder":
            {
                "type": "str",
                "help": "When inserting data via iSQL the ingested files must lay in a directory whitelisted by Virtuoso, usually this is /tmp/ in Linux systems, but can be anywhere if configured so. Script must have write access there."
            },
        "user":
            {
                "type": "str",
                "help": "Name of an authorized user for the desired operation"
            },
        "password":
            {
                "type": "str",
                "help": "Plaintext password for the defined --user, caution advised when saving cleartext passwords in config files or bash history"
            },
        "isql_port":
            {
                "type": "int",
                "help": "When using iSQL the corresponding database usually resides on port 1111, this parameter allows to adjust for changes in that regard",
                "default": 1111
            },
        "HandleWorkOrder":
            {
                "type": "str",
                "help": "Takes any one work order and processes it to the next step, needs all parameters the corresponding steps requires",
                "metavar": ["work_order_file"],
                "nargs": 1
            },
        "FullOrder":
            {
                "type": "str",
                "help": "Creates a new order with assigned methods, immediatly starts with --Parameters [or --config] to fullfill the created order",
                "metavar": ["work_order_name", "fetch", "type", "method"],
                "nargs": 4
            },
        "sparql_endpoint":
            {
                "type": "str",
                "help": "URL to a sparql endpoint of any one triplestore, usually ends with /sparql or /sparql-auth for authenticated user"
            },
        "CheckWorkOrder":
            {
                "type": "str",
                "help": "Checks the status of any given work order and displays it in the console",
                "metavar": ["work_order_file"],
                "nargs": 1
            },
        "config":
            {
                "type": "str",
                "help": "loads the defined config file, must be a json file containing a flat dictionary",
                "metavar": ["path/to/config.json"],
                "short": "-c"
            },
        "UpdateData":
            {
                "help": "Special form of full process, fetches data with a filter, deletes old data and inserts new ones",
                "action": "store_true"
            },
        "environment":
            {
                "action": "store_true",
                "help": "Prints all variables"
            },
        "force":
            {
                "action": "store_true",
                "help": "Ignores security checks in work order execution like only proceeding when the right meta status is present"
            },
        "CleanUp":
            {
                "type": "str",
                "help": "Deletes all temporary files of a given work order.",
                "metavar": ["work_order_file"]
            },
        "CompileSpcht":
            {
                "type": "str",
                "help": "Inserts all includes of a spcht descriptor in one file, resolving all include relations",
                "metavar": ["SPCHT_FILE", "FILEPATH"],
                "nargs": 2
            },
        "CheckFields":
            {
                "type": "str",
                "help": "Loads a spcht file and displays all dictionary keys used in that descriptor",
                "metavar": ["SPCHT_FILE"]
            },
        "debug":
            {
                "action": "store_true",
                "help": "Sets the debug flag for CheckFields, CheckSpcht, CompileSpcht"
            },
        "CheckSpcht":
            {
                "help": "Tries to load and validate the specified Spcht JSON File",
                "type": "str",
                "metavar": ["SPCHT FILE"]
            },
        "ContinueWorkOrder":
            {
                "help":  "Continues a previously paused or interrupted work order, needs parameters",
                "type": "str",
                "metavar": ["WORK ORDER FILE"]
            }
    }
