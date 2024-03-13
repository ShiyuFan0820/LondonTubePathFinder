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
