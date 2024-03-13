# Load file
## import StationInfo from LoadData.py
from LoadData import StationInfo

# Collect user from_station and to_station
from_station = input("Where is your current station? (Example input: AldgateEast or aldgateeast): \n" )
to_station = input("Where you want to go? (Example input: AldgateEast or aldgateeast): \n")

# Use StationInfo to get the station information
from_station_id = StationInfo.GetIDFromName(from_station)
to_station_id = StationInfo.GetIDFromName(to_station)
from_station_nei = StationInfo.GetNeighboursFromID(from_station)

# Import StationFinder to find the path
## Take the from_station_id as root node to create a tree using StationTree and StationNode
