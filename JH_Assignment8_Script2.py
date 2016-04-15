# Jaime Hoffman
# Python Assignment 8
# Script 2: Cursors 2
#_______________________________

import arcpy, numpy

# set environment properties
aws = r"Z:\2016S\Python\Assignment8\California.gdb"
arcpy.env.workspace = aws
arcpy.env.overwriteOutput = True

try:
	# QUESTION #2
	# summarize health care facilites
	featureClass = "CA_HealthFacs"
	outName = "Health_Stats"
	stats = [["LIC_BEDS", "SUM"]]
	case = "CATEGORY"
	arcpy.analysis.Statistics(featureClass, outName, stats, case)

	# create file to write answers to
	aFile = open(r"Z:\2016S\Python\Assignment8\Assignment_08.txt", "a")

	# get number of categories from stats table
	answer1 = arcpy.management.GetCount(outName)
	aFile.write("There are {0} different types of health care facilities.\n\n"
															.format(answer1))

	# create search cursor
	aCursor = arcpy.da.SearchCursor(outName, ["CATEGORY", "SUM_LIC_BEDS"])

	# print the category and number of beds
	for aRow in aCursor:
		aFile.write("{0} facilites have {1} licenced beds.\n\n"
													.format(aRow[0], aRow[1]))

	# delete row and cursor variables
	del aRow, aCursor

	# close and save the file
	aFile.close()

except:
	# when an error occurs
	print "An ERROR occurred:\n"

	# get arcpy error messages
	errorMsg = arcpy.GetMessages(2)

	# if there was no arcpy error, tell the user
	# otherwise print the error message
	if errorMsg == "":
		print "This was not an arcpy error."
	else:
		print errorMsg

else:
	# no errors occurred and the script is finished, get arcpy warnings
	print "No errors occurred.\n\nThe script has finished.\n"
	print arcpy.GetMessages(1)