import sys
import csv


newCSV = open('test.csv', "wb")
writer = csv.writer(newCSV, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow([","] * 5 + ['beans'])
newCSV.close()
