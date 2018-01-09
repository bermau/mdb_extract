#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#
# AccessDump.py
# A simple script to dump the contents of a Microsoft Access Database.
# It depends upon the mdbtools suite:
#   http://sourceforge.net/projects/mdbtools/*
# code trouvé sur : http://mazamascience.com/WorkingWithData/?p=168

import sys, subprocess # the subprocess module is new in python v 2.4
from subprocess import PIPE
INPUT = 'data/'
OUTPUT = "data_export/"

try : 
    DATABASE = sys.argv[1]
except:
    DATABASE =  INPUT+"base_de_bioch.accdb" # pour les tests

debug = True

# Get the list of table names with "mdb-tables"
# ligne suivante adaptée grâce à
# https://stackoverflow.com/questions/27722720/
# how-to-fix-an-encoding-migrating-python-subprocess-to-unicode-literals/

table_names = subprocess.Popen(["mdb-tables", "-1", DATABASE], 
                               stdout=PIPE, stdin=PIPE,
                               stderr=PIPE, universal_newlines=True).communicate()[0]
# ci dessus, la gestion de tous les std et de univeral_newline est modifiée.
if debug: print("tables" , table_names)

tables = table_names.split('\n')

if debug:  print("Les tables sont : \n");
print(tables)


# Dump each table as a CSV file using "mdb-export",
# converting " " in table names to "_" for the CSV filenames.
for table in tables:
    if debug: print("Je traite la table : ", table)
    if table != '':
        filename = table.replace(" ","_") + ".csv"
        file = open(filename, 'w')
        if debug:print("Dumping " + table)
        contents = subprocess.Popen(["mdb-export", DATABASE, table],
                                    stdout=PIPE, stdin=PIPE,
                                    stderr=PIPE, universal_newlines=True                               
                                    ).communicate()[0]
        file.write(contents)
        file.close()
