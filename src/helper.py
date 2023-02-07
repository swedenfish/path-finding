from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import re

def read_input(data_path):
    """
        Read data in and convert them to list of coordinates of reefs and other later needed parameters
        Args:
            data_path (string): absolute path of the input .txt file
        Return:
            (rows, cols, reefs, start, end) ((int, int, [(int, int)], (int, int), (int, int))): 
                number of rows and columns of the map, list of reef coordinates, start point coordinate, and end point coordinate
    """
    rows = 0
    cols = 0
    reefs = []
    start = (0, 0)
    end = (0, 0)
    
    # Error: file not exist at data_path
    try:
        file = open(data_path, "r")
    except FileNotFoundError:
        print("File does not exist at \"" + data_path + "\"")
        exit()
    except Exception as e:
        print("Invalid path!")
        exit()
    text = file.read()
    text = text.replace("\n", "")
    coordinate_list = text.split(",")
    file.close()
    
    filtered_coordinate_list = list(filter(valid, coordinate_list))
    
    if(len(filtered_coordinate_list) < 2):
    # Error: must have at least 2 coordinates in input .txt file
        print("Too few input coordinates!")
        write_output(data_path, "error")
        exit()
        
    start = convert(filtered_coordinate_list[0])
    end = convert(filtered_coordinate_list[-1])
    if start == end:
    # Same start point and end point, only display end point
        print("Start point and end point at same position! Will only display the end point!")
    filtered_coordinate_list.pop(0)
    filtered_coordinate_list.pop(-1)
    
    for reef_coordinate_text in filtered_coordinate_list:
        (x, y) = convert(reef_coordinate_text)
        if x+1 > cols:
            cols = x+1
        if y+1 > rows:
            rows = y+1
        if (x, y) == start:
        # Error: start point at a reef
            print("Start point at a reef!")
            write_output(data_path, "error")
            exit()
        if (x, y) == end:
            # Error: end point at a reef
            print("End point at a reef!")
            write_output(data_path, "error")
            exit()
        reefs.append((x, y))
    # Handle cases when input contains repeated coordinates
    reefs = list(set(reefs))

    (x_start, y_start) = start
    (x_end, y_end) = end
    if(x_start >= cols or y_start >= rows):
    # Error: start point's coordinate must be inside the map
        print("Start point out of map!")
        write_output(data_path, "error")
        exit()
    if(x_end >= cols or y_end >= rows):
    # Error: end point's coordinate must be inside the map
        print("End point out of map!")
        write_output(data_path, "error")
        exit()
        
    return (rows, cols, reefs, start, end)


def valid(coordinate_text):
    """
        Check whether a coordinate_text is valid
        Valid examples: x1y1 x0y0 x1y0 x100y0 x15y28
        Invalid examples: x-1y0 xy0 xxy0 x00y1 x100y 
        Args:
            coordinate_text (string): a string contains a unit of coordinate information (each unit spliting by ',')
        Returns:
            is_valid (bool): whether this coordinate_text is valid and should not be removed
    """
    # regx representing: x + any non-negative integer + y + any non-negative integer
    pattern = re.compile("^x(0|[1-9]\d*)y(0|[1-9]\d*)$")
    is_valid = pattern.match(coordinate_text)
    return is_valid


def convert(coordinate_text):
    """
        Convert a coordinate_text into a tuple representing the coordinates
        Args:
            coordinate_text (string): a string contains a unit of coordinate information (each unit spliting by ',')
        Returns:
            (x, y) ((int, int)): the coordinate representation of coordinate_text
    """
    if not valid(coordinate_text):
    # This should never occur unless convert is used before filtering out invalid corrdinate_text
        print("Invalid coordinate_text: " + coordinate_text)
        exit()
    index_of_y = coordinate_text.index("y")
    x = int(coordinate_text[1:index_of_y])
    y = int(coordinate_text[index_of_y+1:])
    return (x, y)


def write_output(data_path, map):
    """
        Write the output answer into data_path.answer
        Args:
            data_path (string): absolute path of the input .txt file (adding .answer to the end to be the output path)
            map (string): the final map in text version, where sea is '.', reef is 'x', start is 'S', end is 'E', and path are 'O'
        Return:
            success (bool): whether wrting is successful
    """
    try:
    # Should never occur unless calling write_output before read_input being called.
        file = open(data_path + ".answer", "w")
    except Exception as e:
        print("Invalid path: \"" + data_path + "\"")
        exit()
        
    file.write(map)
    file.close()
    print("Write output successfully")
    return True


def draw_map(rows, cols, reefs):
    """
        Draw the 0s/1s binary map based on number of rows, number of columns, and list of coordinates of reefs
        If start_point or end_point out of map, or either one is at a reef, return an empty map 
        Args:
            rows (int): number of rows in the map
            cols (int): number of columns in the map
            reefs ([(int, int)]): list of coordinates of reefs
        Return:
            binary_map ([[int]]): a binary 2d list representing the map, where 0 represents reef and 1 represents sea
    """
    binary_map = [[1 for i in range(cols)] for j in range(rows)]
    for reef in reefs:
        (x, y) = reef
        binary_map[y][x] = 0
    return binary_map


def generate_map(rows, cols, binary_map, start, end, path):
    """
        Convert the binary map into its final text versionm where sea is '.', reef is 'x', start is 'S', end is 'E', and path are 'O'
        Args:
            rows (int): number of rows in the map
            cols (int): number of columns in the map
            binary_map ([[int]]): a binary 2d list representing the map, where 0 represents reef and 1 represents sea
            start ((int, int)): start point coordinate
            end ((int, int)): end point coordinate
            path ([(int, int)]): list of coordinates of all points in the path
        Return:
            map (string): the final map in text version, where sea is '.', reef is 'x', start is 'S', end is 'E', and path are 'O'
    """
    map = ""
    char_map = [['.' for i in range(cols)] for j in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if not binary_map[i][j]:
                char_map[i][j] = 'x'
    
    for (x, y) in path:
        char_map[y][x] = 'O'
    
    (x_start, y_start) = start
    (x_end, y_end) = end
    char_map[y_start][x_start] = 'S'
    char_map[y_end][x_end] = 'E'
    
    for i in range(rows):
        for j in range(cols):
            map += char_map[i][j]
        map += '\n'
    map = map.strip()
    return map


def find_shortest_path(binary_map, start_point, end_point, data_path):
    """
        Find shortest path on the binary_map based on start_point and end_point
        If no path or end_point not reachable, return []
        Args:
            binary_map ([[int]]): 2d list containing 0s and 1s, where 0 represents reef, and 1 represents sea
            start_index ((int, int)): starting point coordinates
            end_index ((int, int)): ending point coordinates
            data_path (string): absolute path of the input .txt file (being used here when handling error cases)
        Return:
            path ([(int, int)]): list of coordinates of all points in the path
    """
    grid = Grid(matrix=binary_map)
    try:
        start = grid.node(start_point[0], start_point[1])
        end = grid.node(end_point[0], end_point[1])
    except IndexError:
    # Error: this error should never occur because of previous condition checking in function read_input
        print("Start or end point out of map")
        write_output(data_path, "error")
        exit()
    finder = AStarFinder()
    path, runs = finder.find_path(start, end, grid)
    if path == []:
    # Error: No path because all possible roads to end point are blocked
        print("No valid path!")
        write_output(data_path, "error")
        exit()
    return path
