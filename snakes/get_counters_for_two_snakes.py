def factorial(n):
   factorial_n = 1
   n=int(n)
   for i in range(1,n+1):
     factorial_n = factorial_n*i
   return factorial_n

def n_choose_2(n):
   # using formular here
   # https://en.wikipedia.org/wiki/Binomial_coefficient
   if n<2: return 0
   return factorial(n)/(factorial(n-2)*factorial(2))
     

def get_number_for_one_snake(number_grids):
   # given number of grids available, output how many snakes can be put under the constrains that the head can not have the same color as the tail
   # it has two cases, the number of grids is even and the number of grids is odd
   if number_grids%2==0:
     half_number_grids = number_grids/2
     result = n_choose_2(number_grids) - 2*n_choose_2(half_number_grids)
   else:
     half_number_grids = (number_grids-1)/2
     result = n_choose_2(number_grids-1) - 2*n_choose_2(half_number_grids)
     result += half_number_grids
   return result
def get_number_for_two_snake(number_grids):
   result = []
   print('snake1_head, snake1_tail, counter_snake2')
   for head in range(number_grids,2,-1):
     for tail in range(head-1,2,-1):
       # if they have different color
       if head%2 != tail%2:
         rest_number_of_grids = tail-1
         how_many_possible_of_putting_the_second_snake= get_number_for_one_snake(rest_number_of_grids)
         result.append(int(how_many_possible_of_putting_the_second_snake))
         print('{:3d} {:3d} {:3d}'.format( head, tail,int(how_many_possible_of_putting_the_second_snake)))
   return sum(result)

if __name__ == '__main__':
  grid_size_n = 2
  grid_size_n =  int(input("Enter the checkboard size n: "))
  number_grids = grid_size_n*grid_size_n
  one_snake_result =  get_number_for_one_snake(number_grids)
  two_snake_result =  get_number_for_two_snake(number_grids)
  print('We can put ', one_snake_result, 'different one snakes if the checkboard size is ', grid_size_n)
  print('We can put ', two_snake_result, 'different two snakes if the checkboard size is ', grid_size_n)

     
   
