# TODO 1: Write a Class to Load Data File

**Explanation:**
1. If `index_co`l is not assigned `False`, the column `ID` will not be recognize, instead, it will be treated as index in the table.
2. When reading the file using pandas, the column `TubeNeighbour` and `TrainNeighbour` will be convert to a string, e.g.:
```py
# Data in the file:
ID|Name|TubeNeighbour|TrainNeighbour
0|LiverpoolStreetStation|1,2,3,4,6,7|2,3,5,7,14,15
1|Bank(Monument)|0,2,5,8,9,10,11,12|2,3,4,8,11,12

# After reading by pandas they will be like:
"1,2,3,4,6,7"
"2,3,5,7,14,15"
"0,2,5,8,9,10,11,12"
"2,3,4,8,11,12"
```
But we want each neighbour station to be stored separately as an ID in the dictionary `m_id_neighbours_dict`, we can use dictionary comprehension to convert strings to separate ID integers.
3. Use `@classmethod` to access the class attributes without defining an instance.


```py
import pandas as pd
filename = "stations.txt"


class StationInfo:
    m_data = pd.read_csv(filename, delimiter="|", index_col=False)
    m_id_to_name_dict = dict(zip(m_data["ID"], m_data["Name"]))
    m_name_to_id_dict = dict(zip(m_data["Name"], m_data["ID"]))
    m_id_neighbours_dict = {row["ID"]: [[int(id) for id in row["TubeNeighbour"] if id != ","], [int(id) for id in row["TrainNeighbour"] if id != ","]] for index, row in m_data.iterrows()}

    @classmethod
    def GetNameFromID(cls, id):
        return cls.m_id_to_name_dict[id]

    @classmethod
    def GetIDFromName(cls, name):
        return cls.m_name_to_id_dict[name]

    @classmethod
    def GetNeighboursFromID(cls, id):
        return cls.m_id_neighbours_dict[id][0]





```
