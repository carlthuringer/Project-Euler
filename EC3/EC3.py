# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


import time

query = 600851475143
#query = 13195
target = 0
current = 1
starttime = time.clock()
while current < query:
  isprime = 0
  timepassed = time.clock() - starttime
  timeremaining = timepassed / (1 - current/query)
  print "Current:", current, "Target:", target, "Isprime:", isprime, "Remaining: {hours}:{minutes}.{seconds}".format(hours=int(timeremaining / 3600), minutes=int(timeremaining / 60), seconds=timeremaining % 60)
  if query % current == 0:
    isprime = 2
    while isprime < current:
      if current % isprime == 0:
        print isprime, "is a factor of", current
        break
      timepassed = time.clock() - starttime
      timeremaining = timepassed / (1 - current/query)
      print "Current:", current, "Target:", target, "Isprime:", isprime, "Remaining: {hours}:{minutes}.{seconds}".format (hours=int(timeremaining / 3600), minutes=int(timeremaining / 60), seconds=timeremaining % 60)      
      if isprime > target:
        target = isprime + 1
      isprime += 1
  current += 1
  
print "Largest prime factor is", target
