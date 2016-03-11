# Assignment 3: Introduction to ArcPy

# Jaime Hoffman
# California State University, Northridge
#________________________________________

# import the ArcPy module
import arcpy

# set the current workspace
arcpy.env.workspace = r"Z:\2016S\Python\Assignment3"

# list of buffer distances
distanceList = ["150", "250", "500"]

# set buffer input outside loop since it doesn't change
buffInput = "stations.shp"

for i in distanceList:

	# set other buffer tool parameters
	linearUnit = "{0} Meters".format(i)
	buffOutput = "Buffer_{0}".format(i)

	# create buffer
	arcpy.analysis.Buffer(buffInput, buffOutput, linearUnit)

# end of script
print "The script has finished."