import math
def norm1(vector):
  x=0
  for i in range(len(vector)):
    x+=abs(vector[i])
  return x


def norm2(vector):
  x=0
  for i in range(len(vector)):
    x+=vector[i]**2
  return (math.sqrt(x))

def infnorm(vector):
  x=0
  for i in range(len(vector)):
    if abs(vector[i]) > x:
      x= abs(vector[i]) 
  return x

vector=[2,3]
print(norm1(vector))

#pnorm 6/18/2018

def normp(vector,p):
  x=0
  for i in range(len(vector)):
      x+=abs(vector[i])**p
  return x**(1/p)

vector = [1,-8,2,10]
for p in range (1,25):
  print(normp(vector,p))

