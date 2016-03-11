# Python Exam 1 - Pt. 2
# Jaime Hoffman
#______________________

# import arcpy site-package
import arcpy

# set workspace
arcpy.env.workspace = r"C:\_StudentData\JHoffman\Exam_01\Exam_1.gdb"

# create list of buffer distances
distanceList = [5, 10]

# set constant buffer tool parameters
buffInput = "CA_HealthFacs"

for i in distanceList:

	# set changing buffer tool parameters
	linearUnit = "{0} Miles".format(i)
	outName = linearUnit.replace(" ", "_")
	buffOutput = "Buffer_{0}".format(outName)

	# check parameters
	print linearUnit
	print buffOutput

	# create buffer
	arcpy.analysis.Buffer(buffInput, buffOutput, linearUnit, "", "", "ALL")

print "The script has finished."

