# What is the difference between the sum of the squares, and the square of the sums, of the first 100 natural numbers?
sumofsquares = 0
squareofsums = 0
a, b = 0, 0

for x in range(101):
  a += x**2
  b += x

b = b**2

print "Result:", b - a
