# Jaime Hoffman
# Python Assignment 7
# Script 1: Select by Attributes
#_______________________________

import arcpy

# set environment properties
aws = r"C:\Users\Jaime\Documents\School\Python\Assignment_07\LandParcels.gdb"
arcpy.env.workspace = aws
arcpy.env.overwriteoutput = True

try:
	# QUESTION #1
	# set feature class
	featureClass = "LandParcels"

	# make feature layer for selections
	outLayer = "lpLayer"
	selectionLayer = arcpy.management.MakeFeatureLayer(featureClass, outLayer)

	# make list for SQL expressions for each question
	sqlList = [
				'',
				'YearBuilt IS NULL',
				'YearBuilt > 1955 AND YearBuilt < 1982',
				''
			]

	# open a text file to write answers 
	aFile = open(r"C:\Users\Jaime\Documents\School\Python\Assignment_07"
													"\Assignment_07.txt", "w")

	# start with question A
	qNum = 1
	qLetter = 'A'

	for anExp in sqlList:

		# set selection type
		selType = "NEW_SELECTION"

		# for question 1
		if qNum == 1:
			# get the number of features in LandParcels FC
			answer = arcpy.management.GetCount("LandParcels")

		elif qNum in [2, 3]:
			# apply the selecton and count the number of features
			arcpy.management.SelectLayerByAttribute(selectionLayer,
																selType, anExp)
			answer = arcpy.management.GetCount(selectionLayer)

		elif qNum == 4:
			# use select by location
			# set parameters and count features
			overlapType = "WITHIN_A_DISTANCE"
			selFeatures = "Towers"
			searchDist = "1 Mile"
			arcpy.management.SelectLayerByLocation(selectionLayer,
								overlapType, selFeatures, searchDist, selType)
			answer = arcpy.management.GetCount(selectionLayer) 

		# write the answer to the file
		aFile.write("Q1 {0}) {1} land parcels.\n\n".format(qLetter, answer))

		# update question number and letter
		qNum += 1
		qLetter = chr(ord(qLetter) + 1)

	# save and close the file
	aFile.close()


	# QUESTION #2
	#____________

	# create update cursor
	aCursor  = arcpy.da.UpdateCursor(featureClass, ["UseCode", "Land"])

	# loop through cursor
	for aRow in aCursor:

		# reclassify based on UseCode
		if aRow[0] == "A":
			aRow[1] = "Single-Family Residential"

		elif aRow[0] == "B":
			aRow[1] = "Multi-Family Residential"

		elif aRow[0] in ["GOV", "CITY", "CITYV", "CITYW"]:
			aRow[1] = "Government"

		elif aRow[0] == "F1":
			aRow[1] = "Commercial"

		elif aRow[0] == "F2":
			aRow[1] = "Industrial"

		elif aRow[0] in ["POS", "PRK", "PROW"]:
			aRow[1] = "Park"

		elif aRow[0] == "SCH":
			aRow[1] = "Schools"

		elif aRow[0] == "UTIL":
			aRow[1] = "Utilities"

		elif aRow[0] == "VAC":
			aRow[1] = "Vacant"

		# apply update
		aCursor.updateRow(aRow)

	# delete row and cursor
	del aRow
	del aCursor

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