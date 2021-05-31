import pandas as pd
import csv
import os

csvpath = os.path.join("cities.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)