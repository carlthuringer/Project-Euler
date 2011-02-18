# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import math

largest = 0
for a in range(1000, 99, -1):
  for b in range(1000, 99, -1):
    product = str(a * b)
    print "Working: A={0}, B={1}, Product={2}, Largest = {3}".format(a, b, int(product), largest)
    reverse = ""
    for x in product:
      reverse = x + reverse[:]
    if product == reverse and reverse != "":
      print "Palindrome found!", a*b
      print "Product of:", a, "and", b
      if a * b > largest:
        largest = a * b
      

      
      
    
