import helper
import sys

example_path = r"C:\Users\Charles\Desktop\path-finding\input"
example_path += "\path-error.txt"

#TODO: handle command line arguements
data_path = example_path
# data_path = sys.argv[1]
(rows, cols, reefs, start, end) = helper.read_input(data_path)
binary_map = helper.draw_map(rows, cols, reefs, start, end)
path = helper.find_shortest_path(binary_map, start, end, data_path)
map = helper.generate_map(rows, cols, binary_map, start, end, path)
helper.write_output(data_path, map)

# print(rows, cols, reefs, start, end)
# print(path)
# print(map)
