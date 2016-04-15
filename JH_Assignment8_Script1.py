# Jaime Hoffman
# Python Assignment 8
# Script 1: Cursors
#_______________________________

import arcpy, numpy

# set environment properties
aws = r"Z:\2016S\Python\Assignment8\California.gdb"
arcpy.env.workspace = aws
arcpy.env.overwriteOutput = True

try:
	# QUESTION #1
	# add field and calculate arae in square feet
	featureClass = "CA_Zipcodes"
	arcpy.management.AddField(featureClass, "Area_SQFT", "DOUBLE")
	arcpy.management.CalculateField(featureClass, "Area_SQFT",
										"!SHAPE.AREA@SQUAREFEET!", "PYTHON")
	# update cursor parameters
	fields = ["PO_NAME", "POP2001", "Area_SQFT"]
	whereClauses = ['PO_NAME LIKE \'Y%\'', 'POP2001 > 5000']

	# create lists for mean calculations
	popList = []
	areaList = []

	# create file to write answers to
	aFile = open(r"Z:\2016S\Python\Assignment8\Assignment_08.txt", "w")

	# create search cursors
	aCursor1 = arcpy.da.SearchCursor(featureClass, fields, whereClauses[0])
	aCursor2 = arcpy.da.SearchCursor(featureClass, fields, whereClauses[1])

	# add each value in cursor 1 to list
	for aRow in aCursor1:
		popList.append(aRow[1])

	# add each value in cursor 2 to list
	for aRow in aCursor2:
		areaList.append(aRow[2])

	# delete row and cursor variables
	del aRow, aCursor1, aCursor2

	# calculate mean population
	answer1 = numpy.mean(popList)
	aFile.write("Q1 A) {0}\n\n".format(answer1))

	# calculate standard deviation of area
	answer2 = numpy.std(areaList)
	aFile.write("Q1 B) {0}\n\n".format(answer2))

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