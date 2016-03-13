# Jaime Hoffman
# In Class Assignment 1
# Created by: 
# Description: 

'''
This is additional description area
'''

# import arcpy site-package and os module
import arcpy, os

# Set geoprocessing environment: a) set  the workspace environment
aWS1 = r"C:\Users\Jaime\Documents\School\Python\InClass_01\Orange_County.gdb"
arcpy.env.workspace = aWS1

# Set geoprocessing environment: b) the overwriteOutput parameter controls whether tools will automatically overwrite any existing output 
arcpy.env.overwriteOutput = False

try:
    # Main Python code here    
    # store GDB path
    gdbPath = r"C:\Users\Jaime\Documents\School\Python\InClass_01"

    # create new GDB
    arcpy.management.CreateFileGDB(r"C:\Users\Jaime\Documents\School\Python\InClass_01", "OC_Projected")

    # store the alternate workspace
    aWS2 = r"C:\Users\Jaime\Documents\School\Python\InClass_01\OC_Projected.gdb"
    
    # create list of feature classes and datasets
    fcList = arcpy.ListFeatureClasses()
    dsList = arcpy.ListDatasets()

    # create a new .txt file
    aFile = open(r"C:\Users\Jaime\Documents\School\Python\InClass_01\InClass_01_Output.txt", "w")

    # list to store unprojected FCs
    unProjectedFC = []

    # list to store unprojected DSs
    unProjectedDS = []

    # loop through all feature classes
    for aFC in fcList:

    	# create a describe object and get properties
    	desc = arcpy.Describe(aFC)
    	projType = desc.spatialReference.type
    	numFeatures = arcpy.management.GetCount(aFC)

    	#check for projection and write to file accordingly
    	if projType == "Projected":
    		arcpy.management.Copy(aFC, "{0}\{1}".format(aWS2, aFC))
    		aFile.write("{0} is projected using the {1} coordinate system. It has {2} feature(s).\n\n".format(aFC, desc.spatialReference.PCSName, numFeatures))
    	else:
    		# project
    		arcpy.management.Project(aFC, "{0}\{1}_Proj".format(aWS2, aFC), arcpy.SpatialReference(26946))
    		aFile.write("{0} is not projected and uses the {1} coordinate system. It has {2} feature(s).\n\n".format(aFC, desc.spatialReference.GCSName, numFeatures))

    # loop through all datasets
    for aDS in dsList:

    	# create a describe object and get properties
    	desc = arcpy.Describe(aDS)
    	projType = desc.spatialReference.type

    	# check for projection and write to file accordingly
    	if projType == "Projected":
    		arcpy.management.Copy(aDS, "{0}\{1}".format(aWS2, aDS))
    		aFile.write("{0} is projected using the {1} coordinate system.\n\n".format(aDS, desc.spatialReference.PCSName))
    	else:
    		# project
    		arcpy.management.ProjectRaster(aDS, "{0}\{1}_Proj".format(aWS2, aDS), arcpy.SpatialReference(26946))
    		aFile.write("{0} is not projected and uses the {1} coordinate system.\n\n".format(aDS, desc.spatialReference.GCSName))

    # close and save the file
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
