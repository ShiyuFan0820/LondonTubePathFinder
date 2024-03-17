# Code
1. This code actually uses the DFS to find the path, it recursively call the `GetPaths` method, everytime it pass a children of the previous station node until the children node is equal to the station the user wants to go, if the `paths` is empty means that there is no path from the `from_station` to the `to_station`.
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
- First creating a tree, whose root is the `from_station` node, every node has its own instance's attributes, `m_id` stores the id information of the node, `m_neighbours` is a list, stores all the neighbour nodes, `m_parent` stores the parent of this node, `self.InsertNeighbours()` will call this method to add all neighbours and complete the tree strucutre. The reason why `m_parent` is needed is that stations information organized in `station.txt` has no direction, e.g. station1 and station2 is connected, so station2 is in the neighbour list of station1 and station1 is also in the neighbour list of station2, when we want to creat a tree whose root is station1, we need to add station2 node in the `m_neighbours` of station1, and we also need to find the neighbours of station2 and add them as nodes to the `m_neighbours` of station2, so we need to track the direction to prevent adding station1 to the `m_neighbours` of station2.
- After creating the tree we can use BFS to find all the possible paths, define a `queue` to record all the paths we will visit, instead of just enqueuing the nodes we are going to visit, we enqueue all the nodes before this node to the queue as a list to keep tracking the path, everytime we dequeue a path list from the queue, check the last element in the path list, if it is equal to the `to_station`, this means we find a path successfully, if not we keep appending neighours to the list path and enqueue it till we find a path or till there is no neighours of the last element, and define a `paths` to record all the possible paths to the `to_station`.
- After finding all possible paths, we call `DisplayPaths` to print the paths bewteen two stations, because `paths` only stores the id of the station, we need to convert all ids to station names. 
```py
from LoadData import StationInfo
class StationNode:
    def __init__(self, id_num, parent=None):
        self.m_id = id_num
        self.m_neighbours = []
        self.m_parent = parent
        self.InsertNeighbours(id_num, parent)

    def InsertNeighbours(self, id_num, parent_id):
        neighbour_ids = StationInfo.GetNeighboursFromID(id_num)
        for neighbour_id in neighbour_ids:
            if neighbour_id != parent_id:
                self.m_neighbours.append(StationNode(neighbour_id, id_num))

    def GetNeighbours(self):
        return self.m_neighbours

    def GetStationID(self):
        return self.m_id


class StationTree:
    def __init__(self, from_station_id):
        self.m_from_station_node = StationNode(from_station_id)

    def GetStartNode(self):
        return self.m_from_station_node

    def GetPathsTo(self, to_station_id):
        queue = []
        paths = []
        start_station_node = self.GetStartNode()
        neighbour_nodes = start_station_node.GetNeighbours()
        if neighbour_nodes:
            for neighbour_node in neighbour_nodes:
                queue.append([start_station_node, neighbour_node])
        while queue:
            path = queue.pop(0)
            if path[-1].GetStationID() == to_station_id:
                path = [station_node.GetStationID() for station_node in path]
                paths.append(path)
            else:
                for neighbour_node in path[-1].GetNeighbours():
                    queue.append(path + [neighbour_node])
        return paths


class StationFinder:
    @classmethod
    def GetPaths(cls, from_station_id, to_station_id, from_station, to_station):
        """

        :param from_station_id: id of the start station
        :param to_station_id:  id of the end station
        :param from_station: name of the start station
        :param to_station:  name of the end station
        :return: return all the possible paths
        """
        station_tree = StationTree(from_station_id)
        paths = station_tree.GetPathsTo(to_station_id)
        if paths:
            cls.DisplayPaths(paths)
            cls.ShortestPath(paths)
        else:
            print(f"Sorry, we didn't find a path from {from_station} to {to_station}.")

    @classmethod
    def DisplayPaths(cls, paths):
        shortest_paths = []
        for path in paths:
            path = [StationInfo.GetNameFromID(station_node.GetStationID()) for station_node in path]
            print("One possible path:")
            print(f"{"-->".join(path)}")
            if len(shortest_paths) != 0:
                if len(shortest_paths[0]) > len(path):
                    shortest_paths.pop()
                shortest_paths.append(path)
            else:
                shortest_paths.append(path)
        for shortest_path in shortest_paths:
            print("Shortest path:")
            print(f"{"-->".join(shortest_path)}")

```

# Issues

1. When I ran the `GetPaths` in `main.py`, it notified me `RecursionError: maximum recursion depth exceeded` when it called the `InsertNeighbours` recursively.

<div align=center>
<img width="550" alt="image" src="https://github.com/ShiyuFan0820/LondonTubePathFinder/assets/149340606/c6f03571-4362-405b-b345-2c6d156a36b5">
</div>

**Solutions： The reason why it exceeded the maximum recursion is that we didn't track the visited station, we only track the parent station of the current station, how ever, one station may have not one parent station, so we may create the tree recursively and never end, and it reached the maximum recursion depth in the end, to solve it no longer infinite creating tree, we can set a class attribute hashset `visited_ids` to record the visited station ids.**

