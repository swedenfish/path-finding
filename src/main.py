import helper

matrix = [
  [1, 0, 1, 1, 1],
  [1, 0, 1, 1, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 1]
]

path = helper.find_path(matrix, (0,0), (4,3))
print(path)