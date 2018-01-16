"""Configuration file"""
import os.path

from os.path import expanduser
HOME = expanduser("~")


DATA = 'important/themes/B_0127_base_pour_chimie_cher/a_001_base_bioch/'


DATA_REP = os.path.join(HOME, DATA)

INPUT = os.path.join(DATA_REP, 'data')
OUTPUT = os.path.join(DATA_REP, "data_export")
