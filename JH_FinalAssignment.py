# Python Final Assignment
# Created by: Jaime Hoffman
# Description: Last assignment of ever

'''
This is additional description area
'''

# import arcpy site-package and os module
import arcpy, numpy, os

# Set geoprocessing environment: a) set  the workspace environment
aWS = r"C:\_StudentData\JHoffman\Final_Assignment\Final_Assignment.gdb"
arcpy.env.workspace = aWS

# Set geoprocessing environment: b) the overwriteOutput parameter controls whether tools will automatically overwrite any existing output 
arcpy.env.overwriteOutput = False

try:
    # Main Python code here    
	# create new file GDB
	GDBpath = r"C:\_StudentData\JHoffman\Final_Assignment"
	arcpy.management.CreateFileGDB(GDBpath, "Projected")

	# store new geodatabase as second workspace
	aWS2 = r"C:\_StudentData\JHoffman\Final_Assignment\Projected.gdb"

	aFilePath = r"C:\_StudentData\JHoffman\Final_Assignment\FinalAssignment.txt"
	aFile = open(aFilePath, "w")

	# -------------
	# QUESTIONS 1-5
	# -------------

	# list all rasters and FCs in the workspace
	fcList = arcpy.ListFeatureClasses()
	rList = arcpy.ListRasters()

	# loop through raster list
	for aRaster in rList:
		# create a describe object
		aDesc = arcpy.Describe(aRaster)

		# check for type of projection
		if aDesc.SpatialReference.type == "Geographic":

			# project the raster
			print "{0} must be projected".format(aRaster)
			arcpy.management.ProjectRaster(aRaster,
							"{0}\{1}_Proj".format(aWS2, aRaster), "26945")

		elif aDesc.SpatialReference.type == "Projected":

			# copy the raster
			print "{0} must be copied.".format(aRaster)
			arcpy.management.Copy(aRaster, "{0}\{1}".format(aWS2, aRaster))

		else:
			# write name of dataset to text file
			print "{0} has no spatial reference.".format(aRaster)
			aFile.write("{0} has no spatial reference.\n\n".format(aRaster))

	# loop through feature class list
	for aFC in fcList:
		# create a describe object
		aDesc = arcpy.Describe(aFC)

		# write the name of the feature class and its type to the text file
		aFile.write("{0} is a {1} feature class.\n\n".format(aFC, aDesc.shapeType))

		# check for type of projection
		if aDesc.SpatialReference.type == "Geographic":
			# project the feature class
			print "{0} must be projected".format(aFC)
			arcpy.management.Project(aFC,
							"{0}\{1}_Proj".format(aWS2, aFC), "26945")

		elif aDesc.SpatialReference.type == "Projected":
			# copy the feature class
			print "{0} must be copied.".format(aFC)
			arcpy.management.Copy(aFC, "{0}\{1}".format(aWS2, aFC))

		else:
			# write name of dataset to text file
			print "{0} has no spatial reference.".format(aFC)
			aFile.write("{0} has no spatial reference.\n\n".format(aFC))

	# ----------
	# QUESTION 6
	# ----------

	# create a list for pop calculation
	popList = []

	# create a cursor
	aCursor = arcpy.da.SearchCursor("ZipCodes", "POP2001", "PO_NAME LIKE 'R%'")

	# loop through cursor and add values to list
	for aRow in aCursor:
		popList.append(aRow[0])

	# delete row and cursor objects
	del aRow, aCursor

	# calculate average population
	avgPop = numpy.mean(popList)

	# write answer to text file
	aFile.write("The average population in zip codes with names starting with 'R' is {0}.".format(avgPop))

	# save and close the text file
	aFile.close()

except:
    # Code to run when an error occured
    print "An ERROR Occured!"
    print "\n" + arcpy.GetMessages(2)

else:
    # Message when there was no error
    print "\nNo Error occurred"
    
# Script end message
print "\nEnd of the script!"




