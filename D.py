import arcpy
 #set upp the variable and set to true
target_City = "Federal Way"     
arcpy.env.workspace = "C:\\Users\\TQuar\\Desktop\\Codeschool\\week 8\\Exercise7\\Exercise7_D\\Washington.gdb"
arcpy.env.overwriteOutput = True
parkAndRide = "ParkAndRide"    
cities = "CityBoundaries"      
  
#query for the target city
cityQuery = "NAME = '" + target_City + "'"
 
# New Selection for target city
cityLayer = arcpy.SelectLayerByAttribute_management(cities, "NEW_SELECTION", cityQuery)
  
# Select all park and rides in the target city
parkAndRideLayer = arcpy.SelectLayerByLocation_management(parkAndRide, "CONTAINED_BY", cityLayer)
  
# a new feature class and delete the unnecessary up
arcpy.CopyFeatures_management(parkAndRideLayer, "TargetParkAndRideFacilities")
  
arcpy.Delete_management(parkAndRideLayer)
arcpy.Delete_management(cityLayer)
# 8 are selected
