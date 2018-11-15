# jimmy shen
# this code is used to vis the Fibonacci Sequence and also the golden ratio
# refreence
# https://www.mathsisfun.com/numbers/fibonacci-sequence.html
import matplotlib.pyplot as plt
def fibonacci(n):
  if n==0: return 1
  elif n==1: return 2
  else:
    if n in memo:
      return memo[n]
    else:
      result = fibonacci(n-1)+fibonacci(n-2)
      memo[n] = result
      return memo[n]
if __name__ == '__main__':
  memo = {}
  # a toy test
  a_toy_test= False
  if a_toy_test:
    for n in range(1,10):
      print(fibonacci(n))
  ns = list(range(1,100))
  fibonacci_ns = [fibonacci(n) for n in ns]
  golden_ratios = [fibonacci(n)/fibonacci(n-1) for n in ns]
  plt.scatter(ns[:10], fibonacci_ns[:10])
  plt.title('fibonacci sequence')
  plt.show()
  plt.close()
  plt.scatter(ns, golden_ratios)
  plt.title('fibonacci sequence')
  plt.show()
