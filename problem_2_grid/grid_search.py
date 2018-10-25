# give each point a cooridinate(i,j)
# traverse all the location to find the contradacted solution
import matplotlib.pyplot as plt
grids = [[i,j] for i in range(5) for j in range(5)]
#import numpy as np
#grids = np.zeros((5,5), dtype=np.int)

#for row in range(5):
#  for col in range(5):
#    grids[row, col] = 
#print(grids)

def plot(grids, color='#7f7f7f', size=2, alpha=0.5):
  x=[grid[0] for grid in grids]
  y=[grid[1] for grid in grids]
  plt.scatter(x,y,c=color, s=size, alpha=alpha)
def vis_longest_tried_paths(longest_tried_paths, grids):
  for i,tried_path in enumerate(longest_tried_paths):
    print('tried_path', tried_path)
    plot(grids, color='#7f7f7f', size=20, alpha=0.5)
    plot(tried_path, color='#d7191c', size=50, alpha=0.95)
    plt.savefig(str(i)+'.png',dpi=2000)
    plt.show()

def get_num_points_in_this_line(next_black_point, previous_point):
  # if the two points are in same row or col, return 5 immediately
  if next_black_point[0] == previous_point[0] or next_black_point[1] == previous_point[1]:
    # print(next_black_point, previous_point)
    # print('same row or same col')
     return 5
  #print('I am here')
  # the line equation defined by two points. 
  number_of_points_in_this_line = 0
  x1, y1 = next_black_point
  x2, y2 = previous_point
  m = (y1-y2)/float(x1-x2)
  b = y1-m*x1
  for grid in grids:
    x, y = grid
    if y == m*x+b:
     number_of_points_in_this_line += 1
  #print(number_of_points_in_this_line)
  return number_of_points_in_this_line
    
    
def find_solution(start_search_point, grids):
  used_black_points = [start_search_point]
  solutions = []
  tried_paths =[]
  open_list = []
  i, j = start_search_point
  for row in range(5):
    for col in range(5):
      if row != i and col!= j:
        open_list.append([row,col])
  #print(len(open_list))
  while open_list:
    next_black_point = open_list.pop()
    #print(open_list)
    every_previous_point_is_good = True
    for previous_point in used_black_points:
     # print('previous_point','next_black_point')
      #print(previous_point,next_black_point)
      number_of_points_in_this_line = get_num_points_in_this_line(next_black_point, previous_point)
      if number_of_points_in_this_line>2:
        every_previous_point_is_good = False
        break
    if every_previous_point_is_good:
      used_black_points.append(next_black_point)
      print('used_black_points', used_black_points)
      if len(used_black_points)>=5:
        print('solution found')
        solutions.append(used_black_points)
        return solutions
  tried_paths.append(used_black_points)
  print('solution not found')
  return tried_paths
tried_paths = []
for start_search_point in grids:
  tried_paths += find_solution(start_search_point, grids)
print(tried_paths)
longest_tried_paths = [_ for _ in tried_paths if len(_)==4]
print(longest_tried_paths)
vis_longest_tried_paths(longest_tried_paths, grids)
