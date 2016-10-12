import csv
import os, sys


#Creates list of all files in path 

path = "C:\Dev\Workspace\HTR"
dirs = os.listdir( path )

find = "F1"
replace = "F2"

for files in dirs:
	os.chdir("C:\Dev\Workspace\HTR")
	ifile = open(files, 'r')
	reader = csv.reader(ifile)
	os.chdir("C:\copyt")
	ofile = open(files, 'w')
	writer = csv.writer(ofile)

	s = ifile.read()
	s = s.replace(find, replace)
	ofile.write(s)
	ifile.close()
	ofile.close()
