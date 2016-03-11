# Jaime Hoffman
# Week 5 Challenge 1
# Description: Python Error Handling and Messages
# _______________________________________________


# import arcpy site-package and os module
import arcpy, os

# Set geoprocessing environment: a) set  the workspace environment 
arcpy.env.workspace = r"C:\Users\Jaime\Desktop\Assignment4\Practice_Data\Geodatabase\Test_Data.gdb"

# Set geoprocessing environment: b) the overwriteOutput parameter controls whether tools will automatically overwrite any existing output 
arcpy.env.overwriteOutput = False

try:
    # create buffer around stations dissolved
    arcpy.analysis.Buffer("Points", "Buffer_175", "175", "", "", "ALL")

    print "Buffer has been created."

    # clip land use using buffer
    arcpy.analysis.Clip("LandParcels", "Buffer_175", "LandParcels_Clip")

    print "Land Use has been clipped using Buffer."

    # summarize area based on parcel type
    arcpy.analysis.Statistics("LandParcels_Clip", "Challenge1", [["Shape_Area", "SUM"]], "CATEGORY")

    print "Area of each land use has been calculated."

    # get results table
    # tableList = arcpy.ListTables("Challenge1")

    # aField1 = "CATEGORY"
    # aField2 = "SUM_Shape_Area"
    # aCursor = arcpy.SearchCursor("Challenge1")
    # aRow = aCursor.next()
    
    # # print results
    # while aRow:
    # 	print aRow.getValue("CATEGORY") + " land use covers an area of " + str(aRow.getValue("SUM_Shape_Area")) + " square meters."

except:
    # Code to run when an error occured
    print "An ERROR Occured!"
    print "\n" + arcpy.GetMessages()

else:
    # Message when there was no error
    print "\nNo Error occurred"
    
# Script end message
print "\nEnd of the script!"    