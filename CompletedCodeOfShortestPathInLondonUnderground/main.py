# Load file
## Import StationInfo from LoadData
## Import StationFinder from PathFinder
from LoadData import StationInfo
from PathFinder import StationFinder
## Find the path of the file, here the file is stations.txt, you can change the path of your own stations file.
filename = "/Users/fanfan/Downloads/200-Learning/250-Com/Pycharm/pythonProject/LondonTube/stations.txt"
## Pass the file to StationInfo to convert the txt file to dictionary
StationInfo.LoadData(filename)


while True:
    # Collect user from_station and to_station from UI input
    from_station = input("Where is your start station? (Example input: AldgateEast): \n" )
    to_station = input("Where you want to go? (Example input: AldgateEast): \n")

    # Check if the input is in the StationInfo
    if from_station not in StationInfo.GetNameIDDict() or to_station not in StationInfo.GetNameIDDict():
        print(f"Your station input is not correct, try to input again.")
        continue
    ## Use StationFinder to find the path
    paths = StationFinder.GetPaths(from_station, to_station)
    if paths:
        StationFinder.DisplayAllPaths(paths)
        shortest_path = StationFinder.ShortestPath(paths)
        StationFinder.DisplayShortestPath(shortest_path)
    else:
        print("Sorry, no path found.")

    ## Ask if the user want to find another path
    if_continue = input("Would you like to use our service again? Yes or No:\n").lower()
    if if_continue == "no":
        break
