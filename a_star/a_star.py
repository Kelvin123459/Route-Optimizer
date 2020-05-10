from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import pandas as pd

df = pd.read_csv (r'C:\Users\rexre\OneDrive\Documents\UPRM\AI\Project\Route-Optimizer\map.csv') #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
#df = pd.DataFrame(data, columns= ['Client Name','Country'])
print (df)

matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
grid = Grid(matrix=matrix)

start = grid.node(0, 0)
end = grid.node(2, 2)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))