import pandas as pd


class StationInfo:
    m_name_to_id_dict = None
    m_id_to_name_dict = None
    m_id_neighbours_dict = None

    @classmethod
    def LoadData(cls, filename):
        """

        :param filename: The name/path of the file.
        """
        data = pd.read_csv(filename, delimiter="|", index_col=False)
        cls.m_name_to_id_dict = dict(zip(data["Name"], data["ID"]))
        cls.m_id_to_name_dict = dict(zip(data["ID"], data["Name"]))
        cls.m_id_neighbours_dict = {row["ID"]: [[int(id) for id in row["TubeNeighbour"].split(",")], [int(id) for id in row["TrainNeighbour"].split(",")]] for index, row in data.iterrows()}

    @classmethod
    def GetNameIDDict(cls):
        """

        :return: A dictionary in which keys are name, values are IDs of stations.
        """
        return cls.m_name_to_id_dict

    @classmethod
    def GetIDNameDict(cls):
        """

        :return: A dictionary in which keys are IDs, values are names of stations.
        """
        return cls.m_id_to_name_dict

    @classmethod
    def GetIDNeisDict(cls):
        """

        :return: A dictionary in which keys are IDs, values are a list in which tube and train neighbour IDs of stations are elements.
        """
        return cls.m_id_neighbours_dict

    @classmethod
    def GetNameFromID(cls, id_num):
        """

        :param id_num: ID of the station.
        :return: Name of the station.
        """
        return cls.m_id_to_name_dict[id_num]

    @classmethod
    def GetIDFromName(cls, name):
        """

        :param name: Name of the station.
        :return: ID of the station.
        """
        return cls.m_name_to_id_dict[name]

    @classmethod
    def GetTubeNeisFromID(cls, id_num):
        """

        :param id_num: ID of the station.
        :return: A list of IDs of the station's tube neighbours.
        """
        return cls.m_id_neighbours_dict[id_num][0]

    @classmethod
    def GetTrainNeisFromID(cls, id_num):
        """

        :param id_num: ID of the station.
        :return: A list of IDs of the station's train neighbours.
        """
        return cls.m_id_neighbours_dict[id_num][1]
