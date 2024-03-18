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
