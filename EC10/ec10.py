#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

bounding_condition = 2000000
prime_sum = 2

for current_num in xrange(3, bounding_condition + 1, 2):
    is_prime = True
#    for testprime in xrange(3, current_num / 2 , 2):
    for testprime in xrange(3, (current_num ** 0.5) + 1, 2):
        if current_num % testprime == 0:
#            print "%", testprime, "= 0!"
            is_prime = False
            break
    if is_prime:
        print "current_num:", current_num,
        print "Is Prime!"
        prime_sum += current_num
            
print "prime_sum:", prime_sum