2. After creating the `visited_ids` to track the visited station ids, another issue occurs, when the there are two paths which can get to the desired station, if we add the desired station as a node to the neighbour list of one of the stations, this desired station will be added to the `visited_ids`, and when we find the neighbour of another station among the two stations, its neighbour has already been added to the `visited_ids`, so we can't add all possible paths.

**Solutions： To solve this situation, we can simply create a new class for the desired station called `StationNodeEnd`, it will have no neighbour attribute, just the id for itself, cause we already find the desired station we don't need to find its neighbours, and we can add an additional contidion when we are checking the neighbour of a station, if the neighbour is in the `visited_ids`, and if is equal to the `to_station_id`, it will call the `StationNodeEnd` and generate a node without neighbours and append this new now to the neighbour list of its parent station, even if this desired station is already added in another station's neighbour list, it can also be added in the neighbour list of other station's.** 

The revised code:
```py
from LoadData import StationInfo

# Step4: Create the StationNode class to store all the information of the station nodes and insert all neighbour nodes.
class StationNode:
    # Use a set to track stations which are already been visited.
    visited_ids = set()

    def __init__(self, id_num, to_station_id):
        self.m_id = id_num
        self.m_neighbours = []
        StationNode.visited_ids.add(id_num)
        self.InsertNeighbours(id_num, to_station_id)

    def InsertNeighbours(self, id_num, to_station_id):
        neighbour_ids = StationInfo.GetNeighboursFromID(id_num)
        for neighbour_id in neighbour_ids:
            if neighbour_id not in StationNode.visited_ids or neighbour_id == to_station_id:
                if neighbour_id == to_station_id:
                    # If the neighbour_id is equal to our end station, we create an other node which doesn't have a neighbour to store the information, cause we already find the end station, we don't need to visit its neighbours.
                    self.m_neighbours.append(StationNodeEnd(neighbour_id))
                else:
                    self.m_neighbours.append(StationNode(neighbour_id, to_station_id))

    def GetNeighbours(self):
        return self.m_neighbours

    def GetStationID(self):
        return self.m_id

# Step5: Create another StationNodeEnd class to store the end station node.
class StationNodeEnd:
    def __init__(self, id_num_end):
        self.m_id_end = id_num_end

    def GetNeighbours(self):
        return None

    def GetStationID(self):
        return self.m_id_end

# Step3: Complete the StationTree class, define a StationNode class to store all the station node information, including the id number of the station node and the neighbour nodes.
class StationTree:
    def __init__(self, from_station_id, to_station_id):
        self.m_from_station_node = StationNode(from_station_id, to_station_id)

    def GetStartNode(self):
        return self.m_from_station_node
    # Step7: Create the GetPathsTo method.
    def GetPathsTo(self, to_station_id):
        # Use a queue to track all the paths.
        queue = []
        # Use paths to store all the possible paths.
        paths = []
        start_station_node = self.GetStartNode()
        neighbour_nodes = start_station_node.GetNeighbours()
        if neighbour_nodes:
            for neighbour_node in neighbour_nodes:
                # Instead of adding all station in the queue, we can add paths we are going to explore in the queue.
                queue.append([start_station_node, neighbour_node])
        while queue:
            path = queue.pop(0)
            # Every time we only check the last station in the path to see if is equal to the end station, if it is, then this path is one possible path.
            if path[-1].GetStationID() == to_station_id:
                path = [station_node.GetStationID() for station_node in path]
                paths.append(path)
            else:
                # If the last station is not the end station, we need to visit stations in the next level, and add all possible paths in the next level to the queue.
                for neighbour_node in path[-1].GetNeighbours():
                    # path is a list, if we want to add the new neighbour_node to a list we also need to convert the neighbour_node to a list.
                    queue.append(path + [neighbour_node])
        return paths

# Step1: Create a StationFinder to call the GetPaths method
class StationFinder:
    @classmethod
    def GetPaths(cls, from_station_id, to_station_id, from_station, to_station):
        """

        :param from_station_id: id of the start station
        :param to_station_id:  id of the end station
        :param from_station: name of the start station
        :param to_station:  name of the end station
        :return: return all the possible paths
        """
        # Step2: Inside the GetPaths method, call StationTree method to create the tree whose root is the start station.
        station_tree = StationTree(from_station_id, to_station_id)
        # Step6: When the tree is completed, we can use BFS to find the paths bewteen the 2 stations, we create a GetPathsTo method to find all the possible paths and return the result.
        paths = station_tree.GetPathsTo(to_station_id)
        # Step7: After finishing finding all paths we can create a DisplayPaths to print all the possible paths and also choose a shortest path for us.
        if paths:
            cls.DisplayPaths(paths)
        else:
            print(f"Sorry, we didn't find a path from {from_station} to {to_station}.")

    @classmethod
    def DisplayPaths(cls, paths):
        shortest_paths = []
        for path in paths:
            path = [StationInfo.GetNameFromID(id) for id in path]
            print("------One possible path------")
            print(f"{"-->".join(path)}")
            if len(shortest_paths) != 0:
                if len(shortest_paths[0]) > len(path):
                    shortest_paths.pop()
                    shortest_paths.append(path)
            else:
                shortest_paths.append(path)
        for shortest_path in shortest_paths:
            print("------Shortest path------")
            print(f"{"-->".join(shortest_path)}")

```
