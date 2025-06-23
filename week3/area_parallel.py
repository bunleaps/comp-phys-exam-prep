import math, time
from multiprocessing import Process, Value, Manager

# Globals
N = 25000000
eps = 1e-10
a = -1
b = 1
h = (b-a)/(N*4)

# True integral
#Area_true = 1.57079632679
Area_true = 0.5 * math.pi
Area = Value('d', 0) 

# Rectangular Method
def circle_area(k, a, b, N, Area):
  S = 0
  h = (b-a)/N
  for i in range(0, N):
    x_h = a + i*h
    y_h = math.sqrt(1 - x_h * x_h)
    S += y_h

  Area.value +=  h * S
  print("Process %i - %f" % (k, Area.value))


if __name__ == '__main__':  
  rng = [[-1, -0.5], [-0.5,0], [0,0.5], [0.5,1]]
  # create a Process object    
  p = []

  for i in range(4):
    p.append(Process(target=circle_area, args=(i, rng[i][0], rng[i][1], N, Area,)))
   
  # start time
  st = time.time()
    
  for i in range(4):
     p[i].start()
  for i in range(4):
     p[i].join()
  for i in range(4):
     p[i].close()
    
  err = abs(Area_true - Area.value)
  print("True area:\t", Area_true)
  print("Approximate:\t", Area.value)
  print("Step h:", h)
  print("Error: ", err)

  # end time
  en = time.time()
  print("Processing time:", en-st)

   
