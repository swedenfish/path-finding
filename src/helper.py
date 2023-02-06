from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def read_input(data_path):
    """
        Read data in and convert them to list of coordinates of reefs
        Args:
            data_path (string): absolute path of the input .txt file
        Return:
            (rows, cols, reefs, start, end) ((int, int, [(int, int)], (int, int), (int, int))): 
                number of rows and columns of the map, list of reef coordinates, start point coordinate, and end point coordinate
    """
    return (0, 0, [], (0, 0), (0, 0))


def write_output(data_path, map):
    """
        Write the output answer into data_path.answer
        Args:
            data_path (string): absolute path of the input .txt file (adding .answer to the end to be the output path)
            map (string): the final map in text version, where sea is '.', reef is 'x', start is 'S', end is 'E', and path are 'O'
        Return:
            success (bool): whether wrting is successful
    """
    return True


def draw_map(rows, cols, reefs, start, end):
    """
        Draw the 0s/1s binary map based on number of rows, number of columns, list of coordinates of reefs, start point coordinate, and end point coordinate
        If start_point or end_point out of map, or either one is at a reef, return an empty map 
        Args:
            rows (int): number of rows in the map
            cols (int): number of columns in the map
            reefs ([(int, int)]): list of coordinates of reefs
            start ((int, int)): start point coordinate
            end ((int, int)): end point coordinate
        Return:
            binary_map ([[int]]): a binary 2d list representing the map, where 0 represents reef and 1 represents sea
    """
    return []


def generate_map(binary_map, start, end, path):
    """
        Convert the binary map into its final text versionm where sea is '.', reef is 'x', start is 'S', end is 'E', and path are 'O'
        Args:
            binary_map ([[int]]): a binary 2d list representing the map, where 0 represents reef and 1 represents sea
            start ((int, int)): start point coordinate
            end ((int, int)): end point coordinate
            path ([(int, int)]): list of coordinates of all points in the path
        Return:
            map (string): the final map in text version, where sea is '.', reef is 'x', start is 'S', end is 'E', and path are 'O'
    """
    return ""


def find_shortest_path(binary_map, start_point, end_point):
    """
        Find shortest path on the binary_map based on start_point and end_point
        If no path or end_point not reachable, return []
        If start_point or end_point out of map, return []
        Args:
            binary_map ([[int]]): 2d list containing 0s and 1s, where 0 represents reef, and 1 represents sea
            start_index ((int, int)): starting point coordinates
            end_index ((int, int)): ending point coordinates
        Return:
            path ([(int, int)]): list of coordinates of all points in the path
    """
    grid = Grid(matrix=binary_map)
    try:
        start = grid.node(start_point[0], start_point[1])
        end = grid.node(end_point[0], end_point[1])
    except IndexError:
        #TODO: distinguish between "start/end out of map error" from "no path error"
        return []
    finder = AStarFinder()
    path, runs = finder.find_path(start, end, grid)
    return path
