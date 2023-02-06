import helper
import sys

#TODO: handle command line arguements
data_path = sys.argv[1]
(rows, cols, reefs, start, end) = helper.read_input(data_path)
binary_map = helper.draw_map(rows, cols, reefs, start, end)
path = helper.find_shortest_path(binary_map, start, end)
map = helper.generate_map(binary_map, start, end, path)
helper.write_output(data_path, map)
