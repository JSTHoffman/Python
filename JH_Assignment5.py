# Jaime Hoffman
# Assignment 5
# Geoprocessing II
# Field Calculator and Select By Attributes

# import arcpy site-package
import arcpy

# set workspace and overwrite environment properties
aWS = r"C:\Users\Jaime\Documents\School\Python\Assignment_05\California.gdb"
arcpy.env.workspace = aWS
arcpy.env.overwriteOutput = False

try:
	# **QUESTION 1**

	# AddField tool parameters
	featureClass = "CA_Zipcodes"
	field = "Acreage"
	fType = "LONG"
	arcpy.management.AddField(featureClass, field, fType)

	# CalculateField tool parameters
	exp = "!SHAPE.AREA@ACRES!"
	arcpy.management.CalculateField(featureClass, field, exp, "PYTHON")


	# **FOR QUESTIONS 2-10**

	# make feature layer for selections
	# MakeFeatureLayer tool parameters
	outLayer = "zipcodeLayer"
	selectionLayer = arcpy.management.MakeFeatureLayer(featureClass,
																outLayer)
	# list of SQL expressions for each question
	sqlList = [
				'Acreage < 65000',
				'Acreage > 200000 AND Acreage < 300000',
				'ZIP LIKE \'000%\'',
				'NOT Region = \'CENTER\'',
				'Region IN(\'CENTER\', \'SOUTH\')',
				'POP2001 < 500 AND Region = \'SOUTH\'',
				'PO_NAME LIKE \'A%\'',
				'PO_NAME LIKE \'D%\'',
				''
			]

	# create new text file for answers
	aFile = open(r"C:\Users\Jaime\Documents\School\Python\Assignment_05"
												"\Assignment_5.txt", "w")

	# start with question 2
	qNum = 2

	# loop through list of sql expressions
	for anExp in sqlList:

		# set selection type to new selection
		selType = "NEW_SELECTION"

		# if question is not #10
		if qNum != 10:
			# apply the selection and count number of selected features
			arcpy.management.SelectLayerByAttribute(selectionLayer,
														selType, anExp)
			answer = arcpy.management.GetCount(selectionLayer)

		# for question #10
		else:
			# set selection type to CLEAR_SELECTION
			selType = "CLEAR_SELECTION"

			# clear the selection and count features in CA_Zipcodes
			arcpy.management.SelectLayerByAttribute(selectionLayer, selType)
			answer = arcpy.management.GetCount(selectionLayer)

		# write the answer to the file and update the qestion number
		aFile.write("Q{0} Answer: {1} zip codes.\n\n".format(qNum, answer))
		qNum += 1

	# save and close the file
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
