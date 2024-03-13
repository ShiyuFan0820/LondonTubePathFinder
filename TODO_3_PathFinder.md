```py
class StationNode:
    def __init__(self, id_num):
        self.m_id = id_num

    def InserNeighbours(self, neighbour_ids):
        pass

    def GetNeighbours(self):
        pass


class StationTree:
    def __init__(self, from_station_id):
        self.m_root = StationNode(from_station_id)


class StationFinder:
    def GetPaths(self, from_station_id, to_station_id):
        tree = StationTree(from_station_id)

```
