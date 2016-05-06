# Python Exam 4
# Created by: Jaime Hoffman
# Description: Exam 4 script

'''
This is additional description area
'''

# import arcpy site-package, os module and numpy
import arcpy, os, numpy

# Set geoprocessing environment: a) set  the workspace environment 
arcpy.env.workspace = r"C:\_StudentData\JHoffman\Exam-04\LanParcels.gdb"

# Set geoprocessing environment: b) the overwriteOutput parameter controls whether tools will automatically overwrite any existing output 
arcpy.env.overwriteOutput = False

try:
    # Main Python code here
	# create new text file for answers
	aFile = open(r"C:\_StudentData\JHoffman\Exam-04\Exam_4.txt", "w")

	# create list for percent change values
	pChange_HDMFR = []

	# create update cursor
	aCursor = aCursor = arcpy.da.UpdateCursor("LandParcels",
									["LU_ALF", "Value_06", "Value_12", "Per_Chg"])

	# loop through rows and calculate percent change
	for aRow in aCursor:
		aRow[3] = ((float(aRow[2])-aRow[1])/aRow[1])*100
		aCursor.updateRow(aRow)

		# if land use is HDMFR, add percent change value to list
		if aRow[0] == "High-Density Multiple Family Residential":
			pChange_HDMFR.append(aRow[3])

	# delete row and cursor variables
	del aRow, aCursor

	# write average percent change for HDMFR to text file (# should be -32.042534)
	aFile.write("The average percent change for High-Density"
					" Multiple Family Residential parcels is {0}."
									.format(numpy.mean(pChange_HDMFR)))

	# save and close the file
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




