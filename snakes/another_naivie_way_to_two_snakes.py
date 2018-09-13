def two_snakes(n):
      result=0
      for head_snake1 in range(1,n+1):
        for tail_snake1 in range(1,n+1):
          for head_snake2 in range(1,n+1):
           for tail_snake2 in range(1, n+1):
             # check whether this 4 tuples satisfy the constraints.
             if head_snake1>tail_snake1 and tail_snake1>head_snake2 and  head_snake2>tail_snake2 and head_snake1%2 != tail_snake1%2 and head_snake2%2 != tail_snake2%2: 
               result = result+1
      return result


checkboard_size = 8
result = two_snakes(checkboard_size*checkboard_size)
print(result)
