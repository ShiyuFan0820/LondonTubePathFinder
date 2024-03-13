# Load file
## import StationInfo from LoadData.py
from LoadData import StationInfo
while True:
    # Collect user from_station and to_station
    from_station = input("Where is your start station? (Example input: AldgateEast or aldgateeast): \n" )
    to_station = input("Where you want to go? (Example input: AldgateEast or aldgateeast): \n")

    # Check if the input is in the StationInfo
    if from_station in StationInfo.m_name_to_id_dict and to_station in StationInfo.m_name_to_id_dict:
        from_station_id = StationInfo.GetIDFromName(from_station)
        to_station_id = StationInfo.GetIDFromName(to_station)
    else:
        print(f"Your station input is not correct, try to input again.")
        continue
    # Use StationInfo to get the station information
    from_station_nei = StationInfo.GetNeighboursFromID(from_station)

    # Import StationFinder to find the path
    ## Take the from_station as root node to create a tree using StationTree and StationNode
