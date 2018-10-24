def fact(n):
  if n<=1:
    return 1
  else: return n*fact(n-1)


def n_choose_k(n, k):
  return fact(n)/(fact(n-k)*fact(k))




#pick 1:
# 57 
# 56
# 55
# 2 same, the rest 7 is different:
# 3 same, the rest 4 is different:
# 4 same
# 5 same
# 6 same
# 7 same
# 8 same
if __name__ == '__main__':
  print(n_choose_k(65,9)-57)
