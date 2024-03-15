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


class StationTree:
    def __init__(self, from_station_id):
        self.m_from_station_node = StationNode(from_station_id)

    def GetPathsTo(self, to_station_id):
        queue = []
        paths = []
        start_station = self.m_from_station_node
        neighbours = start_station.GetNeighbours()
        if neighbours:
            for neighbour in neighbours:
                queue.append([start_station, neighbour])
        while queue:
            path = queue.pop(0)
            if path[-1].m_id == to_station_id:
                path = [station_node.m_id for station_node in path]
                paths.append(path)
            for neighbour in path[-1].GetNeighbours():
                queue.append(path + [neighbour])
        return paths


class StationFinder:
    def GetPaths(self, from_station_id, to_station_id):
        pass


```
