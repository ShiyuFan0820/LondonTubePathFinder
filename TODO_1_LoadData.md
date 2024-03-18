# TODO 1: Write a Class to Load Data File

**Explanation:**
1. If `index_co`l is not assigned `False`, the column `ID` will not be recognize, instead, it will be treated as index in the table.
2. When reading the file using pandas, the column `TubeNeighbour` and `TrainNeighbour` will be convert to a string, for example:
```py
# Data in the file:
ID|Name|TubeNeighbour|TrainNeighbour
0|LiverpoolStreetStation|1,2,3,4,6,7|2,3,5,7,14,15
1|Bank(Monument)|0,2,5,8,9,10,11,12|2,3,4,8,11,12

# After reading by pandas the neighbour will be displayed like:
"1,2,3,4,6,7"
"2,3,5,7,14,15"
"0,2,5,8,9,10,11,12"
"2,3,4,8,11,12"
```
But we want each neighbour station to be stored separately as an ID in the dictionary `m_id_neighbours_dict`, we can use dictionary comprehension to convert strings to separate ID integers.

3. Use `@classmethod` to access the class attributes (variables that belongs to a class rather than to instances of the class, also means variables are defined outside of any method within the class, including the `__init__` method.) without defining an instance.
4. Always remember that variables starting with `m_` are accessible inside class and cannot be accessed outside, so we have to create methods that can access return the value of variables starting with `m_`.

**The code is:**
```py
import pandas as pd


class StationInfo:
    m_name_to_id_dict = None
    m_id_to_name_dict = None
    m_id_neighbours_dict = None

    @classmethod
    def LoadData(cls, filename):
        data = pd.read_csv(filename, delimiter="|", index_col=False)
        cls.m_name_to_id_dict = dict(zip(data["Name"], data["ID"]))
        cls.m_id_to_name_dict = dict(zip(data["ID"], data["Name"]))
        cls.m_id_neighbours_dict = {row["ID"]: [[int(id) for id in row["TubeNeighbour"].split(",")], [int(id) for id in row["TrainNeighbour"].split(",")]] for index, row in data.iterrows()}

    @classmethod
    def GetNameFromID(cls, id_num):
        return cls.m_id_to_name_dict[id_num]

    @classmethod
    def GetIDFromName(cls, name):
        return cls.m_name_to_id_dict[name]

    @classmethod
    def GetTubeNeisFromID(cls, id_num):
        return cls.m_id_neighbours_dict[id_num][0]

    @classmethod
    def GetTrainNeisFromID(cls, id_num):
        return cls.m_id_neighbours_dict[id_num][1]

```
