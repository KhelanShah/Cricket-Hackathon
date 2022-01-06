# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:07:59 2021

@author: MAFIA
"""

### Imports ###
# add imports - classes and defs
from predictor import predictRuns


"""
sys.argv[1] is the input test file name given as command line arguments

"""
runs = predictRuns('input_test_data.csv')
print("Predicted Runs: ", runs)

