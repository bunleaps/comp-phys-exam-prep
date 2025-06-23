import math, time

#Area_true = 1.57079632679
Area_true = 0.5 * math.pi
eps = 1e-10

N = 100000000
h = 2/N

# start time
st = time.time()

Area = 0
for i in range(N):
    x_h = -1 +(i+1)*h
    y_h = math.sqrt(1 - x_h*x_h)
    Area += h * y_h

err = abs(Area_true - Area)
print("True area:\t", Area_true)
print("Approximate:\t", Area)
print("Step h:",h)
print("Error: ", err)

# end time
en = time.time()
print("Processing time:",en-st)

