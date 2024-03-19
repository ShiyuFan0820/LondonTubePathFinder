# Code
1. The first code I wrote actually uses the DFS to find the path, it recursively call the `GetPaths` method, everytime it pass a children of the previous station node until the children node is equal to the station the user wants to go, if the `paths` is empty means that there is no path from the `from_station` to the `to_station`.
```py
from LoadData import StationInfo
class StationNode:
    def __init__(self, id_num):
        self.m_id = id_num
        self.m_children = StationInfo.GetNeighboursFromID(id_num)

    def GetStation(self):
        return self.m_id

    def GetNeighbours(self):
        return self.m_children


class StationTree:
    def __init__(self, from_station_id):
        self.m_root = StationNode(from_station_id)


class StationFinder:
    def GetPaths(self, from_station_id, to_station_id):
        paths = self.GetPathsto(from_station_id, to_station_id, path = [])
        self.DisplayPaths(from_station_id, to_station_id, paths)
    
    def GetPathsto(self, from_station_id, to_station_id, path = []):
        paths = []
        path.append(from_station_id)
        if from_station_id == to_station_id:
            return path
        tree = StationTree(from_station_id)
        for neighbour in tree.GetNeighbours():
            if neighbour not in path:
                new_paths = self.GetPaths(neighbour, to_station_id, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def DisplayPaths(self, from_station_id, to_station_id, paths):
        from_station = StationInfo.GetNameFromID(from_station_id)
        to_station = StationInfo.GetNameFromID(to_station_id)
        if paths:
            for path in paths:
                path = [StationInfo.GetNameFromID(station_id) for station_id in path]
                print("One possible path:")
                print(f"{"-->".join(path)}")
        else:
            print(f"Sorry, we didn't find a path from {from_station} to {to_station}.")

```

2. This code uses BFS to find the paths between 2 stations.
- 
```py
from LoadData import StationInfo


# Step1: Create a StationFinder to call the GetPaths method
class StationFinder:
    @classmethod
    def GetPaths(cls, from_station, to_station):
        """

        :param from_station: Name of the start station.
        :param to_station:  Name of the end station.
        :return: All possible paths.
        """
        # Convert names to IDs to find neighbours later.
        start_id = StationInfo.GetIDFromName(from_station)
        end_id = StationInfo.GetIDFromName(to_station)

        # Use a set to track stations which are already been visited.
        visited = set()
        # Use a queue to track all the paths.
        queue = []
        # Use paths to store all the possible paths.
        paths = []
        queue.append([start_id])
        visited.add(end_id)
        while queue:
            # Pop the first path from the queue.
            current_path = queue.pop(0)
            # Abstract the last element (this is also the end station id) of the path.
            last_station_id = current_path[-1]
            # Check if it's id is equal to the desired end station id, if it is, add this path to paths.
            if last_station_id == end_id:
                paths.append(current_path)
                continue
            # If still not reaches the end station, we continue to the next level to find the end station.
            neighbour_ids = StationInfo.GetTubeNeisFromID(last_station_id)
            for neighbour_id in neighbour_ids:
                # If one neighbour id is already visit, but it is equal to the end station id, it means this is a new path, we also should add this path to paths.
                if neighbour_id not in visited or neighbour_id == end_id:
                    queue.append(current_path + [neighbour_id])
                    visited.add(neighbour_id)
        return paths


    @classmethod
    def DisplayPaths(cls, paths):
        """

        :param paths: A list include all possible paths.
        :return: Pint all possible paths and print a shortest path.
        """
        if paths:
            shortest_paths = []
            for path in paths:
                path = [StationInfo.GetNameFromID(id) for id in path]
                print("------One possible path------")
                print(f"{"-->".join(path)}\n")
                if len(shortest_paths) == 0 or len(shortest_paths[0]) == len(path):
                    shortest_paths.append(path)
                elif len(shortest_paths[0]) > len(path):
                    shortest_paths.pop()
                    shortest_paths.append(path)
            for shortest_path in shortest_paths:
                print("------Shortest path------")
                print(f"{"-->".join(shortest_path)}\n")
            return
        print(f"Sorry, we didn't find a path, please try other station.")
        return

```

# Issues Recorded

1. No need to create a real tree.

At the beginning I wanted to create a tree by defining `StationTree` and `StationNode` class, and make start station as root, and all neighbours are children, add all children level by level until the end station, after finishing building the tree, traverse from the start station to the end station to find all possible paths, this is not efficient, and as these stations' connection is a graph, when I first ran the `GetPaths` in `main.py`, it raised an error, `RecursionError: maximum recursion depth exceeded`.

<div align=center>
<img width="550" alt="image" src="https://github.com/ShiyuFan0820/LondonTubePathFinder/assets/149340606/c6f03571-4362-405b-b345-2c6d156a36b5">
</div>

Then I realise all station IDs and their neighbours are stored in a dictionary using the class in `LoadData`, this means they are already connected to each other, so I don't need to create a tree to connect them again.

2. 


