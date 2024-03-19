# LondonTubePathFinder

The goal of this project is to build a station-to-station path-finding system for London tube and find the shortest between two stations.

## TODO List

### Collect Data of London Tube Before Coding
1. Search and download the data of stations of each tube in London.
- [This is the newest tube map of London.](https://tfl.gov.uk/maps/track?intcmp=40400)
2. Read the data file. The original data in `.mat` format and the method to read the data can be found at:

- [Data in .mat format.](https://www.cs.cornell.edu/~arb/data/spatial-underground-London/)

- [How to read the .mat file in Python.](https://stackoverflow.com/questions/874461/read-mat-files-in-python)

3. There's already a organized file about the data of the stations, we can use this directly (This is not the newest tube stations, but we can complete the code first and revise it to the newest one).
- [Organized data in txt file.](https://github.com/mincongzhang/StationPathFinder/blob/master/LondonTube/LondonTube/stations.txt)

### Write the Code
1. **Load Data:**
- Write a class which can convert and return the formated dictionaries of stations information by passing the file name into it.
- In side the class, use pandas to read the data in the txt file, and convert it to three dictionaries.
- One dictionary with ID of each station as key, and the name of each station as value.
- Another dictionary with the name of each station as key, and the ID as value.
- The last dictionary with ID of each station as key, and its neighbours as value.
- Adn this class should also contain methods which can return the name, id, and neighbours. 
2. **Collect User Input:**
- Handle user input to specify the starting station and the end station.
- Handle the situation if the user input the wrong name of the station.
- At this stage it can only identify the same station names as in `station.txt` file, I marked this as an issue, hope to resolve it in the future.
3. **Find the Path:**
- The connection of tube lines is a graph, but it can be extracted separately and simplify it into a tree structure, that is, the starting station is root, the neighbours directly connected to the root are regarded as its children, and the neighbors connected to its neighbors can be regarded as their children, so on and so forth, traverse level by level until the end station.
- To implement traversal mentioned above, BFS algorithm can be used in this situation, but unlike nodes in a tree, they have direction, the direction is from parent nodes to children nodes, in a graph, if two stations are connected, they are each other's neighbour, so this problem should be considered when writing code.
- After finding all possible paths, find the shortest path.
4. **Issues Handling:**
- Consider cases such as stations not connected in the network, or multiple paths with the same length.
6. **Improve User Experience by Adding an User Interface:**
- Use `tkinter` to create a GUI for better display.
