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
        # Step7: After finishing finding all paths we can create a DisplayPaths to print all the possible paths and also choose the shortest path.
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
