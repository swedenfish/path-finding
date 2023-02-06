from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def find_path(map, start_point, end_point):
    """
        Find shortest path on the map based on start_point and end_point. 
        If no path or end_point not reachable, return []
        If start_point or end_point out of map, return [].
        Args:
            map ([[int]]): 2d list containing 0s and 1s, where 0 represents reef, and 1 represents sea.
            start_index ((int, int)): starting point coordinates
            end_index ((int, int)): ending point coordinates
        Return:
            path ([(int, int)]): list of coordinates which are all points in the path
    """
    grid = Grid(matrix=map)
    try:
        start = grid.node(start_point[0], start_point[1])
        end = grid.node(end_point[0], end_point[1])
    except IndexError:
        #TODO: distinguish between "start/end out of map error" from "no path error"
        return []
    finder = AStarFinder()
    path, runs = finder.find_path(start, end, grid)
    return path
