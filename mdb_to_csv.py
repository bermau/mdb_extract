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
import sys, os, subprocess
from subprocess import PIPE
import config_file as Cf


debug = True

class Translator_mdb2():
    """Tools to translate form mdb to sqlite"""
    
    def __init__(self, DATABASE):
        self.DB_name = DATABASE
        
    def extract_table_names(self):
        # Get the list of table names with "mdb-tables"
        print("DB name :",self.DB_name)
        table_names = subprocess.Popen(["mdb-tables", "-1", self.DB_name], 
                                       stdout=PIPE, stdin=PIPE, stderr=PIPE,
                                       universal_newlines=True).communicate()[0]
        print(table_names)
        if debug: print("tables" , table_names)
        #  tables = table_names.split('\n')
        self.tables = table_names.splitlines()
        if debug:
            print("Table names :");
            print(self.tables)
    def extract_structure(self):
        pass
    def extract_data_as_csv(self): 
        # Dump each table as a CSV file using "mdb-export",
        # converting " " in table names to "_" for the CSV filenames.
        for table in self.tables:
            if table != '':
                if debug:print("Extracting table : " + table)
                filename = os.path.join(Cf.OUTPUT, table.replace(" ","_") + ".csv")
                with open(filename, 'w') as file:                    
                    contents = subprocess.Popen(["mdb-export", self.DB_name, table],
                                                stdout=PIPE, stdin=PIPE,
                                                stderr=PIPE, universal_newlines=True                               
                                                ).communicate()[0]
                    # Autres options : 
                    #
                    if debug> 1:
                        print(contents)
                    else:
                        file.write(contents)
                        print("Data written in ", filename)

    
if __name__ == '__main__':
    try : 
        DATABASE = sys.argv[1]
    except:
        DATABASE =  os.path.join(Cf.INPUT, "base_de_bioch.accdb") # pour les tests

    if not os.path.isfile(DATABASE):
        print("Fichier inexistant")
        
    T = Translator_mdb2(DATABASE)
    T.extract_table_names()
    T.extract_data_as_csv()
