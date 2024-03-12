# TODO 1: Write a Class to Load Data File

```py
import pandas as pd
filename = "stations.txt"


class StationInfo:
    def __init__(self):
        self.m_data = pd.read_csv(filename, delimiter="|", index_col=False)
        self.m_id_to_name_dict = dict(zip(self.m_data["ID"], self.m_data["Name"]))
        self.m_name_to_id_dict = dict(zip(self.m_data["Name"], self.m_data["ID"]))
        self.m_id_neighbours_dict =

```
