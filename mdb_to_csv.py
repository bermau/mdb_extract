#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#
# A simple python script to import data from a Microsoft Access database.
# It depends on the suite of mdbtools available on unix:
# http://sourceforge.net/projects/mdbtools/*# A simple script to dump the contents of a Microsoft Access Database.
# It depends upon the mdbtools suite:
#   http://sourceforge.net/projects/mdbtools/*
# code trouvé sur : http://mazamascience.com/WorkingWithData/?p=168

# ajout : classe 
import sys, subprocess
from subprocess import PIPE
import config_file as Cf


try : 
    DATABASE = sys.argv[1]
except:
    DATABASE =  Cf.INPUT+"base_de_bioch.accdb" # pour les tests

class Translator_mdb2():
    """Tools to translate form mdb to sqlite"""

    def init(self):
        pass   

    def extract_data(self):          
        debug = True
        # Get the list of table names with "mdb-tables"
        table_names = subprocess.Popen(["mdb-tables", "-1", DATABASE], 
                                       stdout=PIPE, stdin=PIPE, stderr=PIPE,
                                       universal_newlines=True).communicate()[0]
        if debug: print("tables" , table_names)
        #  tables = table_names.split('\n')
        tables = table_names.splitlines()
        if debug:
            print("Table names :");
            print(tables)
        # Dump each table as a CSV file using "mdb-export",
        # converting " " in table names to "_" for the CSV filenames.
        for table in tables:
            if table != '':
                if debug:print("Extracting table : " + table)
                filename = Cf.OUTPUT+table.replace(" ","_") + ".csv"
                with open(filename, 'w') as file:                    
                    contents = subprocess.Popen(["mdb-export", DATABASE, table],
                                                stdout=PIPE, stdin=PIPE,
                                                stderr=PIPE, universal_newlines=True                               
                                                ).communicate()[0]
                    file.write(contents)
                    print("Data written in ", filename)
                    
if __name__ == '__main__':
    T = Translator_mdb2()
    T.extract_data()
