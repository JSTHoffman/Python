# Python Exam 1 - Pt. 1
# Jaime Hoffman
#______________________

# import arcpy site-package
import arcpy

# set workspace
arcpy.env.workspace = r"Z:\2016S\Python\Exam1\Exam_1.gdb"

# create list of feature classes that are polygon and start with "CA"
fcList = arcpy.ListFeatureClasses("CA*", "POLYGON")

# get name for text file from user
fileName = raw_input("Please enter a name for the file: ")

# create the full file path
filePath = r"Z:\2016S\Python\Exam1\{0}.txt".format(fileName)

# create a new text file
aFile = open(filePath, "w")

for aFC in fcList:

	# get the number of features in the featureclass
	numFeatures = arcpy.GetCount_management(aFC)

	# write the name of the feature class and the number of
	# features it has to the file
	aFile.write("{0} has {1} feature(s).\n".format(aFC, numFeatures))

#close and save the file
aFile.close()

print "The script has finished."