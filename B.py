import arcpy
arcpy.env.overwriteOutput = True

#setting up the variable
featureClass = "C:\\Users\\TQuar\\Desktop\\Codeschool\\week 8\\Exercise7\\Exercise7_B\\Washington.gdb"
cityBoundaries = "CityBoundaries"
parkAndRide = "ParkAndRide"
parkAndRideField = "HasParkAndRide"
citieswithPAR = 0

   # Pulling the IS column and starting with )
cityIDStringField = "CI_FIPS"             
citiesWithTwoParkAndRides = 0             
numCities = 0                             
 
# Gotta close the loop and return with an iterator of names or cities then start at 0
with arcpy.da.UpdateCursor(cityBoundaries, (cityIDStringField, parkAndRideField)) as cityRows:
    for city in cityRows:
        #  query for the current city    
        cityIDString = city[0]
        whereClause = cityIDStringField + " = '" + cityIDString + "'"
        print("Processing city " + cityIDString)
  
        # select the layer field    
        currentCityLayer = arcpy.SelectLayerByAttribute_management(cityBoundaries, "NEW_SELECTION", whereClause)
  
        try:
            # reduce the search from the current list
            selectedParkAndRideLayer = arcpy.SelectLayerByLocation_management(parkAndRide, "CONTAINED_BY", currentCityLayer)
  
            # Count the number places or parks and rides selected
            numSelectedParkAndRide = int(selectedParkAndRideLayer[2])
  
            # Set it to TRUE if there is 2 or more
            if numSelectedParkAndRide >= 2:
                city[1] = "TRUE"
  
                # Don't forget to call updateRow
                cityRows.updateRow(city)
  
                # Add 1 to your tally of cities with two park and rides                
                citiesWithTwoParkAndRides += 1
             
            numCities += 1
        except:
            print("Issue in locating ParkAndRides in " + cityIDString)
        finally:
            # delete the selection
            arcpy.Delete_management(selectedParkAndRideLayer) 
            arcpy.Delete_management(currentCityLayer)
 
del city, cityRows
  
# find the percentage of cities with two park and rides
if numCities != 0:
    percentCitiesWithParkAndRide = (citiesWithTwoParkAndRides / numCities) * 100
    print (str(round(percentCitiesWithParkAndRide,1)) + " percent of cities have two park and rides.")
else:
    print ("There is no city/cities found or wrong input.")
#38.0 percent of cities have two park and rides
