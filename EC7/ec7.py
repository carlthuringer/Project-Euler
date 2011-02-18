# Find the 10001th prime

targetprime = 10001
count = 1
working = 1
biggestprime = 0

while count < targetprime:
  working += 1
  for x in range(2, working):
    if working % x == 0:
      break
    elif x == working - 1:
      count += 1
      print "Working:", working, "Primes:", count
      break
  
  
print "The answer is:", working
      
