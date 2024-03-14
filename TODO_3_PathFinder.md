```py
from LoadData import StationInfo
class StationNode:
    def __init__(self, id_num):
        self.m_id = id_num
        self.m_children = StationInfo.GetNeighboursFromID(id_num)

    def GetStation(self):
        return self.m_id

    def GetNeighbour(self):
        return self.m_children


class StationTree:
    def __init__(self, from_station_id):
        self.m_root = StationNode(from_station_id)


class StationFinder:
    def GetPaths(self, from_station_id, to_station_id, path = []):
        if from_station_id == to_station_id:
            return path
        path += from_station_id
        tree = StationTree(from_station_id)
        paths = []
        for neighbour in tree.m_root.m_children:
            if neighbour not in path:
                new_paths = self.GetPaths(neighbour, to_station_id, path)
                for p in new_paths:
                    paths.append(p)
        return paths

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
