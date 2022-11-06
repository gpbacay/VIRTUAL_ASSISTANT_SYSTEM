import csv

file = open("attendance.csv", "r")
csvr = csv.reader(file)

namelist = []
file = open("attendance.csv", "w", newline = '')
csvr = csv.writer(file)
csvr.writerows(namelist)
file.close()

#python clearcsv.py