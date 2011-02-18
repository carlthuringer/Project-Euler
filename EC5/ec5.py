# What is the smallest number evenly divisible by all of the numbers from 1 to 20

#  TODO Identify each prime less than the upper bound, then each power of that prime less than the upper bound, then multiply all those factors together to find the result for upper bound N.

target = float(20)
# Determined that it's bigger that 1627920
# target = 1627920
divisor = 2
goal = False
results = []
incrementor = 20
hit = 20
bestresult = 0
# In an attempt to speed the process, we shall add the smallest divisor yet found to the incrementer each time a new maximum has been found. Theory is that if we go up by 20 each time, then find one that is divisible by 19, we should go up by 20 + 19 each time thereafter... And so on.
while divisor <= target:
  results.append(divisor)
  divisor += 1

while goal == False:
  divisor = 20
  while divisor >= 2:
    print target, hit, bestresult
    if target % divisor != 0: 
      break
    elif divisor == 2:
      goal = True
      print "The smallest number is", target
    else:
      results[divisor - 2] = target
      if divisor <= hit:
        incrementor += divisor
        hit -= 1
        bestresult = target
    divisor -= 1
  target += incrementor
print results
