import pandas as pd
filename = "stations.txt"


class StationInfo:
    m_data = pd.read_csv(filename, delimiter="|", index_col=False)
    m_id_to_name_dict = dict(zip(m_data["ID"], m_data["Name"]))
    m_name_to_id_dict = dict(zip(m_data["Name"], m_data["ID"]))
    m_id_neighbours_dict = {row["ID"]: [[int(id) for id in row["TubeNeighbour"].split(",")], [int(id) for id in row["TrainNeighbour"].split(",")]] for index, row in m_data.iterrows()}

    @classmethod
    def GetNameFromID(cls, id_num):
        return cls.m_id_to_name_dict[id_num]

    @classmethod
    def GetIDFromName(cls, name):
        return cls.m_name_to_id_dict[name]

    @classmethod
    def GetNeighboursFromID(cls, id_num):
        return cls.m_id_neighbours_dict[id_num][0]
