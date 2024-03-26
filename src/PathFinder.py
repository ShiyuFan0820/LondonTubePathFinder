from LoadData import StationInfo


# Step1: Create a StationFinder to call the GetPaths method
class StationFinder:
    @classmethod
    def GetPaths(cls, from_station, to_station):
        """

        :param from_station: Name of the start station.
        :param to_station:  Name of the end station.
        :return: All possible paths.
        """
        # Convert names to IDs to find neighbours later.
        start_id = StationInfo.GetIDFromName(from_station)
        end_id = StationInfo.GetIDFromName(to_station)

        # Use a set to track stations which are already been visited.
        visited = set()
        # Use a queue to track all the paths.
        queue = []
        # Use paths to store all the possible paths.
        paths = []
        queue.append([start_id])
        visited.add(end_id)
        while queue:
            # Pop the first path from the queue.
            current_path = queue.pop(0)
            # Abstract the last element (this is also the end station id) of the path.
            last_station_id = current_path[-1]
            # Check if it's id is equal to the desired end station id, if it is, add this path to paths.
            if last_station_id == end_id:
                paths.append(current_path)
                continue
            # If still not reaches the end station, we continue to the next level to find the end station.
            neighbour_ids = StationInfo.GetTubeNeisFromID(last_station_id)
            for neighbour_id in neighbour_ids:
                # If one neighbour id is already visit, but it is equal to the end station id, it means this is a new path, we also should add this path to paths.
                if neighbour_id not in visited or neighbour_id == end_id:
                    queue.append(current_path + [neighbour_id])
                    visited.add(neighbour_id)
        return paths


    @classmethod
    def DisplayAllPaths(cls, paths):
        """

        :param paths: A list include all possible paths.
        :return: Pint all possible paths.
        """
        for path in paths:
            path = [StationInfo.GetNameFromID(id) for id in path]
            print("------One possible path------")
            print(f"{"-->".join(path)}\n")
        return

    @classmethod
    def ShortestPath(cls, paths):
        """

        :param paths: A list of all possible paths.
        :return: The shortest path.
        """
        shortest_paths = []
        for path in paths:
            path = [StationInfo.GetNameFromID(id) for id in path]
            if len(shortest_paths) == 0 or len(shortest_paths[0]) == len(path):
                shortest_paths.append(path)
            elif len(shortest_paths[0]) > len(path):
                shortest_paths.pop()
                shortest_paths.append(path)
        return shortest_paths

    @classmethod
    def DisplayShortestPath(cls, shortest_path):
        for path in shortest_path:
            print("------Shortest path------")
            print(f"{"-->".join(path)}\n")
        return

