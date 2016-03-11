# Jaime Hoffman
# Week 5 Challenge 2
# Description: Python Error Handling and Messages
# _______________________________________________


# import arcpy site-package and os module
import arcpy, os

# Set geoprocessing environment: a) set  the workspace environment 
arcpy.env.workspace = r"C:\Users\Jaime\Desktop\Assignment4\Practice_Data\Geodatabase\Test_Data.gdb"

# Set geoprocessing environment: b) the overwriteOutput parameter controls whether tools will automatically overwrite any existing output 
arcpy.env.overwriteOutput = False

try:
    # create buffer around stations without dissolve
    arcpy.analysis.Buffer("Points", "Buffer_175_noDiss", "175")

    print "Buffer has been created."

    # intersect buffer and land use
    arcpy.analysis.Intersect(["LandParcels", "Buffer_175_noDiss"], "Intersect", "ALL")

    print "Buffer and Land Use have been intersected."

    # dissolve intersect based on land use and buffer ID
    arcpy.management.Dissolve("Intersect", "Challenge2", ["CATEGORY", "Number_ID"])

    print "Intersect layer has been dissolved."

except:
    # Code to run when an error occured
    print "An ERROR Occured!"
    print "\n" + arcpy.GetMessages()

else:
    # Message when there was no error
    print "\nNo Error occurred"
    
# Script end message
print "\nEnd of the script!"    