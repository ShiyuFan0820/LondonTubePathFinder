# LondonTubePathFinder

The goal of this project is to build a station-to-station pathfinding system for London tube.

## TODO List

### Collect Data of London Tube Before Codeing
1. Search and download the data of stations of each tube in London.
2. Read the data file. The original data in `.mat` format and the method to read the data can be found at:

- [Data in .mat format.](https://www.cs.cornell.edu/~arb/data/spatial-underground-London/)

- [How to read the .mat file in Python.](https://stackoverflow.com/questions/874461/read-mat-files-in-python)

- [Organized data in txt file.](https://github.com/mincongzhang/StationPathFinder/blob/master/LondonTube/LondonTube/stations.txt)

### Write the Code
1. **Load Data:**
   - Read the `.mat` data file, extract the content and convert in to a `.txt` file.
   - Each station could be a node, and make the adjacent station node to a list.
2. **Collect User Input:**
   - Handle user input to specify the starting station and the end station.
   - Handle the situation if the user input the wrong name of the station.
3. **Create the Path Tree:**
   - Create a tree whose root is the start station, get its adjacent station from the file.
4. **Find the Path:**
   - Use the BFS algorithm to traverse the tree from the start station to the end station.
   - During the traversal, keep track of the parent of each node to reconstruct the path later.
   - Once BFS reaches the end station, backtrack from the end station to the start station using the parent information collected during the traversal, then the shortest path is found.
5. **Issues Hanlding:**
   - Consider cases such as stations not connected in the network, or multiple paths with the same length.
6. **Improve User Experience by Adding an User Interface:**
   - Use `tkinter` to create a GUI for better display.
