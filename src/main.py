import helper
import sys

try:
    data_path = sys.argv[1]
except IndexError:
    print("Missing an argument for input path!")
    exit()

(rows, cols, reefs, start, end) = helper.read_input(data_path)
binary_map = helper.draw_map(rows, cols, reefs)
path = helper.find_shortest_path(binary_map, start, end, data_path)
map = helper.generate_map(rows, cols, binary_map, start, end, path)
helper.write_output(data_path, map)

