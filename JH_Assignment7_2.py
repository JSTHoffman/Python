# Jaime Hoffman
# Python Assignment 7
# Script 1: Select by Attributes
#_______________________________

import arcpy

# set environment properties
aws = r"Z:\2016S\Python\Assignment7\LandParcels.gdb"
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
	aFile = open(r"Z:\2016S\Python\Assignment7\Assignment_07.txt", "w")

	# start with question A
	qNum = 1
	qLetter = 'A'

	for anExp in sqlList:

		# set selection type
		selType = "NEW_SELECTION"

		# for question 1
		if qNum == 1:
			# get the number of features in LandParcels FC
			answer = arcpy.management.GetCount(featureClass)

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

	# create list of SQL expressions for search cursor
	expList = [
				'UseCode = \'A\'',
				'UseCode = \'B\'',
				'UseCode IN(\'GOV\', \'CITY\', \'CITYV\', \'CITYW\')',
				'UseCode = \'F1\'',
				'UseCode = \'F2\'',
				'UseCode IN( \'POS\', \'PRK\', \'PROW\')',
				'UseCode = \'SCH\'',
				'UseCode = \'UTIL\'',
				'UseCode = \'VAC\''
			]
	# create list of new values
	newValues = [
					"Single-Family Residential",
					"Multi-Family Residential",
					"Government",
					"Commercial",
					"Industrial",
					"Park",
					"Schools",
					"Utilities",
					"Vacant"
				]

	# set fields for cursor and set counter variable
	fields = ["UseCode", "Land"]
	counter = 0

	# loop through expression list
	for anExp in expList:

		print counter

		# create a cursor with the expression
		with arcpy.da.UpdateCursor(featureClass, fields, anExp) as aCursor:

			# loop through cursor and update "Land" field
			for aRow in aCursor:
				aRow[1] = newValues[counter]

				# apply update
				aCursor.updateRow(aRow)

			# delete row and cursor
			del aRow
			del aCursor

			# update counter
			counter += 1

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
