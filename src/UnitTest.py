import unittest
from unittest.mock import patch
from LoadData import StationInfo
from PathFinder import StationFinder


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

class testStationFinder(unittest.TestCase):
    def setUp(self):
        self.m_file = "/Users/fanfan/Downloads/200-Learning/250-Com/Pycharm/pythonProject/LondonTube/stations.txt"
        self.m_test_from_1 = 'BethnalGreen'
        self.m_test_from_2 = 'CustomHouseforExCel'
        self.m_test_from_3 = 'Pinner'
        self.m_test_to_1 = 'DevonsRoad'
        self.m_test_to_2 = 'Beckton'
        self.m_test_to_3 = 'Rickmansworth'
        self.m_path_1 = [[6, 17, 41, 63]]
        self.m_path_2 = [[103, 136, 166, 189, 219, 247, 303]]
        self.m_path_3 = [[335, 336, 337, 338, 341]]
        self.m_display_path_1 = 'BethnalGreen-->MileEnd-->BowRoad(BowChurch)-->DevonsRoad\n'
        self.m_display_path_2 = 'CustomHouseforExCel-->PrinceRegent-->RoyalAlbert-->BecktonPark-->Cyprus-->GallionsReach-->Beckton\n'
        self.m_display_path_3 = 'Pinner-->NorthwoodHills-->Northwood-->MoorPark-->Rickmansworth\n'
        StationInfo.LoadData(self.m_file)

    def testShortestPaths(self):
        test_path_1 = StationFinder.GetPaths(self.m_test_from_1, self.m_test_to_1)
        test_path_2 = StationFinder.GetPaths(self.m_test_from_2, self.m_test_to_2)
        test_path_3 = StationFinder.GetPaths(self.m_test_from_3, self.m_test_to_3)
        test_shortest_path_1 = StationFinder.ShortestPath(test_path_1)
        test_shortest_path_2 = StationFinder.ShortestPath(test_path_2)
        test_shortest_path_3 = StationFinder.ShortestPath(test_path_3)
        self.assertEqual(test_shortest_path_1, self.m_path_1)
        self.assertEqual(test_shortest_path_2, self.m_path_2)
        self.assertEqual(test_shortest_path_3, self.m_path_3)

    @patch('builtins.print')
    def testDisplayPaths(self, mock_print):
        test_path_1 = StationFinder.GetPaths(self.m_test_from_1, self.m_test_to_1)
        test_shortest_path_1 = StationFinder.ShortestPath(test_path_1)
        StationFinder.DisplayPaths(test_shortest_path_1)
        expected_call_1 = self.m_display_path_1
        mock_print.assert_called_with(expected_call_1)

        test_path_2 = StationFinder.GetPaths(self.m_test_from_2, self.m_test_to_2)
        test_shortest_path_2 = StationFinder.ShortestPath(test_path_2)
        StationFinder.DisplayPaths(test_shortest_path_2)
        expected_call_2 = self.m_display_path_2
        mock_print.assert_called_with(expected_call_2)

        test_path_3 = StationFinder.GetPaths(self.m_test_from_3, self.m_test_to_3)
        test_shortest_path_3 = StationFinder.ShortestPath(test_path_3)
        StationFinder.DisplayPaths(test_shortest_path_3)
        expected_call_3 = self.m_display_path_3
        mock_print.assert_called_with(expected_call_3)
