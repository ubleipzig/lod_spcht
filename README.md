# Solr to Triplestore Bridge

This project started out under a vastly different name. In its first life it was a very tightly build small tool aiming to provide a singular job. That objective remained mostly the same but the scope grew a bit larger and so a decision was made: a tool evolved from the first one takes the place and provides the ability to do more than a simple tool.

![Simple diagram explaining the workflow](./README/simplediagram1.png)

The project had already processed data from various sources in a search-able database, in this case an apache solr. On of the export formats of the solr is in json-format. Here we find some header informations and a list of key-value statements describing various attributes of media. These data should be transfered in a [triplestore](https://en.wikipedia.org/wiki/Triplestore), originally [OpenLink Virtuoso](https://virtuoso.openlinksw.com/) stored as rdf-triple. For those triples another step has to be taken, each data-pair needs to be matched into the right kind of object. The first instance of this work was hard coded and found the mapping directly in the code. To preserve the ability to change things at a later point of time a new format was found: the **spcht descriptor format**.

While other frameworks like [MetaFacture](https://github.com/metafacture) exists, these proved to unwieldy. The format of the *sdf* is written in json and structured more simply. It cannot provide the same feature richness MetaFacture offers but runs easier. There is also a [GUI Tool](https://github.com/jpkanter/spcht_checker_gui) to provide guidance for the format itself.

## Content

The Codebase is strictly divided in the actual framework for spcht and an implementation for this specific project. 

## main.py

The main part of the logic. It offers a handful of functions usable via a command line interface. Most settings that can be specified via a direct resource can also referenced in a configuration json file with the key `para`.

### local_tools.py

To cleanup the main functions a bit some auxiliary functions where placed here to keep the code more readable.

## SpchtDiscriptorFormat.py

Main class file for the spcht descriptor format. Further instructions and how to use it are in the [SPCHT.md](SPCHT.md) file

## Requirements

* python3-rdflib 
* python3-elasticsearch
* python3-dev
* unixodbc-dev

## Development Notes

Apart from very German capitalization of random words i would also like to lose a word about the program and plug-ins i used for this, while the master can work with everything i would not consider myself as such.

I used [Intellij Pycharm](https://www.jetbrains.com/pycharm/)  with the following plug-ins:

* Rainbow Brackets - makes it easier to find the right entry point
* GitToolBox - for people that just forget most of the functionality git offers
* Comments Highlighter - Port of the Vs Code Plug-in _Better Comments_, makes comments a bit more colorful
* CodeGlance - provides a neat minimap to the code
* a bunch of standard plug-ins that come with Pycharm when you just install it

for writing markdown files i used [Typora](https://typora.io/).

## Funding

Funded by European Regional Development Fund (EFRE)![EFRE_EU_quer_2015_cmyk_engl](./README/EFRE_EU_quer_2015_cmyk_engl.jpg)