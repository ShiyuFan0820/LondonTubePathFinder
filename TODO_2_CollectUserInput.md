# Code
```py
from LoadData import StationInfo
while True:
    # Collect user from_station and to_station
    from_station = input("Where is your start station? (Example input: AldgateEast): \n" )
    to_station = input("Where you want to go? (Example input: AldgateEast): \n")

    # Check if the input is in the StationInfo
    if from_station in StationInfo.m_name_to_id_dict and to_station in StationInfo.m_name_to_id_dict:
        from_station_id = StationInfo.GetIDFromName(from_station)
        to_station_id = StationInfo.GetIDFromName(to_station)
    else:
        print(f"Your station input is not correct, try to input again.")
        continue
```

# Issues
1. What if the user input `AldgateEast` as `Aldgate East` or `aldgate east` or the user just typo a letter, the code doesn't handle these situations, how can we verify the validity of input?
