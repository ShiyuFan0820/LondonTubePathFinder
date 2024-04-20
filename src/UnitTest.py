import unittest
from LoadData import StationInfo

# Test if StationInfo works well
class TestStationInfo(unittest.TestCase):
    def setUp(self):
        self.m_file = "/Users/fanfan/Downloads/200-Learning/250-Com/Pycharm/pythonProject/LondonTube/stations.txt"
        self.m_test_name_1 = 'LondonFields'
        self.m_test_name_2 = 'WarrenStreet'
        self.m_test_name_3 = 'TheobaldsGrove'
        self.m_test_id_1 = 40
        self.m_test_id_2 = 107
        self.m_test_id_3 = 293
        self.m_test_tube_neis_1 = [16,62]
        self.m_test_tube_neis_2 = [76,89,142]
        self.m_test_tube_neis_3 = [292,294]
        self.m_test_trai_neis_1 = [14]
        self.m_test_trai_neis_2 = [8,10]
        self.m_test_trai_neis_3 = [14]
        StationInfo.LoadData(self.m_file)

    def testGetNameIDDict(self):
        test_dict = StationInfo.GetNameIDDict()
        self.assertIsInstance(test_dict, dict)

    def testGetIDNameDict(self):
        test_dict = StationInfo.GetIDNameDict()
        self.assertIsInstance(test_dict, dict)

    def testGetIDNeisDict(self):
        test_dict = StationInfo.GetIDNeisDict()
        self.assertIsInstance(test_dict, dict)

    def testGetNameFromID(self):
        test_name_1 = StationInfo.GetNameFromID(self.m_test_id_1)
        test_name_2 = StationInfo.GetNameFromID(self.m_test_id_2)
        test_name_3 = StationInfo.GetNameFromID(self.m_test_id_3)
        self.assertEqual(test_name_1, self.m_test_name_1)
        self.assertEqual(test_name_2, self.m_test_name_2)
        self.assertEqual(test_name_3, self.m_test_name_3)

    def testGetIDFromName(self):
        test_id_1 = StationInfo.GetIDFromName(self.m_test_name_1)
        test_id_2 = StationInfo.GetIDFromName(self.m_test_name_2)
        test_id_3 = StationInfo.GetIDFromName(self.m_test_name_3)
        self.assertEqual(test_id_1, self.m_test_id_1)
        self.assertEqual(test_id_2, self.m_test_id_2)
        self.assertEqual(test_id_3, self.m_test_id_3)

    def testGetTubeNeisFromID(self):
        test_tube_neis_1 = StationInfo.GetTubeNeisFromID(self.m_test_id_1)
        test_tube_neis_2 = StationInfo.GetTubeNeisFromID(self.m_test_id_2)
        test_tube_neis_3 = StationInfo.GetTubeNeisFromID(self.m_test_id_3)
        self.assertEqual(test_tube_neis_1, self.m_test_tube_neis_1)
        self.assertEqual(test_tube_neis_2, self.m_test_tube_neis_2)
        self.assertEqual(test_tube_neis_3, self.m_test_tube_neis_3)

    def testGetTrainNeisFromID(self):
        test_trai_neis_1 = StationInfo.GetTrainNeisFromID(self.m_test_id_1)
        test_trai_neis_2 = StationInfo.GetTrainNeisFromID(self.m_test_id_2)
        test_trai_neis_3 = StationInfo.GetTrainNeisFromID(self.m_test_id_3)
        self.assertEqual(test_trai_neis_1, self.m_test_trai_neis_1)
        self.assertEqual(test_trai_neis_2, self.m_test_trai_neis_2)
        self.assertEqual(test_trai_neis_3, self.m_test_trai_neis_3)
